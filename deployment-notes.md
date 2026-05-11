# 部署運維筆記（Deployment Notes）

這份是 Hexo + GitHub Pages 部署相關的踩坑與排查紀錄。每次遇到「明明 push 了卻沒看到更新」這類問題，把過程寫進來。下次同樣問題就不用再重新查一次。

**最後更新**：2026-05-11（午後新增 GitHub Actions 自動化）

---

## 部署架構快照

```
本機 source 編輯
    │
    ↓ git push origin main
GitHub main branch
    │
    ↓ GitHub Actions（.github/workflows/deploy.yml）
    ↓ 三種觸發：push / 每日 cron / 手動
    │
    ↓ npm ci → hexo generate
    ↓ peaceiris/actions-gh-pages → push 到 gh-pages
origin/gh-pages
    │
    ↓ GitHub Pages 服務讀取 gh-pages branch
https://jiamingla.github.io
    │
    ↓ CDN（Fastly）快取 + max-age=600（10 分鐘）
讀者瀏覽器
```

**關鍵設定**：

- `_config.yml`：
  - `future: false` — 未來日期文章不會被 build（**但配 Actions cron 後，到日期那天會自動補 build**）
  - `render_drafts: false` — `_drafts/` 不會產生 HTML
- `.github/workflows/deploy.yml`（**2026-05-11 新增**）：
  - Push 到 main 自動 deploy（除了 `_drafts/` 跟操作型文件）
  - 每天 00:30 台北時間 cron rebuild（消化排程文章）
  - 手動觸發（Actions 頁面點 Run workflow）
- `package-lock.json` 已存在，Actions 用 `npm ci` 鎖版本
- 本機仍可 `hexo deploy` 手動推（向後相容），但**正常情況下不需要**

---

## Workflow 規格（`.github/workflows/deploy.yml`）

### 觸發方式

1. **Push 到 main**（除了 `_drafts/`、`README.md`、`deployment-notes.md`、`.gitignore` 這些不影響 build 的檔案）
2. **每日 cron**：`30 16 * * *` = 台北時間每天 00:30 — 用來把排程文章發出來
3. **手動觸發**：Actions 頁面點 "Run workflow"

### 流程

1. checkout main
2. `npm ci`（按 `package-lock.json` 安裝）
3. `npx hexo generate` 產出 `public/`
4. 用 `peaceiris/actions-gh-pages@v4` push 到 `gh-pages` branch

### 權限

- 用 default `GITHUB_TOKEN`，`contents: write` 權限即可
- 不需要 PAT、不需要額外 secret 設定

### Concurrency

`group: pages-deploy` + `cancel-in-progress: false` — 同時最多一個 deploy 跑，避免 push 衝突

### 一次性 GitHub 設定確認（首次推上去後要去 GH 確認）

1. **Settings → Pages**：source 設為 "Deploy from a branch"、branch 設為 `gh-pages`、folder `/ (root)`
2. **Settings → Actions → General → Workflow permissions**：設為 "Read and write permissions"（讓 `GITHUB_TOKEN` 能 push 到 gh-pages）

### Failure mode 排查

- Deploy 失敗：去 Actions 頁面看 log
- 常見原因：依賴版本問題（檢查 `package-lock.json` 同步）、`_config.yml` 語法錯、Workflow permissions 沒開

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

### 2026-05-11（後段）：建立 GitHub Actions 自動部署

**動機**：上面那次事件之外，還發現 `ten-minute-test-plan-when-test-stage-down`（押 2026-05-13）因為 `future: false` 不會被 build，**而手動 `hexo deploy` 必須在那天回來再跑一次**，是個容易漏掉的陷阱。

**做法**：新增 `.github/workflows/deploy.yml`，三種觸發：
- Push 到 main 即時部署
- 每日 cron 00:30 台北時間補 build 排程文章
- 手動觸發

**效果**：
- 押未來日期的文章會在當天自動上線，最多延遲 24 小時
- 不用再手動 `hexo deploy`
- 也順便解決「換電腦/出差就漏稿」的脆弱

---

## 已知容易踩的坑

### 坑 1：`future: false` 會「靜默漏稿」（✅ 2026-05-11 由 Actions cron 解決）

**已修復**——`.github/workflows/deploy.yml` 設了每天 00:30 台北時間的 cron，會自動 rebuild。押未來日期的文章在當天自動上線，不用人為介入。

**原始問題（保留紀錄）**：押未來日期 → Hexo build 時跳過 → 沒有 HTML 在 gh-pages 上。Hexo 本身沒有排程器，所以只靠手動 deploy 的話需要那天記得重跑。

**現在的行為**：
- 押 `2026-05-13` 的文章 → 5/13 那天的 cron 醒來 → rebuild → 上線。最多延遲 24 小時（取決於離 cron 觸發點多遠）
- 想加速：去 Actions 頁面手動 Run workflow

### 坑 2：「明明 push 了沒更新」幾乎都是 cache 不是部署失敗

排查順序（從近到遠，從便宜到貴）：

1. **Hard refresh** 或無痕視窗（90% 問題在這）
2. `curl -s <URL> | grep <你改的字>` —— 直接看 server 端吐什麼，繞過所有瀏覽器 cache
3. `git show origin/gh-pages:<path>` —— 看 deploy 完的 HTML branch 內容對不對
4. 去 GitHub Actions 頁面看最後一次 workflow 跑成功嗎
5. `git log origin/main` —— 確認 main 真的有 push 上去

只要 #2 看到新內容，問題一定在讀者端 cache，不是部署。

### 坑 3：本機 `gh-pages` branch 跟 origin 不同步是正常的

本機的 `gh-pages` branch 通常會落後 `origin/gh-pages` 一大截（Actions 推到 remote，不會更新本機 branch）。**這不會影響部署**。

不用每次都 `git checkout gh-pages && git pull`——除非你想看 diff。

---

## 部署 Checklist（給未來自己）

每次發新文章時：

- [ ] `urlname` 是英文 slug，沒有中文（連結會破）
- [ ] 文章在 `source/_posts/`，不是 `source/_drafts/`
- [ ] frontmatter `date` 設好（**可以押未來日期，cron 會自動補發**）
- [ ] 本機 `hexo server` 預覽過，確認版面正常
- [ ] `git add` + commit + push 到 `origin/main`
- [ ] （**Actions 會自動 deploy，不用再手動跑 `hexo deploy`**）
- [ ] 到 [Actions 頁面](https://github.com/jiamingla/jiamingla.github.io/actions) 確認 workflow 跑成功（綠勾 ✓）
- [ ] 開無痕視窗確認 live 站
- [ ] 若 push 但沒看到更新——**先 Hard refresh，再懷疑部署**

排程文章（押未來日期）：
- [ ] 押好日期，push 到 main，**就完事了**——不用設行事曆提醒、不用記日子
- [ ] 那天想看有沒有上線：到 Actions 頁面看當天 00:30 那次 cron 跑成功嗎

---

## 相關設定 / 文件

- `_config.yml` — Hexo 主設定
- `.github/workflows/deploy.yml` — Build & deploy 自動化（2026-05-11 新增）
- `.github/dependabot.yml` — 依賴更新提醒
- `package.json` / `package-lock.json` — Node 依賴清單
- `source/_drafts/writing-roadmap.md` — 寫作節奏與進度
- `source/_drafts/tools-roadmap.md` — 工具開發路線
