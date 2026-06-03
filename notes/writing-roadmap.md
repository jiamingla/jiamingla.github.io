# 寫作路線圖（Writing Roadmap）

**最後更新**：2026-06-04
**對應策略**：寫作目前以「累積、SEO 自然成長」為導向，不主動對外大肆推廣，但 6 月起啟動國際社群（Ministry of Testing）的精準試水。
**並進文件**：
- [writing-themes.md](writing-themes.md) — 13 條主題線的長期版圖（策略型，較少更新）
- [tools-roadmap.md](tools-roadmap.md) — 工具優先策略（文章是副產品）

> 📂 **拆檔說明**：2026-05-21 把原本一檔的 roadmap 拆成兩份。**這份檔（writing-roadmap.md）負責操作層**——進度快照、寫作節奏、發稿順序（這週要做什麼、下篇排誰）。**[writing-themes.md](writing-themes.md) 負責策略層**——13 條主題線各自累積到哪、缺什麼（新題目要歸到哪條線、版圖均衡嗎）。

> ⚠️ **每次發新文章後都要回來更新此檔**：把該篇從「完稿待上」移到「已上稿」表格，並更新 [writing-themes.md](writing-themes.md) 對應主題線的狀態。這個 roadmap 是 live 文件，stale 之後會比沒有更糟。

> ⚠️ **更新前先檢查 git 進度**：跑 `git log --oneline -20 -- source/_drafts source/_posts` 看實際 commit，並 cross-check `source/_posts/` 確認 urlname 是否已發布。**不要只信 roadmap 自己的宣告**——roadmap 是 git 狀態的 downstream artifact，不是 source of truth。

---

## 進度快照（2026-06-04）

### 推廣里程碑

- **2026-05-07：第一次對外分享**——把 [rethinking-regression-test-value](/post/rethinking-regression-test-value/) 貼給一位 QA 同事看（無負面反應）。
- **2026-06 月計畫**：首度試水國際社群（Ministry of Testing 論壇），透過回覆既有討論串分享 Rethinking Regression 英文版，並發布 Frontend UI Vocabulary 英文 adapted 版以建立反向連結。

### 已上稿（15 篇，依日期倒序）

| 日期 | 文章 | URL slug | 主題線 |
|---|---|---|---|
| 2026-06-03 | QA 該認識的 32 個前端 UI 詞彙——從 AI 給我 skeleton loading 那天開始補的課 | frontend-ui-vocabulary-for-qa | 線二 / 線八 |
| 2026-05-22 | 給新進 QA 的第一封信：如何在兩天內穩定的回歸測試完一個產品？ | letter-to-new-qa-two-day-regression | 線十一 / 線四 |
| 2026-05-20 | 你以為 AI Agent 在做稱職的 QA，其實它在當你的 Yes Man | ai-as-yes-man-rd-pm-trust-calibration | AI literacy / 「方法論為內、AI 為殼」策略首發 |
| 2026-05-13 | 測試站登入壞了那天：我真的測完了嗎？ | ten-minute-test-plan-when-test-stage-down | 突發應變 / 自我審視 / 信仰 |
| 2026-05-06 | 「煩」是 QA 的診斷工具 | boredom-is-a-signal | 自動化決策 / 信仰 |
| 2026-05-03 | 用 specs.md 餵 AI 之前 | spec-maintenance-gray-zone | AI 取代 / 組織 |
| 2026-04-24 | 問題驅動測試（PDT） | problem-driven-testing-intro | **招牌主張** ✓ |
| 2026-04-17 | 太多「無意義」的回歸測試嗎？ | rethinking-regression-test-value | 測試紀律 |
| 2026-04-08 | QA 績效指標視角 | qa-performance-metrics-perspective | 職涯 / KPI |
| 2026-03-31 | 黑箱測試的限制與策略 | black-box-limitations-and-strategy | 方法論 |
| 2026-03-26 | Appium 3.0 遷移 | appium-v2-to-v3-migration | 技術實戰 |
| 2026-03-24 | 語音測試 × FFmpeg | audio-testing-ffmpeg | 技術實戰 |
| 2026-01-29 | 開台宣言 | testing-manifesto | 招牌（藍圖） |
| 2026-01-20 | Selenium 踩坑筆記 | selenium-troubleshooting | 技術實戰 |
| 2026-01-18 | Hello World | hello-world | 開台 |

