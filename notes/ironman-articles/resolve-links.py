"""把文章裡的 🔲DAYnn 佔位連結，換成 ithelp 上實際發布的網址。

用法：python resolve-links.py [--write]
不加 --write 只報告，不改檔。

三個來源，依優先序合併：
  1. known-urls.json —— 手動登記，給沒經過工具發布的篇章用
  2. 工具的 receipts —— 發布當下就寫好，最即時
  3. 系列 RSS —— 備援。有數小時延遲，所以不能當主要來源

RSS 會濾掉標題裡的標點（「」。等），比對前先正規化。
"""

import re
import sys
import json
import pathlib
import urllib.request

SERIES_RSS = "https://ithelp.ithome.com.tw/rss/series/9947"
HERE = pathlib.Path(__file__).parent
RECEIPTS = pathlib.Path(
    r"C:\Users\user1\orca\workspaces\ithome-ironman-autopost\output\receipts"
)
TOKEN = re.compile(r"🔲DAY(\d{1,2})")


def normalize(title: str) -> str:
    return re.sub(r"[\s\W_]+", "", title, flags=re.UNICODE)


def from_overrides() -> dict[int, str]:
    path = HERE / "known-urls.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {int(k): v for k, v in data.items() if k.isdigit()}


def from_receipts() -> dict[int, str]:
    found = {}
    if not RECEIPTS.exists():
        return found
    for path in RECEIPTS.glob("*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, OSError):
            continue
        day, url, status = data.get("day"), data.get("publicUrl"), data.get("status")
        if isinstance(day, int) and isinstance(url, str) and status in {"published", "already-published"}:
            found[day] = url
    return found


def from_rss(titles: dict[int, str]) -> dict[int, str]:
    try:
        request = urllib.request.Request(SERIES_RSS, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            xml = response.read().decode("utf-8")
    except OSError as error:
        print(f"（RSS 讀取失敗，略過這個來源：{error}）")
        return {}

    published = {}
    for item in re.findall(r"<item\b[^>]*>([\s\S]*?)</item>", xml):
        raw_title = re.search(r"<title\b[^>]*>([\s\S]*?)</title>", item)
        link = re.search(r"<link\b[^>]*>([\s\S]*?)</link>", item)
        if not raw_title or not link:
            continue
        text = raw_title.group(1)
        cdata = re.match(r"\s*<!\[CDATA\[([\s\S]*?)\]\]>\s*$", text)
        published[normalize((cdata.group(1) if cdata else text).strip())] = (
            link.group(1).strip().split("?")[0]
        )

    return {
        day: published[normalize(title)]
        for day, title in titles.items()
        if normalize(title) in published
    }


def day_titles() -> dict[int, str]:
    titles = {}
    for path in sorted(HERE.glob("Day*.md")):
        match = re.match(r"Day(\d{1,2})\.md$", path.name)
        if not match:
            continue
        head = path.read_text(encoding="utf-8")[:600]
        title = re.search(r"^title:\s*(.+)$", head, re.M)
        if title:
            titles[int(match.group(1))] = title.group(1).strip()
    return titles


def main() -> int:
    write = "--write" in sys.argv
    titles = day_titles()

    sources = {
        "RSS": from_rss(titles),
        "receipt": from_receipts(),
        "手動登記": from_overrides(),
    }
    resolved, origin = {}, {}
    for name, mapping in sources.items():  # 後者覆蓋前者，優先序由低到高
        for day, url in mapping.items():
            resolved[day] = url
            origin[day] = name

    changed, remaining = 0, set()
    for path in sorted(HERE.glob("Day*.md")):
        text = path.read_text(encoding="utf-8")
        tokens = {int(d) for d in TOKEN.findall(text)}
        if not tokens:
            continue
        new_text = text
        for day in sorted(tokens & resolved.keys()):
            new_text = new_text.replace(f"🔲DAY{day}", resolved[day])
        still = sorted({int(d) for d in TOKEN.findall(new_text)})
        remaining.update(still)
        if new_text != text:
            changed += 1
            if write:
                path.write_text(new_text, encoding="utf-8")
            print(f"{path.name}: 已填 {sorted(tokens & resolved.keys())}，仍待補 {still}")

    print(json.dumps({
        "可回填": {d: f"{resolved[d]}  ({origin[d]})" for d in sorted(resolved)},
        "仍缺連結的 Day": sorted(remaining),
        "模式": "已寫入" if write else "僅報告（加 --write 才改檔）",
        "異動檔案數": changed,
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
