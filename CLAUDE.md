# CLAUDE.md

Project conventions for AI assistance in this Hexo blog repository.

This is a personal blog at https://jiamingla.github.io built with Hexo. Posts focus on QA engineering, 問題驅動測試 (problem-driven testing), and 品質工程.

## Repository structure

- `source/_drafts/` — work-in-progress posts and planning files (writing roadmap, tools roadmap, draft articles)
- `source/_posts/` — published posts (deployed via GitHub Actions)
- `themes/` — Hexo theme files
- `_config.yml` — Hexo config (note custom permalink format below)

## Internal link format

Internal links between blog posts MUST use `/post/<urlname>/`, NOT the date-based path `/YYYY/MM/DD/<slug>/`.

The Hexo config customizes permalinks to `/post/:urlname/`. Date-based links will return 404 in production.

When linking from one post's body to another, use the `urlname:` value from the target post's frontmatter:

```markdown
See [related post](/post/related-post-urlname/) for background.
```

## Writing roadmap maintenance

`source/_drafts/writing-roadmap.md` tracks the publication pipeline. It is a live document with three status buckets: 已上稿 / 完稿待上 / 規劃中.

Before editing entries in this roadmap, verify the actual status against git — do not just propagate what the roadmap currently claims.

Workflow:

1. Run `git log --oneline -20 -- source/_drafts source/_posts` to see recent commits affecting drafts or published posts
2. Check `source/_posts/` for the urlname if unsure whether a draft has been published
3. Update status accordingly:
   - Draft moved from `_drafts/` to `_posts/` → mark as 已上稿 with the actual file date
   - Draft committed but stays in `_drafts/` → mark as 完稿待上 (mention commit date if known)
   - Otherwise → 規劃中

The roadmap's own header warns: "stale 之後會比沒有更糟." Treat the roadmap as a downstream artifact of git state, not as the source of truth itself.