### 完稿草稿待上稿（5 篇）

| 文章 | 主題線 | 狀態備註 |
|---|---|---|
| [empty-result-ambiguity-in-filter-testing](../source/_drafts/empty-result-ambiguity-in-filter-testing.md) | 測試設計 / 篩選功能 | 完稿，**已排程 2026-06-06 自動發布** |
| [page-source-vs-find-element](../source/_drafts/page-source-vs-find-element.md) | 自動化效能 / Appium | 完稿，**已排程 2026-06-20 自動發布** |
| [ai-replacement-accountability-checklist](../source/_drafts/ai-replacement-accountability-checklist.md) | AI 取代 / 當責 | 完稿（2026-04-28），待定時間發布 |
| [ai-replacement-seminary-calling](../source/_drafts/ai-replacement-seminary-calling.md) | AI 取代 / 信仰 | 完稿（2026-04-28），待定時間發布 |
| [qa-report-workplace-wisdom](../source/_drafts/qa-report-workplace-wisdom.md) | 大人學 / 向上管理 | 完稿，已清公司指紋，冷卻期後發布 |

### 草稿與規劃中（已寫但尚未確認完稿）

| 文章 | 主題線 | 狀態備註 |
|---|---|---|
| [bug-triage-six-patterns-industry-survey](../source/_drafts/bug-triage-six-patterns-industry-survey.md) | 線八 / 線十 | 完稿度 90%，長尾力極強，6 月發稿候選 |
| [ai-test-output-default-reader-is-ai](../source/_drafts/ai-test-output-default-reader-is-ai.md) | 線二 | 完稿度 80%，Working with AI 雙篇，6 月發稿候選 |
| [not-just-make-manual-script-automate](../source/_drafts/not-just-make-manual-script-automate.md) | 線三 + 線五 | 骨架已建，待解答 4 個反思問題以填實內容 |
| [notest-ambiguity-skip-vs-low-confidence](../source/_drafts/notest-ambiguity-skip-vs-low-confidence.md) | 線五 | 概念規劃中，待 empty-result (6/6) 上稿後啟動 |
| [pom-refactor-from-runnable-to-maintainable](../source/_drafts/pom-refactor-from-runnable-to-maintainable.md) | 線三 | 教材草稿階段，6-7 月工程實戰篇 |
| [frontend-ui-vocabulary-for-qa](../source/_drafts/frontend-ui-vocabulary-for-qa.md) | 線八 / 線二 | 規劃種子檔與 adapt 備忘（保留在草稿目錄） |

---

# 📅 2026 年 6 月專注計畫與發稿節奏

6 月的核心目標是**「穩固長尾 SEO 護城河」**並**「開啟國際社群低摩擦試水」**。本月不發布任何線六（自省/大人學）的文章以防止過熱，完全專注在技術實作與 AI literacy 雙維度。

## 1. 中文發稿時程表（每兩週 1 篇為主，SEO 強文適度插空）

| 順序 | 預計日期 | 文章 | 長尾力 | 主題線 | 發稿狀態 / 備註 |
|---|---|---|---|---|---|
| 1 | 6/3 (四) | **frontend-ui-vocabulary-for-qa** | ⭐⭐⭐⭐ | 線二 / 線八 | ✅ **已上稿**（融入週會 AI 案例痛點） |
| 2 | 6/6 (六) | **empty-result-ambiguity-in-filter-testing** | ⭐⭐⭐ | 線五（自動化決策）| ⏳ **已排程自動上稿** |
| 3 | ~6/12-14 | **bug-triage-six-patterns-industry-survey** | ⭐⭐⭐⭐ | 線八 / 線十 | ✍️ **本月手動主打**，極強 SEO 長尾文，月底前完成發布 |
| 4 | ~6/18-20 | **ai-test-output-default-reader-is-ai** | ⭐⭐ | 線二（AI literacy）| ✍️ 配對 yes-man 篇，月中手動發布 |
| 5 | 6/20 (六) | **page-source-vs-find-element** | ⭐⭐⭐⭐ | 線三（自動化效能）| ⏳ **已排程自動上稿** |

