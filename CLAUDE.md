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

