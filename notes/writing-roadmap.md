# 寫作路線圖（Writing Roadmap）

**最後更新**：2026-05-21
**對應策略**：寫作目前以「累積、SEO 自然成長」為導向，不主動對外推廣。
**並進文件**：
- [writing-themes.md](writing-themes.md) — 10 條主題線的長期版圖（策略型，較少更新）
- [tools-roadmap.md](tools-roadmap.md) — 工具優先策略（文章是副產品）

> 📂 **拆檔說明**：2026-05-21 把原本一檔的 roadmap 拆成兩份。**這份檔（writing-roadmap.md）負責操作層**——進度快照、寫作節奏、發稿順序（這週要做什麼、下篇排誰）。**[writing-themes.md](writing-themes.md) 負責策略層**——10 條主題線各自累積到哪、缺什麼（新題目要歸到哪條線、版圖均衡嗎）。

> ⚠️ **每次發新文章後都要回來更新此檔**：把該篇從「完稿待上」移到「已上稿」表格，並更新 [writing-themes.md](writing-themes.md) 對應主題線的狀態。這個 roadmap 是 live 文件，stale 之後會比沒有更糟。
>
> ⚠️ **更新前先檢查 git 進度**：跑 `git log --oneline -20 -- source/_drafts source/_posts` 看實際 commit，並 cross-check `source/_posts/` 確認 urlname 是否已發布。**不要只信 roadmap 自己的宣告**——roadmap 是 git 狀態的 downstream artifact，不是 source of truth。具體分流：
>
> - 草稿從 `_drafts/` 移到 `_posts/` → 標為「已上稿」並填實際日期
> - 草稿 commit 了但仍在 `_drafts/` → 標為「完稿待上」（如知 commit 日期請註記）
> - 其他情況 → 「規劃中」

---

## 進度快照（2026-05-20）

### 推廣里程碑

- **2026-05-07：第一次對外分享**——把 [rethinking-regression-test-value](/post/rethinking-regression-test-value/) 貼給一位 QA 同事看（暫無具體回饋，但無負面反應）。詳見 memory: `blog_promotion_stance.md`

### 已上稿（13 篇，依日期倒序）

| 日期 | 文章 | URL slug | 主題線 |
|---|---|---|---|
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

### 完稿草稿待上稿（6 篇）

| 文章 | 主題線 | 狀態備註 |
|---|---|---|
| [ai-replacement-accountability-checklist](../source/_drafts/ai-replacement-accountability-checklist.md) | AI 取代 / 當責 | 完稿（2026-04-28） |
| [ai-replacement-seminary-calling](../source/_drafts/ai-replacement-seminary-calling.md) | AI 取代 / 信仰 | 完稿（2026-04-28） |
| [qa-report-workplace-wisdom](../source/_drafts/qa-report-workplace-wisdom.md) | 大人學 / 向上管理 | 完稿，已清公司指紋 |
| [letter-to-new-qa-two-day-regression](../source/_drafts/letter-to-new-qa-two-day-regression.md) | 新進 QA / 回歸方法論 | 完稿，**押 2026-05-22 23:00 發布**（5/21 潤稿：加 Herzberg 保健因子段 + 文末 P.S. 回連 4 篇舊文） |
| [empty-result-ambiguity-in-filter-testing](../source/_drafts/empty-result-ambiguity-in-filter-testing.md) | 測試設計 / 篩選功能 | 完稿，**押 2026-06-06 發布** |
| [page-source-vs-find-element](../source/_drafts/page-source-vs-find-element.md) | 自動化效能 / Appium | 完稿，**押 2026-06-20 發布** |

### 草稿（已寫但尚未確認完稿）

| 文章 | 主題線 | 狀態備註 |
|---|---|---|
| [pom-refactor-from-runnable-to-maintainable](../source/_drafts/pom-refactor-from-runnable-to-maintainable.md) | 技術深度 / 教材潛力 | 草稿，等思考完才動 |
| [not-just-make-manual-script-automate](../source/_drafts/not-just-make-manual-script-automate.md) | 線三 + 線五（UI 自動化 / 自動化決策） | **2026-05-15 骨架完成、4 個反思問題待答**，等想清楚 Q1-Q4 再填內容 |

