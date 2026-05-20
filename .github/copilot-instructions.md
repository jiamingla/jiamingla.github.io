# GitHub Copilot Instructions

This is **jiamingla.github.io**——繁體中文個人部落格，Hexo 架構，主題 QA 工程 / 問題驅動測試（PDT）/ 品質工程。

作者偏好**誠實、不誇大**的 commit messages 跟內容生成——避免「Yes Man」式的 puffy phrasing。這是 personal blog，**不是公司專案**——commit 訊息不需要 marketing tone、不需要組織內部公文體。

Project structure 跟內部慣例見 [CLAUDE.md](../CLAUDE.md)。

---

## Commit Message 規範（**最重要**）

### 動詞要跟「檔案位置」匹配

不同位置的檔案，commit 訊息該用不同等級的動詞——**狀態 ≠ 規模**：

| 檔案位置 | 該用的動詞 | 不該用的動詞 |
|---|---|---|
| `notes/*.md` | 新增**備忘** / 擴充 idea / 整理觀察 / 更新筆記 | ❌ 新增文章 / 定義 / 強化 |
| `source/_drafts/*.md` | 新增**草稿** / 補骨架 / 補實戰素材 / 補章節 | ❌ 新增文章 / 強調 / 提升 |
| `source/_posts/*.md`（新檔） | 新增**文章** | （這時才該用，不要提早用） |
| `source/_posts/*.md`（修改） | 更新文章 / 補連結 / 修字句 | ❌ 強化結構 / 定義 |
| 檔案搬動 / 重命名 | `refactor:` | （不用 `feat:`） |
| 純小修正 | `fix:` | （不用 `feat:`） |

**判斷流程**：先看檔案在哪個目錄 → 再決定動詞 → 再決定 conventional prefix（feat/docs/refactor/fix）。

### 禁用的「政策化 / 公文化」用語

這些詞讓 personal blog commit 聽起來像公司公文，**請避免生成**：

| 禁用 ❌ | 替代 ✅ |
|---|---|
| 強調 X 的重要性 | 補 X 段落 |
| 強化 SEO 及讀者定位 | 調整標題 / 補 tag |
| 定義專案規範 | 補專案慣例紀錄 |
| 探討 X 的本質與分工 | 新增討論 X 的初稿 |
| 以提升測試信心度 | （直接刪這一段） |
| 更新 X 結構，新增 Y 框架對比及 Z 概念 | 補一段 Y 對比 |
| 強調 X 的核心價值 | 補 X 章節 |
| 觀察到 X 的結構性 Y，建議改為 Z | 補一段觀察：X 可改為 Z |

### Conventional commit prefix 對應

- `feat:` — 真的新增 user-facing 內容（新文章、新章節）
- `docs:` — 文檔 / notes / 內部紀錄（**這個 repo 的 `notes/` 多半該用這個**）
- `refactor:` — 純粹的檔案移動 / 重命名 / 重組
- `fix:` — 修錯誤、修錯字、修壞掉的 link
- `ci:` — `.github/workflows/` 改動

### Scope 建議（選用）

- `(posts)` — 動到 `source/_posts/`
- `(drafts)` — 動到 `source/_drafts/`
- `(notes)` — 動到 `notes/`
- `(workflow)` — 動到 `.github/workflows/`

### 範例

**✅ 好的範例**：

```
docs(notes): 5/20 PDT Coach session insights + v1.x 第 12 面向

- 新增 coach-sessions/2026-05-20-insights.md
- writing-roadmap: 校準到 5/20、補線六密度警示
```

```
feat(posts): 新增文章「你以為 AI Agent 在做稱職的 QA」
```

```
feat(drafts): 補 not-just-make-manual-script-automate 骨架的實戰素材
```

```
refactor: move meta files from source/_drafts/ into notes/
```

**❌ 不好的範例**（過去發生過的）：

```
❌ feat: 新增文章「分工我擅長，協作我不行」，探討教學與操作的認知成本
    → 檔案實際在 notes/，是備忘不是文章；「探討⋯認知成本」太宏大
    → 應改：docs(notes): 新增〈分工我擅長，協作我不行〉備忘

❌ feat: 更新 AI 測試角色認知，強調 RD/PM 提問習慣的重要性，新增三個關鍵問題以提升測試信心度
    → 「強調⋯重要性」「以提升⋯信心度」是公文體
    → 應改：feat(drafts): 補 ai-as-yes-man 三個提問清單

❌ feat: 新增業界 Bug 預設指派的六種模式對照及七種 backlog workaround，強化 SEO 及讀者定位
    → 「強化 SEO 及讀者定位」是 marketing tone
    → 應改：feat(drafts): 新增 bug-triage 六種模式對照
```

---

## 風格 priors（給內容生成時參考）

- **誠實 > 顯眼**：寧可寫「補一段觀察」也不要寫「強化論述」
- **動詞跟著規模走**：改 1 段話 → 「補」/「加」；新增整個檔案 → 「新增」；跨檔案重組 → 「refactor」
- **不用 marketing / corporate tone**：personal blog 不需要 SEO / 讀者定位 / 業界對比 / 框架升維 這種語彙
- **不要替「未來會做」的事 commit**：commit 紀錄的是**已做的事**，不是意圖
- **保留作者聲音**：使用者的 commit 偏好親近、口語、誠實——不要套用通用工程團隊的 PR 體
- **句長控制**：commit subject line ≤ 50 字（中文等同 25 個漢字），body 視需要展開

---

## 內部慣例 cross-reference

- `_drafts/` = 「未來確定要發的文章」（草稿）
- `notes/` = 反思 / 規劃 / 工具設定 / 抽屜文（不會發為 blog 文章）
- 詳細慣例見 [CLAUDE.md](../CLAUDE.md)
- Internal links between posts MUST use `/post/<urlname>/`（見 CLAUDE.md「Internal link format」段）
