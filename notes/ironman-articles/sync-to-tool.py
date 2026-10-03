"""把主稿（含 frontmatter）轉成工具要的格式，同步到發文用的目錄。

用法：python sync-to-tool.py [--day N]
不指定 --day 就同步全部。

主稿是 notes/ironman-articles/DayNN.md，有 Hexo 的 frontmatter，之後回填部落格用。
工具吃的是 articles/<series>/DayNN.md，第一行必須是 `# Day NN｜標題`，沒有 frontmatter。
兩份的本文必須一致，否則發出去的會是舊版。
"""

import re
import sys
import pathlib

HERE = pathlib.Path(__file__).parent
TOOL_ARTICLES = pathlib.Path(
    r"C:\Users\user1\orca\workspaces\ithome-ironman-autopost\articles\the-other-half"
)


def convert(path: pathlib.Path) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"{path.name} 沒有 frontmatter")
    title = re.search(r"^title:\s*(.+)$", parts[1], re.M)
    if not title:
        raise ValueError(f"{path.name} 的 frontmatter 沒有 title")
    return title.group(1).strip(), parts[2].strip()


def main() -> int:
    only = None
    if "--day" in sys.argv:
        only = int(sys.argv[sys.argv.index("--day") + 1])

    TOOL_ARTICLES.mkdir(parents=True, exist_ok=True)
    synced = 0
    for path in sorted(HERE.glob("Day*.md")):
        match = re.match(r"Day(\d{1,2})\.md$", path.name)
        if not match:
            continue
        day = int(match.group(1))
        if only is not None and day != only:
            continue

        title, body = convert(path)
        target = TOOL_ARTICLES / f"Day{day}.md"
        target.write_text(f"# Day {day}｜{title}\n\n{body}\n", encoding="utf-8")
        synced += 1

        holes = body.count("🔲")
        flag = f"⚠️ 含 {holes} 處 🔲，發布會被擋" if holes else "可發布"
        print(f"Day{day:<3} {title[:34]:<36} {flag}")

    print(f"共同步 {synced} 篇")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