> 註：原 survival-kit-when-test-stage-down 在 5/11 重寫為 [ten-minute-test-plan-when-test-stage-down](/post/ten-minute-test-plan-when-test-stage-down/)，主軸從「Survival Kit 三件事」改為「ACC 自審覆蓋率」，已排程 5/13 上稿。

### 規劃文件（_drafts/，不會直接成為文章）

- [analogy-series-proposals.md](analogy-series-proposals.md) — PDT 類比系列（醫生 / 記者 / 偵探 / 讀者）
- [book-ideas-qa-growth-guide.md](book-ideas-qa-growth-guide.md) — 讀書延伸題目（《QA 職涯手冊》七個切角）
- [tools-roadmap.md](tools-roadmap.md) — PDT/Self-Review Agent 工具路線
- [pdt-coach-session-2026-05-12-insights.md](coach-sessions/2026-05-12-insights.md) — PDT Coach 首次使用：自我審查 / 跨團隊協作 / 金流無主之地
- [pdt-coach-session-2026-05-13-insights.md](coach-sessions/2026-05-13-insights.md) — **「該做 vs 想做」**（首次下載三種語義 / A-B 工作取捨 / PM 訪談）
- [pdt-coach-session-2026-05-14-insights.md](coach-sessions/2026-05-14-insights.md) — **「不是退讓，是調整佔用」**（三天故事收尾 / Owner 敘事 / Coach 沒給安慰）
- [pdt-coach-session-2026-05-20-insights.md](coach-sessions/2026-05-20-insights.md) — **D4-D9「不是退讓，是調整射程」**（90/10 節奏 / 八個月醞釀 / 三選項框架 / 自我打折 / facilitator / 失落是 senior 成本）— **六天累積，密度最高的一場**
- [pdt-coach-session-2026-05-21-insights.md](coach-sessions/2026-05-21-insights.md) — **Org-Signal Coach 模式**「想要偽裝成怕失去」+「B 堆是流量不是存量」（會議真相 / 站位戰略 / prototype 權力學 / 馬拉松配速）— **最深揭曉：三個月期待往顧問走偽裝成怕被裁**
- [rethinking-regression-sequel-idea.md](rethinking-regression-sequel-idea.md) — 〈4 個刪測試問題加第 5 個〉的續篇 idea（5/15）
- [yes-man-sequel-what-qa-still-owns.md](yes-man-sequel-what-qa-still-owns.md) — yes-man 發後讀者會問的續篇 idea（5/20）
- [cant-teach-while-doing.md](cant-teach-while-doing.md) — 〈我懂了我爸做水電時為什麼沒辦法邊教邊做〉（5/20）
- [pm-bug-management-structural-DRAWER.md](pm-bug-management-structural-DRAWER.md) — 🗄️ Framing B 抽屜文（暫不發表）
- [qa-self-review-agent-prompt-v1.md](qa-self-review-agent-prompt-v1.md) — PDT Coach v1 系統 prompt


---

# 主題線地圖

> 📂 **已移至** [writing-themes.md](writing-themes.md)（10 條主題線的長期版圖）。
>
> 那邊看：新題目該歸到哪條線、這條線缺什麼、版圖均衡嗎。
> 這邊看：這週發什麼、下篇排誰、發稿節奏怎麼控。

---

# 整體寫作節奏（2026-05-20 校準）

> 上次校準是 2026-05-11。9 天進展：ten-minute-test-plan 5/13 已上稿、新加 5 條線（線十無主之地、PDT Coach session insights 等）、PDT Coach 四場連續對話累計 13 個自省題目擠在線六、yes-man 5/20 即將發。

## 庫存壓力（持續）

