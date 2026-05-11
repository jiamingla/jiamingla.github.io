# 部署運維筆記（Deployment Notes）

這份是 Hexo + GitHub Pages 部署相關的踩坑與排查紀錄。每次遇到「明明 push 了卻沒看到更新」這類問題，把過程寫進來。下次同樣問題就不用再重新查一次。

---

## 部署架構快照（2026-05-11 整理）

```
本機 source（main branch）
    │
    ↓  hexo generate
本機 public/ (產出靜態 HTML)
    │
    ↓  hexo deploy（推到遠端 gh-pages branch）
origin/gh-pages
    │
    ↓  GitHub Pages 服務讀取 gh-pages branch
https://jiamingla.github.io
    │
    ↓  CDN（Fastly）快取 + max-age=600（10 分鐘）
讀者瀏覽器
```

**關鍵設定**（`_config.yml`）：
- `future: false` — **未來日期的文章不會被 build**。要靠手動在那天之後重新 deploy 才會上線。
- `render_drafts: false` — `_drafts/` 裡的檔案不會被產生成 HTML。
- 沒有 GitHub Actions 自動 build（`.github/workflows/` 不存在）——deploy 都是本機手動跑。

---

## 事件紀錄

### 2026-05-11：boredom-is-a-signal 段落標題改動後「看不到更新」

**症狀**：使用者在 [boredom-is-a-signal](/post/boredom-is-a-signal/) 第五節段落標題從 `〈spec-maintenance-gray-zone〉` 改為 `〈用 specs.md 餵 AI〉` 後，push 完發現 live 站還是舊的。

**排查步驟**：

1. **確認 main 同步**：`git log` vs `git log origin/main` — 一致 ✓
2. **確認 gh-pages 有更新**：
   ```bash
   git log origin/gh-pages --oneline -5
   # b9ec804 Site updated: 2026-05-11 17:02:59
   ```
   ✓ 已更新
3. **確認 gh-pages branch 上的 HTML 真的有新標題**：
   ```bash
   git show origin/gh-pages:post/boredom-is-a-signal/index.html | grep "五、"
   # 顯示：<h2 id="五、與前一篇〈用-specs-md-餵-AI〉互為鏡像">...
   ```
   ✓ HTML 內容正確
4. **直接 curl live URL**：
   ```bash
   curl -s "https://jiamingla.github.io/post/boredom-is-a-signal/" | grep "五、"
   # 顯示新標題 ✓
   ```
   live 站實際吐出的 HTML 就是最新版。
5. **檢查 HTTP headers**：
   ```
   Last-Modified: Mon, 11 May 2026 09:03:43 GMT
   Cache-Control: max-age=600
   X-Cache: MISS
   Age: 0
   ```
   server 端是 cache miss，回的是最新 origin 內容。

**結論**：**部署完全成功，是讀者端瀏覽器 cache 顯示舊版**。

**根因**：GitHub Pages CDN 設 `max-age=600`（10 分鐘）。使用者在最後一次 deploy 之前打開過頁面，瀏覽器 cache 還在窗口內，重新整理也不會去 server 拿新版。

**解法**：
1. Hard refresh：`Ctrl + F5`（Windows）/ `Cmd + Shift + R`（Mac）
2. 無痕視窗
3. 等 10 分鐘以上

---

## 已知容易踩的坑

### 坑 1：`future: false` 會「靜默漏稿」

如果文章 frontmatter 寫了未來日期（例如想排程 5/13 上線），**Hexo build 時會直接跳過**，產生出來的 gh-pages 上**不會有那篇 HTML**。

GitHub Pages 也沒有「到 5/13 自動重新 build」這種能力——Hexo 沒有排程器。

**所以如果你押了未來日期，記得**：
- 那天之後一定要重跑一次 `hexo generate && hexo deploy`
- 否則那篇會永遠卡在 `_posts/` 但沒上線
- 或者改成 `future: true`（全站不再篩 future）

### 坑 2：「明明 push 了沒更新」幾乎都是 cache 不是部署失敗

排查順序（從近到遠，從便宜到貴）：

1. **Hard refresh** 或無痕視窗（90% 問題在這）
2. `curl -s <URL> | grep <你改的字>` —— 直接看 server 端吐什麼，繞過所有瀏覽器 cache
3. `git show origin/gh-pages:<path>` —— 看 deploy 完的 HTML branch 內容對不對
4. `git log origin/gh-pages` —— 確認最後一次 deploy 的時間
5. `git log origin/main` —— 確認 main 真的有 push 上去

只要 #2 看到新內容，問題一定在讀者端 cache，不是部署。

### 坑 3：本機 `gh-pages` branch 跟 origin 不同步是正常的

本機的 `gh-pages` branch 通常會落後 `origin/gh-pages` 一大截（因為 `hexo deploy` 直接 push 到 remote，不會更新本機 branch）。**這不會影響部署**。

不用每次都 `git checkout gh-pages && git pull`——除非你想看 diff。

---

## 部署 Checklist（給未來自己）

每次發新文章時：

- [ ] frontmatter `date` 是「現在或過去」？（不要押未來日期，除非你會記得回來 deploy）
- [ ] `urlname` 是英文 slug，沒有中文（連結會破）
- [ ] 文章在 `source/_posts/`，不是 `source/_drafts/`
- [ ] 本機跑過 `hexo generate` 沒報錯
- [ ] 本機 `hexo server` 預覽過，確認版面正常
- [ ] `git add` + commit + push 到 `origin/main`
- [ ] `hexo deploy` 推到 `origin/gh-pages`
- [ ] 開無痕視窗確認 live 站
- [ ] 若 push 但沒看到更新——**先 Hard refresh，再懷疑部署**

---

## 相關設定 / 文件

- `_config.yml` — Hexo 主設定
- `.github/dependabot.yml` — 只有依賴更新提醒，沒有 build workflow
- `source/_drafts/writing-roadmap.md` — 寫作節奏與進度
- `source/_drafts/tools-roadmap.md` — 工具開發路線
