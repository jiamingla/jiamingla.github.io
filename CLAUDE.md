# CLAUDE.md

Project conventions for AI assistance in this Hexo blog repository.

This is a personal blog at https://jiamingla.github.io built with Hexo. Posts focus on QA engineering, 問題驅動測試 (problem-driven testing), and 品質工程.

## Repository structure

- `source/_drafts/` — **ONLY future article drafts** (will be published as blog posts). Files here are committed-to-write articles, not planning notes.
- `source/_posts/` — published posts (deployed via GitHub Actions)
- `notes/` — meta / planning / reflection files that are NOT future articles. Includes:
  - Roadmaps (`writing-roadmap.md` 操作層 + `writing-themes.md` 策略層, `tools-roadmap.md`, `ithome-ironman-2026-planning.md`)
  - Writing proposals (`analogy-series-proposals.md`, `book-ideas-qa-growth-guide.md`)
  - Tool configs (`qa-self-review-agent-prompt-v1.md`)
  - Drawer files / unpublishable drafts (`pm-bug-management-structural-DRAWER.md`)
  - Ops notes (`deployment-notes.md`)
  - `notes/coach-sessions/` — PDT Coach session insights (`<YYYY-MM-DD>-insights.md`)
- `themes/` — Hexo theme files
- `_config.yml` — Hexo config (note custom permalink format below)

### Convention: where things go

**Going into `source/_drafts/`** = "this will be published as a blog post" (even if scheduled / locked / waiting). If a file is reflection, planning, tool config, or a proposal, it belongs in `notes/`, not `_drafts/`.

`notes/` is outside `source/`, so Hexo never processes it — files there can never accidentally appear on the blog.

## Internal link format

Internal links between blog posts MUST use `/post/<urlname>/`, NOT the date-based path `/YYYY/MM/DD/<slug>/`.

The Hexo config customizes permalinks to `/post/:urlname/`. Date-based links will return 404 in production.

When linking from one post's body to another, use the `urlname:` value from the target post's frontmatter:

```markdown
See [related post](/post/related-post-urlname/) for background.
```