目前完稿草稿庫存：
- 4 篇彈性發布：accountability-checklist、seminary-calling、qa-report-workplace-wisdom、letter-to-new-qa
- 2 篇排程發布：empty-result（6/6）、page-source（6/20）
- 1 篇骨架完成、4 個反思問題待答：not-just-make-manual-script-automate
- 1 篇剛完成、即將發：ai-as-yes-man-rd-pm-trust-calibration（5/20）

寫作不缺東西，**缺的還是發稿節奏 + 主題線輪替紀律**。

## ⚠️ 線六密度警示（2026-05-20 加）

PDT Coach 四場 session 累積 **13 個自省 / 大人學題目**全擠在線六。如果照題目浮現順序連發，**部落格會給人「自省過載 / 心靈雞湯」的觀感**，傷品牌定位。

**主題線輪替紀律**：
- **同一線發稿至少間隔 3-4 週**
- **連續三篇必須跨至少兩條主題線**
- **線六每個月最多發 1 篇**——其他自省題目排隊等

## 接下來 1-2 週的建議發佈節奏（2026-05-20 校準）

| # | 文章 | 主題線 | 理由 |
|---|---|---|---|
| 1 | **ai-as-yes-man-rd-pm-trust-calibration** ⭐ | 線二 AI 取代 | 5/20 即將發。「方法論為內、AI 為殼」策略第一個對外案例 |
| 2 | **letter-to-new-qa-two-day-regression** ⭐ | 線四 測試紀律 | 跨線換調性（從 AI 議題回到紮實方法論）。5/21 潤稿完成、加 P.S. hub 設計（回連 4 篇舊文）。**frontmatter 排 2026-05-22 23:00**，比原 5/24-5/25 目標提前 2-3 天 |
| 3 | **ai-test-output-default-reader-is-ai** | 線二 AI literacy | 跟 yes-man 配對形成「Working with AI Output 雙篇」（會問 + 會讀）。**目標發稿：5/28-5/30**，跟 yes-man 隔 8-10 天最有記憶點 |
| 4 | empty-result-ambiguity-in-filter-testing | 線五 測試設計 | 排程 6/6，自動上 |

## 接下來 4-6 週的紀律建議（2026-05-20 加，**特別重要**）

**🚫 4-6 週內避開的事**：
- 不要發**任何**線六（自省 / 大人學 / 向上管理）的文章——13 個題目排隊，但**現在發任何一篇都會被讀成「最近怎麼一直在抱怨 / 反省」**
- 不要連發兩篇 AI 議題（yes-man → ai-test-output 之間必須插一篇別線）
- 不要連發兩篇「跟 PM/RD 溝通」題材的文章

**✅ 4-6 週內值得排的順序**：
1. AI 議題（yes-man）→ 2. 測試紀律（letter-to-new-qa）→ 3. AI literacy（ai-test-output）→ 4. 測試設計（empty-result 排程）→ 5. **技術深度文**（pom-refactor 或 page-source，**這時候特別需要**——讓品牌從近期偏軟的「自省 + AI 議題」拉回「技術紮實」）

線六的自省題目要等**所有人都看清楚你最近不只在反省**之後再排——大約 6-7 月才考慮重新動。**特別是 5/14 那篇〈不是退讓，是調整佔用〉**——它已經標「等 3 週後檢查點過了再寫」，那個自然 cooling-off 期跟現在的密度警示剛好對得上。

## 接下來 1 個月的寫作目標

庫存清完後動的新題目：

1. **PDT × 醫生問診類比**（補招牌主張深度，[analogy-series-proposals 主菜](analogy-series-proposals.md)）
2. **Bug Report 寫作教學**（補入門 / SEO 長尾，品牌缺）

寫完這兩篇，部落格從「招牌＋零散技術文」推進到「招牌 × 技術 × 入門 × 信仰 × 職涯 × 突發應變」**七線並進**。

## 與工具路線的分工

從 2026-05-04 起採取「先工具、後文章」策略（見 [tools-roadmap.md](tools-roadmap.md)）：

- **寫作**：思想沉澱、長期 SEO、未來職涯資本
- **工具**：日常工作生產力、可被同事 / 主管看見的具體產出