## 2. 6 月國際社群試水計畫 (Ministry of Testing)

### 🚀 行動 A：Rethinking Regression 英文回文 (6/5 - 6/8)
*   **目標**：將 `rethinking-regression-test-value` 整理為英文，以「回應者」姿態加入 MoT 的 [Regression 討論串](https://club.ministryoftesting.com/t/are-we-running-too-many-regressions-than-required/87169)。
*   **做法**：quote 討論區中 kinofrost 的見解，再附上自己的論點與部落格回連。

### 🚀 行動 B：Frontend Vocabulary 英文版 (6/10 - 6/12)
*   **目標**：在中文版發布一週後，推出 adapted 英文版 *"A tester's lens on frontend UI patterns"*。
*   **做法**：不採直譯，而是將 PDT 的反向應用轉為 *"AI as a vocabulary mirror"* 或 *"reverse exploratory testing"*，重點在於第三欄的 **testing heuristics**。

---

## ⚠️ 主題線輪替與紀律原則

1. **🚫 嚴格執行線六（大人學/自我審視）冷卻期**：6 月不發布任何線六文章，19 個自省題目持續留在抽屜，等 7 月後再行評估。
2. **🚫 避免 AI 議題連發**：`yes-man` 與 `frontend-ui-vocabulary` 已間隔 14 天；接下來 `ai-test-output` 將排在 `empty-result` 之後。
3. **✅ 先工具，後文章**：本月繼續以 `PDT Coach` 及 `Self-Review Agent` 工具在工作中的肉身碰撞，作為後續方法論文章的真實養分。

---

# 📖 接下來 1-2 個月的長線目標（非排程文章）

這些是更遠的長線題目——還沒進 6 月排程，但會持續放在腦中：

1. **PDT × 醫生問診類比**（補招牌主張深度，[analogy-series-proposals 主菜](analogy-series-proposals.md)）——等線六冷卻 + 招牌系列再延伸時動
2. **Bug Report 寫作教學**（補入門 / SEO 長尾——這是線八目前完全空白的位置）
3. **PDT Coach 工具實作後的反思文**（呼應 tools-first 策略——等工具用過 1-2 個月再寫）
4. **線十一（Mentorship 系列）首發**：〈我懂了我爸做水電時為什麼沒辦法邊教邊做〉
5. **線十二（單兵 QA 自動化系列）首發**：〈單兵 QA 的第一個月：不要大張旗鼓，要「悄悄進行」的影子自動化〉
6. **PDT × QBT 雙層架構戰略**：詳見 [pdt-vs-qbt-positioning.md](pdt-vs-qbt-positioning.md)。
7. **新孕育的 5 個文章角度**（從 [2026-05-28-insights.md](coach-sessions/2026-05-28-insights.md) 衍生）：
   - A.〈QBT：QA 是產品的責任編輯〉⭐⭐⭐⭐
   - B.〈接班不是接人格——讀懂組織的「實質本年結構」〉⭐⭐⭐
   - C.〈混合動機的承認——做 QA 為什麼不能 only one motive〉⭐⭐
   - D.〈個人化歸因是 QA 的職業病——強迫三解工具〉⭐⭐⭐
   - E.〈Coach 主動踩煞車——AI 助手該何時叫使用者離開？〉⭐⭐⭐⭐

---

# 📅 2026 年中目標：iThome 鐵人賽（6 月末定錨）

- 在 6 月底前決定是否參與 2026 iThome 鐵人賽，並從 3 個主題方向中定錨，啟動 4 個月的準備期。
- 專屬評估文件見：[ithome-ironman-2026-planning.md](ithome-ironman-2026-planning.md)
