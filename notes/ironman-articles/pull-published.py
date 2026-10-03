"""把 ithelp 上已發布的文章抓回本機主稿，並登記它的網址。

用法：python pull-published.py <day> <article-url-or-id> [<day> <url> ...]

為什麼要抓回來：發布之後作者會在 iThome 上直接改字，那份才是權威版本。
本機主稿是之後回填部落格的來源，兩邊必須一致，否則回填的是舊稿。

抓回來之後記得依序跑：
    resolve-links.py --write   把這篇的網址填進還在引用它的稿子
    sync-to-tool.py            把更新後的主稿同步到發文目錄
再把受影響的草稿重新 save-draft 推回 iThome，否則 iThome 上是舊版。
"""

import re
import sys
import json
import html
import pathlib
import urllib.request

HERE = pathlib.Path(__file__).parent
BLOCK = re.compile(
    r"<(h2|h3|h4|p|blockquote|ul|ol|pre|table)\b[^>]*>(.*?)</\1\s*>|<hr\s*/?>", re.S | re.I
)


def inline(fragment: str) -> str:
    fragment = re.sub(r"<br\s*/?>", "\n", fragment)
    fragment = re.sub(r"<strong>(.*?)</strong>", r"**\1**", fragment, flags=re.S)
    fragment = re.sub(r"<em>(.*?)</em>", r"*\1*", fragment, flags=re.S)
    fragment = re.sub(r"<code>(.*?)</code>", r"`\1`", fragment, flags=re.S)
    fragment = re.sub(
        r'<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>', r"[\2](\1)", fragment, flags=re.S
    )
    return re.sub(r"[ \t]+\n", "\n", html.unescape(re.sub(r"<[^>]+>", "", fragment))).strip()


def table_markdown(inner: str) -> str:
    rows = []
    for row in re.findall(r"<tr\b[^>]*>(.*?)</tr\s*>", inner, re.S | re.I):
        cells = [
            inline(cell).replace("\n", " ")
            for cell in re.findall(r"<t[hd]\b[^>]*>(.*?)</t[hd]\s*>", row, re.S | re.I)
        ]
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "|" + "---|" * width]
    lines += ["| " + " | ".join(row) + " |" for row in rows[1:]]
    return "\n".join(lines)


def to_markdown(body: str) -> str:
    out = []
    for match in BLOCK.finditer(body):
        if match.group(1) is None:
            out.append("---")
            continue
        tag, inner = match.group(1).lower(), match.group(2)
        if tag in ("h2", "h3", "h4"):
            out.append("#" * int(tag[1]) + " " + inline(inner))
        elif tag == "p":
            text = inline(inner)
            if text:
                out.append(text)
        elif tag == "table":
            text = table_markdown(inner)
            if text:
                out.append(text)
        elif tag == "blockquote":
            text = to_markdown(inner) if re.search(r"<p\b", inner, re.I) else inline(inner)
            out.append("\n".join(("> " + line if line else ">") for line in text.split("\n")))
        elif tag in ("ul", "ol"):
            lines = []
            for index, item in enumerate(
                re.findall(r"<li\b[^>]*>(.*?)</li\s*>", inner, re.S | re.I), 1
            ):
                bullet = "- " if tag == "ul" else f"{index}. "
                lines.append(bullet + inline(item).replace("\n", "\n  "))
            out.append("\n".join(lines))
        elif tag == "pre":
            out.append("```\n" + html.unescape(re.sub(r"<[^>]+>", "", inner)).strip("\n") + "\n```")
    return "\n\n".join(out)


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def register(day: int, url: str) -> None:
    path = HERE / "known-urls.json"
    data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    data[str(day)] = url
    ordered = {k: data[k] for k in sorted(data, key=lambda k: (not k.isdigit(), k.isdigit() and int(k)))}
    path.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    args = sys.argv[1:]
    if not args or len(args) % 2:
        print(__doc__)
        return 1

    for day_text, target in zip(args[::2], args[1::2]):
        day = int(day_text)
        url = target if target.startswith("http") else f"https://ithelp.ithome.com.tw/articles/{target}"
        url = url.split("?")[0]

        page = fetch(url)
        start = page.find('class="markdown__style"')
        if start < 0:
            print(f"Day{day}: 找不到文章內容，可能尚未公開或網址有誤：{url}")
            continue
        opening = page.find(">", start) + 1
        body = to_markdown(page[opening : page.find("</div>", opening)]).strip()

        local = HERE / f"Day{day}.md"
        if not local.exists():
            print(f"Day{day}: 本機沒有主稿 {local.name}，跳過")
            continue
        current = local.read_text(encoding="utf-8")
        frontmatter = current.split("---", 2)[1]

        # 線上版不一定比本機新。本機可能有還沒貼上去的修改，直接覆蓋會把它洗掉
        # （2026-10-02 真的發生過）。所以先看本機有哪些小節是線上沒有的。
        missing = set(re.findall(r"^## (.+)$", current, re.M)) - set(
            re.findall(r"^## (.+)$", body, re.M)
        )
        if missing and "--force" not in sys.argv:
            print(f"Day{day}: 中止，沒有覆蓋。本機有這些小節，線上版沒有：")
            for heading in sorted(missing):
                print(f"           ## {heading}")
            print("           代表本機的修改還沒貼到 iThome。先貼上去再抓，"
                  "或加 --force 確定要用線上版覆蓋本機。")
            continue

        local.write_text(f"---{frontmatter}---\n\n{body}\n", encoding="utf-8")
        register(day, url)

        holes = body.count("🔲")
        note = f"⚠️ 仍有 {holes} 處 🔲" if holes else "無 🔲"
        print(f"Day{day}: 已抓回 {len(re.sub(r'\\s', '', body))} 字，{note}，已登記 {url}")

    print("\n接著請跑：resolve-links.py --write，再跑 sync-to-tool.py，"
          "然後把有變動的草稿重新 save-draft 推回 iThome。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