兩條線會在某些題目交會。例如做完 self-review agent 用一個月後，可以寫一篇「我把 PDT 變成工具學到的事」——**先工具、後文章**會比硬擠出來的方法論文章紮實。

POM 那篇也可以走類似路線：文章先發、之後可能變成內部 workshop / 同事 onboarding 教材。

---

# SEO 策略 + 推廣節奏（2026-05-21 加）

## 三條策略原則

1. **主攻長尾關鍵字 (Long-tail Keywords)** — 不挑「軟體測試」「自動化」這種大魔王，標題佈局具體痛點。例如「Appium V2 升級 V3 踩坑紀錄」、「QA 沒權限修 Bug 怎麼辦」這種詞，搜尋量小但競爭也小，容易排第一頁
2. **建立外部連結 (Backlinks)** — Google 看「有沒有其他網站連過來」。MoT 論壇、LinkedIn、其他 QA 社群的回連會直接提升網域權重
3. **保持更新頻率** — Google 爬蟲喜歡「活著」的網站。固定發稿節奏 = 收錄與排名同步提升

## 現有已上稿文章的長尾力評估

| 文章 | 長尾關鍵字方向 | 長尾力 |
|---|---|---|
| [Selenium 踩坑筆記](/post/selenium-troubleshooting/) | By.ID 重複 ID 定位、Selenium 踩坑 | ⭐⭐⭐ |
| [Appium 3.0 遷移](/post/appium-v2-to-v3-migration/) | Appium 3.0 遷移、v2 v3 升級指南 | ⭐⭐⭐ |
| [語音測試 × FFmpeg](/post/audio-testing-ffmpeg/) | FFmpeg 語音聊天室錄音測試 | ⭐⭐⭐ |
| [10 分鐘測試計畫](/post/ten-minute-test-plan-when-test-stage-down/) | 測試站登入壞了、10 分鐘測試計畫、ACC | ⭐⭐⭐ |
| [回歸測試精簡](/post/rethinking-regression-test-value/) | 無意義回歸測試、MoT 論壇、回歸測試精簡 | ⭐⭐ |
| [黑箱測試限制](/post/black-box-limitations-and-strategy/) | 主管只想做黑箱、黑箱測試限制 | ⭐⭐ |
| [QA 績效指標](/post/qa-performance-metrics-perspective/) | QA 績效指標、測試工程師價值 | ⭐⭐ |
| [yes-man（5/20）](/post/ai-as-yes-man-rd-pm-trust-calibration/) | AI 測試 Yes Man、AI 測試結果信任 | ⭐⭐ |
| [boredom-is-a-signal](/post/boredom-is-a-signal/) | 手動測試自動化判斷、QA 自動化訊號 | ⭐⭐ |
| [spec-maintenance](/post/spec-maintenance-gray-zone/) | specs.md AI 測試案例、文件維護灰色地帶 | ⭐⭐ |
| [PDT](/post/problem-driven-testing-intro/) | 問題驅動測試、PDT — **招牌但概念性，長尾弱** | ⭐ |
| [testing-manifesto](/post/testing-manifesto/) | 測試靈魂提問——sticky 頁，本身不靠長尾 | — |

## 待發草稿的長尾力評估（**找下一篇可優先發的**）

| 草稿 | 長尾關鍵字方向 | 長尾力 | 建議發稿時機 |
|---|---|---|---|
| **bug-triage-six-patterns-industry-survey** | Bug Triage 業界六種模式、QA bug 指派 | ⭐⭐⭐⭐ | 完稿即可，長尾力極強 |
| **frontend-ui-vocabulary-for-backend-qa** | 後端 QA 前端 UI 詞彙、skeleton loading | ⭐⭐⭐⭐ | 完稿即可，題目稀缺 |
| **page-source-vs-find-element** | page_source vs find_element、UI 自動化效能 | ⭐⭐⭐⭐ | 已排 6/20，極具長尾 |
| **empty-result-ambiguity-in-filter-testing** | 篩選沒結果、自動化測試 empty | ⭐⭐⭐ | 已排 6/6 |
| **not-just-make-manual-script-automate** | 手動測試轉自動化、UI 自動化分工 | ⭐⭐⭐ | 等 4 題反思答完 |
| **notest-ambiguity-skip-vs-low-confidence** | AI 測試 pass fail 不夠、notest 歧義 | ⭐⭐⭐ | 6 月中後 |
| **pom-refactor-from-runnable-to-maintainable** | POM 重構、Page Object Pattern | ⭐⭐⭐ | 6-7 月 |
| **letter-to-new-qa-two-day-regression** | 新進 QA、兩天回歸測試 | ⭐⭐ | 5/24-25（已建議） |
| **ai-test-output-default-reader-is-ai** | AI 測試案例讀不懂、AI 預設讀者 | ⭐⭐ | 5/28-30（已建議） |
| **qa-report-workplace-wisdom** | 測試報告對牛彈琴、向上管理 | ⭐⭐ | 6 月 |
| **ai-replacement-accountability-checklist** | AI 取代 QA、當責清單 | ⭐⭐ | 6 月 |

## 從長尾力看「接下來該發什麼」

原本排程：letter-to-new-qa（5/24）→ ai-test-output（5/28-30）→ empty-result（6/6 排程）→ page-source（6/20 排程）

**但長尾力角度建議調整**——目前**最強的長尾候選**有三篇是「完稿即可、未排程」：
1. ⭐⭐⭐⭐ **bug-triage-six-patterns-industry-survey**
2. ⭐⭐⭐⭐ **frontend-ui-vocabulary-for-backend-qa**
3. ⭐⭐⭐⭐ page-source-vs-find-element（已排 6/20）

**新建議節奏（長尾優先版）**：

| 順序 | 日期 | 文章 | 長尾 | 主題線 |
|---|---|---|---|---|
| 1 | 5/24-25 | letter-to-new-qa | ⭐⭐ | 線四（測試紀律） |
| 2 | 5/28-30 | **frontend-ui-vocabulary**（取代 ai-test-output） | ⭐⭐⭐⭐ | 線二 / 線八 |
| 3 | 6/3-4 | **bug-triage-six-patterns** | ⭐⭐⭐⭐ | 線十（無主之地） |
| 4 | 6/6 | empty-result（排程） | ⭐⭐⭐ | 線五 |
| 5 | 6/12-15 | ai-test-output-default-reader | ⭐⭐ | 線二 |
| 6 | 6/20 | page-source-vs-find-element（排程） | ⭐⭐⭐⭐ | 線三 |

**主要調動**：把兩篇 ⭐⭐⭐⭐ 的 SEO 強文（frontend-ui-vocabulary + bug-triage）排前面，ai-test-output 推到 6 月中——這樣 **6 月前累積到 3 篇 ⭐⭐⭐⭐ 長尾文，加速 Google 收錄**。

## MoT 論壇試水的英文翻譯選擇

⚠️ **首先確認**：這是推廣節奏的躍進（從內部試水→國際社群），[blog_promotion_stance](C:\Users\user1\.claude\projects\c--Users-user1-Documents-GitHub-jiamingla-github-io\memory\blog_promotion_stance.md) memory 還停在「不主動對外推廣」——MoT 試水代表進一步。決定推之前可以再評估一次心理準備度。

### 📌 2026-05-21 校準：MoT 並不「嚴格」（事實檢驗版）

先前 SEO 段裡寫過「**國際社群比同事嚴格**」——這個判斷**沒有數據支持**，被使用者問「如何知道？」之後承認是猜的。

**實際 fact-check** [rethinking-regression-test-value 引用的那個 MoT thread](https://club.ministryoftesting.com/t/are-we-running-too-many-regressions-than-required/87169) 之後：

| 維度 | 實際數據 |
|---|---|
| 回覆數 | 10 則 |
| 參與者 | 8-9 人 |
| 調性分布 | 建設性經驗分享 ~60% / 批評性分析 ~25% / 中立提問 ~15% |
| 嚴厲反對意見 | **無** |
| 對新人友善度 | **友善且歡迎**，無門檻設置 |
| 反覆出現的核心框架 | 成本效益分析、風險導向、test ownership、data-driven decision |

**重新校準後的真實畫面**：
- ❌ 不是「嚴格」——是「**直接但友善**」
- ❌ 不是「會被酸」——是「**會收到建設性回應，但可能完全沒人理**」
- ✅ 真正的風險是「**慢熱 + 反應週期長**」——sometimes 留言會在 2-4 週後才出現
- ✅ 這個 thread 跟使用者文章主張**高度共鳴**（kinofrost 批評「大型套件的恐懼心態」=== 使用者主張「無意義的回歸測試」）

### 翻譯首選：[rethinking-regression-test-value](/post/rethinking-regression-test-value/)

理由（5/21 fact-check 後更強）：
1. ⭐ **直接跟那個 thread 對話**——文章本身就 cite 了這個 thread，翻成英文後 = 「**一個沉澱版的 reply**」加入既有討論
2. **主題對齊 MoT 受眾**——回歸測試成本效益是 MoT 經常討論的議題（從上面的 fact-check 看到核心框架完全重疊）
3. **5/7 已內部試水成功**——讀者驗證過、可信度高
4. **長尾力 ⭐⭐ 中等**——但加上 MoT 回連，網域權重會跳很快
5. **不涉及任何台灣公司情境**——translation 阻力最低
6. **kinofrost 那則批判跟你的主張共鳴**——你的翻譯可以直接 quote 他然後延伸，這在 MoT 文化裡是被歡迎的「building on each other」動作

### 翻譯次選：[ai-as-yes-man-rd-pm-trust-calibration](/post/ai-as-yes-man-rd-pm-trust-calibration/)

理由：
1. **MoT 受眾近期火紅議題**：AI in testing
2. **觀點尖、辨識度高**——「AI 不是你的 QA，是你的 Yes Man」這種主張在英文圈也少見
3. 但**剛 5/20 發、還沒累積中文讀者數據**——可能先讓中文版跑 1-2 週看反應再翻

### 不建議首翻

- **PDT 介紹** — 概念性太強、翻成英文容易撞既有 exploratory testing / context-driven 流派論述
- **boredom-is-a-signal** — 文化色彩重（"煩" 這個中文情緒詞），翻譯後力道會弱
- **testing-manifesto** — 個人開台宣言，國際社群不關心

### 試水流程建議（5/21 校準版）

1. 翻譯 `rethinking-regression-test-value` 成英文（保留作者風格、不要太正式化）
2. **去那個既有 thread 留言**（[are-we-running-too-many-regressions-than-required](https://club.ministryoftesting.com/t/are-we-running-too-many-regressions-than-required/87169)）——而**不是開新 thread**。理由：
   - 留言形式 = 加入既有對話，沒人理也很正常
   - 新 thread 形式 = 要承受「我新開的 thread 沒人理」的個人化解讀
   - Backlink 效果一樣（連結還是回到部落格）
   - thread 已有 10 則回覆、8-9 人關注——還有活性
3. **留言寫法建議**：可以 quote kinofrost 那則批判「大型套件的恐懼心態」當引子，然後說「I had a similar reflection from a Taiwanese QA's angle, written it up here: [連結]」——這是 MoT 文化裡最受歡迎的「**building on a previous comment**」姿態
4. 觀察 **2-4 週**反應——MoT 反應週期長，1 週沒人留言是常態
5. 如果反應好（有人回應、有人 click 連結）→ 翻第二篇
6. 反應冷淡也不要立刻退——慢熱社群本來就這樣
7. **絕對不要做的事**：去翻譯後**回頭刪掉留言**或**頻繁編輯**——這在小社群裡會被注意到

---

# 2026 年中目標：iThome 鐵人賽（探索中）

> ℹ️ 關於鐵人賽的評估（包含機會成本、3個主題方向與 4 個月準備期排程等），因篇幅較長，已獨立至專屬規劃文件：
> 👉 [ithome-ironman-2026-planning.md](ithome-ironman-2026-planning.md)
