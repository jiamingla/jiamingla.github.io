# 寫作路線圖（Writing Roadmap）

**最後更新**：2026-06-11
**對應策略**：寫作目前以「累積、SEO 自然成長」為導向，不主動對外大肆推廣。**6 月不推廣**——用「沒人在看」的空窗刻意練 publish-then-revise（發了再反覆讀、反覆改）來克服完美主義；國際社群（Ministry of Testing）試水延到**報名 iThome 鐵人賽的當週**才啟動（報名動作 = 「準備好對外」的觸發點，試水搭著那股氣勢一起做）。
**並進文件**：
- [writing-themes.md](writing-themes.md) — 13 條主題線的長期版圖（策略型，較少更新）
- [tools-roadmap.md](tools-roadmap.md) — 工具優先策略（文章是副產品）

> 📂 **拆檔說明**：2026-05-21 把原本一檔的 roadmap 拆成兩份。**這份檔（writing-roadmap.md）負責操作層**——進度快照、寫作節奏、發稿順序（這週要做什麼、下篇排誰）。**[writing-themes.md](writing-themes.md) 負責策略層**——10 條主題線各自累積到哪、缺什麼（新題目要歸到哪條線、版圖均衡嗎）。

> ⚠️ **每次發新文章後都要回來更新此檔**：把該篇從「完稿待上」移到「已上稿」表格，並更新 [writing-themes.md](writing-themes.md) 對應主題線的狀態。這個 roadmap 是 live 文件，stale 之後會比沒有更糟。
>
> ⚠️ **更新前先檢查 git 進度**：跑 `git log --oneline -20 -- source/_drafts source/_posts` 看實際 commit，並 cross-check `source/_posts/` 確認 urlname 是否已發布。**不要只信 roadmap 自己的宣告**——roadmap 是 git 狀態的 downstream artifact，不是 source of truth。具體分流：
>
> - 草稿從 `_drafts/` 移到 `_posts/` → 標為「已上稿」並填實際日期
> - 草稿 commit 了但仍在 `_drafts/` → 標為「完稿待上」（如知 commit 日期請註記）
> - 其他情況 → 「規劃中」
>
> ⚠️ **更新時優先改舊段、不要直接 append**（2026-05-25 加紀律）：這個檔案非常容易累積「5/20 校準的」「5/21 加的」「5/25 加的」三個版本同時存在的混亂。**動筆前先問自己**：
>
> 1. 我要改的是哪個既有 section？能不能就地更新，而不是在底下新加？
> 2. 如果我在新加，是否其實該**替換掉**某個舊的？
> 3. 既有的「（YYYY-MM-DD 加）」標記是否該升日期 / 已 stale 該刪？
>
> Append 比 update 容易，但 append 會讓檔案逐月變沉。**讀者（包括未來的自己）要在三個版本之間判斷哪個才是真的——那一刻 roadmap 就失去 source-of-truth 的功能了**。

---

## 進度快照（2026-06-08）

### 推廣里程碑

- **2026-05-07：第一次對外分享**——把 [rethinking-regression-test-value](/post/rethinking-regression-test-value/) 貼給一位 QA 同事看（暫無具體回饋，但無負面反應）。詳見 memory: `blog_promotion_stance.md`

### 已上稿（21 篇，依日期倒序）

| 日期 | 文章 | URL slug | 主題線 |
|---|---|---|---|
| 2026-06-11（排程） | 你的團隊 Bug 預設給誰？業界六種主流 Bug 分派（Triage）模式對照 | bug-triage-six-patterns-industry-survey | 線十 / 線八 |
| 2026-06-10 | 【踩坑紀錄】uv + PyTorch + PyQt5 在 Windows 的 DLL 衝突：完整根因與解決方案 | uv-torch-pyqt5-dll-conflict | 線三 |
| 2026-06-08 | 【職場大人學】老闆要的不是綠燈，是心安：為什麼你的測試報告總是「對牛彈琴」？ | qa-report-workplace-wisdom | 線六 |
| 2026-06-07 | 如果有一天我被 AI 取代了，我大概會去讀神學院 | ai-replacement-seminary-calling | 線七 |
| 2026-06-06 | UI 自動化跑得慢？先別怪裝置——page_source 與 find_element 的成本完全不同 | page-source-vs-find-element | 線三 |
| 2026-06-06 | 篩選後沒結果，是資料真的沒符合條件，還是篩選功能壞掉了？——自動化測試的五種解法 | empty-result-ambiguity-in-filter-testing | 線五 |
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

### 完稿草稿待上稿（0 篇，在 _drafts/）

| 文章 | 主題線 | 長尾 | 狀態備註 |
|---|---|---|---|
| (無) | — | — | 所有完稿皆已移至 posts 排程上稿 |

> 註 1：原列此處的 ai-replacement-accountability-checklist 已於 2026-06-05 移回 [notes/](ai-replacement-accountability-checklist.md)（重構為「品質責任編輯當責模型」骨架），不再是待上稿草稿。
> 註 2：**bug-triage-six-patterns**——6/8 一度降為規劃檔（揭露邊界 gating），同日揭露邊界定案（前公司只示範 F+E、不掛 QA 第一手、現公司不寫）後**已生成全文並排程 2026-06-10**，移入 _posts/。規劃檔 [bug-triage-six-patterns-planning.md](bug-triage-six-patterns-planning.md) 保留決策紀錄。

### 草稿（已寫但尚未確認完稿）

| 文章 | 主題線 | 狀態備註 |
|---|---|---|
| [notest-ambiguity-skip-vs-low-confidence-planning](../source/_drafts/notest-ambiguity-skip-vs-low-confidence-planning.md) | 線二（AI 測試判讀） | ⭐⭐⭐ 長尾。已積 ~21k 字（比「骨架」成熟，但未確認完稿）。6 月中後 |
| [pom-refactor-from-runnable-to-maintainable](../source/_drafts/pom-refactor-from-runnable-to-maintainable.md) | 技術深度 / 教材潛力 | ⭐⭐⭐ 長尾。已融入 AI 價值，暫不發布，保留作為個人技術與工程備忘 |
| [not-just-make-manual-script-automate](../source/_drafts/not-just-make-manual-script-automate.md) | 線三 + 線五（UI 自動化 / 自動化決策） | ⭐⭐⭐ 長尾。系列第一篇總綱已完成草稿，隨時可發布 |

> 註：原 survival-kit-when-test-stage-down 在 5/11 重寫為 [ten-minute-test-plan-when-test-stage-down](/post/ten-minute-test-plan-when-test-stage-down/)，主軸從「Survival Kit 三件事」改為「ACC 自審覆蓋率」，已排程 5/13 上稿。

### 規劃文件（notes/，不會直接成為文章）

- [successor-communication-and-ai-impatience.md](successor-communication-and-ai-impatience.md) — **2026-06-10 新**：大人學接班人（溝通樞紐）的實踐、尋求平行肯定，以及 AI 即時回饋帶來的「組織耐性赤字」反思。
- [white-label-app-testing-strategy.md](white-label-app-testing-strategy.md) — **2026-06-10 新**：白牌/多 App 自動化測試的痛點分析與漸進式定位抽象策略。
- [bug-triage-six-patterns-planning.md](bug-triage-six-patterns-planning.md) — **2026-06-08 新**：bug-triage 六種模式對照的素材 + 待思考問題。**gating decision = 揭露邊界**（改用兩間前公司第一手案例，去識別化 / 法務距離 / 情緒中立想清楚才生成文章）。⭐⭐⭐⭐ 長尾，線八主場 + 線十前傳
- [pom-refactor-from-runnable-to-maintainable-planning.md](pom-refactor-from-runnable-to-maintainable-planning.md) — **2026-06-09 新**：大四實習時的 POM 啟蒙與現今實踐對照，並思考封裝良好的 Page Object 在 AI 時代作為 Agent Tool API 的全新戰略價值。
- [analogy-series-proposals.md](analogy-series-proposals.md) — PDT 類比系列（醫生 / 記者 / 偵探 / 讀者）
- [book-ideas-qa-growth-guide.md](book-ideas-qa-growth-guide.md) — 讀書延伸題目（《QA 職涯手冊》七個切角）
- [tools-roadmap.md](tools-roadmap.md) — PDT/Self-Review Agent 工具路線
- [pdt-coach-session-2026-05-12-insights.md](coach-sessions/2026-05-12-insights.md) — PDT Coach 首次使用：自我審查 / 跨團隊協作 / 金流無主之地
- [pdt-coach-session-2026-05-13-insights.md](coach-sessions/2026-05-13-insights.md) — **「該做 vs 想做」**（首次下載三種語義 / A-B 工作取捨 / PM 訪談）
- [pdt-coach-session-2026-05-14-insights.md](coach-sessions/2026-05-14-insights.md) — **「不是退讓，是調整佔用」**（三天故事收尾 / Owner 敘事 / Coach 沒給安慰）
- [pdt-coach-session-2026-05-20-insights.md](coach-sessions/2026-05-20-insights.md) — **D4-D9「不是退讓，是調整射程」**（90/10 節奏 / 八個月醞釀 / 三選項框架 / 自我打折 / facilitator / 失落是 senior 成本）— **六天累積，密度最高的一場**
- [pdt-coach-session-2026-05-21-insights.md](coach-sessions/2026-05-21-insights.md) — **Org-Signal Coach 模式**「想要偽裝成怕失去」+「B 堆是流量不是存量」（會議真相 / 站位戰略 / prototype 權力學 / 馬拉松配速）— **最深揭曉：三個月期待往顧問走偽裝成怕被裁**
- [pdt-coach-session-2026-05-27-insights.md](coach-sessions/2026-05-27-insights.md) — **Org-Signal Coach 三天**（5/25-27）：北極星 + Head 被拒不受傷 + **比較表上桌**。**最深揭曉：B 堆不是 QA 主場、C 堆才是；訓練面對反駁是練論點硬度不是膽量**。新孕育 7 個文章角度（A 文「UX vs 系統行為裂縫」最強）
- [2026-05-31-brand-value-and-smoke-test-proposal.md](coach-sessions/brand-value-and-smoke-test-proposal.md) — **品牌價值與冒煙測試提案**（異常處理價值 / 向上管理劇本 / 技術與業務共生策略）
- [pdt-coach-session-2026-05-28-insights.md](coach-sessions/2026-05-28-insights.md) — **Org-Signal Coach 三天**（5/28-30）：**本年地圖大校正**（Head 是支撐桿、接班 = 接 Head 不是 Manager）+ 跟接班對象第一次微妙分歧 + 混合動機承認 + 個人化歸因警覺 + Coach 5/30 主動踩煞車。新孕育 5 個文章角度（A 文「QBT 責任編輯」⭐⭐⭐⭐ + E 文「Coach 該何時叫使用者離開」⭐⭐⭐⭐ 最強）
- [pdt-coach-session-2026-06-01-insights.md](coach-sessions/2026-06-01-insights.md) — **Org-Signal Coach 三天**（6/1-3）：**「被看見會自然發生」實證**（IB 事件鏈印證 5/28 權力地圖）+ 「工作不是全部的出口」personal 覺察 + 「你跟 QA-A 的分野」定位浮現（組織派 vs 技術派）+ 綠燈做決策 / 紅燈做執行內化。新孕育 8 個文章角度（C「組織派 vs 技術派」⭐⭐⭐⭐ + G「報告一眼看懂」⭐⭐⭐⭐ 最強、跟 [first-principle](software-testing-first-principle.md) 強連動）
- [pdt-coach-session-2026-06-04-insights.md](coach-sessions/2026-06-04-insights.md) — **Org-Signal Coach 六天**（6/4-9）：**自己踩煞車能力成形**（自己診斷紅燈 + 切回 + 比 Coach 更務實判斷）+ 對外溝通內外有別（RD-Al 事件）+ 樞紐 ≠ 客服 reframe + 「想職涯是想工作的高級偽裝」（請假日鏡子）+ **核心測試發現「測不了的已知風險」**（[first-principle](software-testing-first-principle.md) 活案例）+ 讀懂 Head 不給 PM 太多文件原則（DTNO 例子、補 5/29 分歧）+ 跟同類型 PM-Ve 溝通的盲點。**新孕育 8 個文章角度**（A「測不了的已知風險」⭐⭐⭐⭐ + D「不會忙到沒成長」⭐⭐⭐⭐ + F「同類型人溝通盲點」⭐⭐⭐⭐ 最強）
- [pdt-vs-qbt-positioning.md](pdt-vs-qbt-positioning.md) — **2026-06-01 戰略檔**：QBT 不是業界 established term（WebSearch + Preely 驗證後）；Preely 的 QBT 在 UX 領域、不撞義；PDT 對內 / QBT 對外的雙層架構討論。**rebrand 成本評估：PDT 投資 47 檔案不划算**
- [rethinking-regression-sequel-idea.md](rethinking-regression-sequel-idea.md) — 〈4 個刪測試問題加第 5 個〉的續篇 idea（5/15）
- [yes-man-sequel-what-qa-still-owns.md](yes-man-sequel-what-qa-still-owns.md) — yes-man 發後讀者會問的續篇 idea（5/20）
- [cant-teach-while-doing.md](cant-teach-while-doing.md) — 〈我懂了我爸做水電時為什麼沒辦法邊教邊做〉（5/20）
- [cross-app-locator-strategy.md](cross-app-locator-strategy.md) — 跨 APP 測試框架的元素定位策略（漸進式三階段：fallback chain → LocatorStrategy → per-APP class）。**含公司指紋**，blog 化需洗（5/28）→ ⭐⭐⭐⭐ 長尾力，建議落線三、跟 pom-refactor 形成 POM 雙篇
- [pm-bug-management-structural-DRAWER.md](pm-bug-management-structural-DRAWER.md) — 🗄️ Framing B 抽屜文（暫不發表）
- [qa-self-review-agent-prompt-v1.md](qa-self-review-agent-prompt-v1.md) — PDT Coach v1 系統 prompt


---

# 主題線地圖

> 📂 **已移至** [writing-themes.md](writing-themes.md)（10 條主題線的長期版圖）。
>
> 那邊看：新題目該歸到哪條線、這條線缺什麼、版圖均衡嗎。
> 這邊看：這週發什麼、下篇排誰、發稿節奏怎麼控。

---

# 整體寫作節奏（2026-06-04 校準）

> 上次校準是 2026-06-01（3 天前）。這 3 天進展：
> - 6/1-3 Org-Signal Coach 三天：**「被看見會自然發生」實證**（IB 帳號誠實事件 → Head 帶到 Lead → Lead 拍板）、印證 5/28 校正權力地圖
> - **6/3 最深揭曉**：你跟 QA-A 的分野——他走技術 / AI 賦能、你走組織 / 流程 / 可讀性。**這正是 RD Head-style QA Head 的位置**
> - 衍生 8 個新文章角度（C「組織派 vs 技術派」⭐⭐⭐⭐ + G「報告一眼看懂」⭐⭐⭐⭐ 最強）
> - 線六累積已破 40 candidates、配額**長期透支**——這場應優先發 C / G（**不是線六**）
>
> 上次校準是 2026-05-25（7 天前）。前 7 天進展：
> - 5/28 frontend-ui-vocabulary-for-qa 結構整理完成（H2 整理、章節從六章重整為五章 + 結語、6 個待思考問題嵌入正文）
> - 5/29 早上完成第一份顯性化 PDT 文件（影音直播 + 語音直播），自己用立「QBT 責任編輯」框架
> - 5/30 Coach 主動踩煞車（週六不展開）、使用者重新檢視部落格方向
> - **2026-06-01：發現 PDT vs QBT 命名戰略議題**——驗證後 QBT 不是業界 established term、Preely 的 QBT 在 UX 領域不撞義。詳見 [pdt-vs-qbt-positioning.md](pdt-vs-qbt-positioning.md)
> - **frontend-ui-vocabulary 順利解鎖**（6/4 融入週會 AI 案例痛點重新定位，6 個問題已修改完畢，隨時可排程發布）
> - 5/28-30 Org-Signal Coach 三天：本年地圖大校正、混合動機承認、個人化歸因警覺 —— 衍生 5 個新文章角度，最強是「QBT 責任編輯」⭐⭐⭐⭐

## 庫存壓力（2026-06-08 校正）

目前 _drafts/ **3 支**主草稿，按發稿成熟度：
- **完稿待上（0）**：所有完稿皆已排程
- **已積大量字數但未確認完稿（2）**：notest-ambiguity（~21k 字）、pom-refactor（~17k 字）
- **骨架階段（1）**：not-just-make-manual-script-automate-planning（4 個反思問題待答）

> 2026-06-08 校正：原寫「7 支」並把 ai-replacement-accountability-checklist 列為完稿待上——該檔已於 6/5 移回 notes/。同日 bug-triage 因改用前公司第一手案例、揭露邊界待解，移到 notes/ 成規劃檔，_drafts/ 從 6 支再減為 5 支。

**六月策略**：不推廣 = 沒人在看，所以「還沒 100% 滿意」不再是擋發稿的理由。發了再反覆讀、反覆改（publish-then-revise，刻意拿來打完美主義）。主題線輪替紀律仍守，但節奏快慢在六月不是問題。

寫作不缺東西，**缺的還是發稿節奏 + 主題線輪替紀律**。

## ⚠️ 線六密度警示（2026-05-21 升級）

PDT Coach 五場 session 累積 **19 個自省 / 大人學題目**全擠在線六。如果照題目浮現順序連發，**部落格會給人「自省過載 / 心靈雞湯」的觀感**，傷品牌定位。

**主題線輪替紀律**：
- **同一線發稿至少間隔 3-4 週**
- **連續三篇必須跨至少兩條主題線**
- **線六每個月最多發 1 篇**——其他自省題目排隊等

## 接下來 4-6 週的紀律建議（**特別重要**）

**🚫 4-6 週內避開的事**：
- 不要發**任何**線六（自省 / 大人學 / 向上管理）的文章——19 個題目排隊，但**現在發任何一篇都會被讀成「最近怎麼一直在抱怨 / 反省」**
- 不要連發兩篇 AI 議題（中間必須插別線）
- 不要連發兩篇「跟 PM/RD 溝通」題材的文章

**✅ 6-7 月才考慮重啟線六**：
等所有人都看清楚你最近不只在反省之後再排——大約 6-7 月。**特別是 5/14 那篇〈不是退讓，是調整佔用〉**——它已標「等 3 週後檢查點過了再寫」，cooling-off 期跟密度警示剛好對得上。

## 📌 接下來節奏（具體排程）

**現役表格在下方 SEO 策略段的「[從長尾力看接下來該發什麼](#從長尾力看接下來該發什麼)」**——SEO 策略升級了原本的 5/20 純主題線排程，把長尾力評估納入排序邏輯。**請以下方那張表為準**，這裡不重複列。

## 接下來 1 個月的長線目標（非排程文章）

下方 SEO 段的「接下來節奏」處理 4-6 週內具體要發什麼。這節是**更遠的長線題目**——還沒進排程，但會持續放在腦中：

### 🎯 UI 自動化測試的反思與設計美學系列（2026-06-10 新增）

1. **系列（一）：〈不要只是把手動測試腳本自動化：為什麼「直接搬運」是自動化專案崩盤的開始？〉**
   - **urlname**: `not-just-make-manual-script-automate`
   - **狀態**: 已完成草稿，暫不發布，保留作為本地備忘與沉澱。
2. **系列（二）：〈綠燈下的盲區：自動化測試中的「資訊坍縮」與隱性品質防護的流失〉**
   - **urlname**: `ui-automation-information-collapse`
   - **思考方向**: 
     - 人類手動測試的「眼角餘光檢查」如何量化？機器只看 DOM node，那我們是否能在核心斷言外，加上某些「全域健康指標斷言」（例如：監控 Console Error、驗證特定的佈局變動 CLS 指標、或是用輕量的視覺比較工具僅驗證關鍵 Container，而非比對整張圖）？
     - 寫下「當你看到全綠的 CI，你到底敢不敢拍胸脯保證品質？」的心理對照。
3. **系列（三）：〈放過 UI 元素吧！解耦 UI 動作與「資料狀態斷言」的自動化實戰〉**
   - **urlname**: `decouple-ui-actions-and-assertions`
   - **思考方向**: 
     - E2E 測試的底線在哪裡？如果我們只用 UI 點擊，但驗證點全部換成 API response 與 Database，這到底算不算 E2E 測試？
     - 具體實作上，如何設計一個乾淨的 `assert_db_state()` 或 `assert_event_triggered()` 封裝，讓撰寫測試案例的人不需要寫複雜的 SQL 或呼叫 API，而是維持高階語義？
4. **系列（四）：〈自動化測試案例的半衰期：為什麼你該有刪除測試的「垃圾回收（GC）」機制？〉**
   - **urlname**: `test-case-half-life-and-garbage-collection`
   - **思考方向**: 
     - 建立一個簡單的「測試價值評估公式」：`價值 = (抓到的 bug 數量 * 嚴重度) / (維護排錯時間 * 執行時間)`。
     - 當一條測試的價值分數小於某個臨界值時，我們該如何建立團隊內的「刪除授權與機制」？如何說服主管「刪除這個測試能讓我們跑得更快更穩」？
5. **系列（五）：〈AI 時代的自動化測試：我們不再寫步驟，我們寫 Page API 與觀測指標〉**
   - **urlname**: `ai-testing-era-page-api-and-observability`
   - **思考方向**: 
     - 當 AI Agent 內建了點擊和自我修復能力，自動化工程師的核心產出應該變成什麼？
     - 如何設計一個「便於 AI 測試」的軟體架構？除了在 DOM 裡加 `data-testid` 外，我們是否應該在系統行為發生時發出隱藏的 `test-signals`？

### 其他長線題目（排隊中）

1. **PDT × 醫生問診類比**（補招牌主張深度，[analogy-series-proposals 主菜](analogy-series-proposals.md)）——等線六冷卻 + 招牌系列再延伸時動
2. **Bug Report 寫作教學**（補入門 / SEO 長尾——這是線八目前完全空白的位置）
3. **PDT Coach 工具實作後的反思文**（呼應 tools-first 策略——等工具用過 1-2 個月再寫）
4. **線十一（Mentorship 系列）首發**：〈我懂了我爸做水電時為什麼沒辦法邊教邊做〉（將生鮮觀察轉為 drafts 完稿）
5. **線十二（單兵 QA 自動化系列）首發**：〈單兵 QA 的第一個月：不要大張旗鼓，要「悄悄進行」的影子自動化〉
6. **PDT × QBT 雙層架構戰略**（**2026-06-01 新增**）：詳見 [pdt-vs-qbt-positioning.md](pdt-vs-qbt-positioning.md)。
7. **新孕育的 5 個文章角度**（從 [2026-05-28-insights.md](coach-sessions/2026-05-28-insights.md) 衍生）：
   - A.〈QBT：QA 是產品的責任編輯〉⭐⭐⭐⭐
   - B.〈接班不是接人格——讀懂組織的「實質本年結構」〉⭐⭐⭐
   - C.〈混合動機的承認——做 QA 為什麼不能 only one motive〉⭐⭐
   - D.〈個人化歸因是 QA 的職業病——強迫三解工具〉⭐⭐⭐
   - E.〈Coach 主動踩煞車——AI 助手該何時叫使用者離開？〉⭐⭐⭐⭐

主題線已從開台時的 4 條擴張到 12 條（見 [writing-themes.md](writing-themes.md)），結構性版圖已十分完整，接下來的重心在於穩健地產出每條線的代表作，並在發稿時落實主題線輪替，用專業管理/實踐線（線十一、線十二）來平衡過熱的線六。

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
| [uv + PyTorch + PyQt5 衝突](/post/uv-torch-pyqt5-dll-conflict/) | uv PyTorch PyQt5 DLL 衝突、WinError 1114 | ⭐⭐⭐⭐ |
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
| **bug-triage-six-patterns** | Bug Triage 業界六種模式、Bug 分派、QA bug 指派 | ⭐⭐⭐⭐ | ✅ **已生成並排程 2026-06-11**（前公司 F+E 第一手 + 業界 survey），見 [planning](bug-triage-six-patterns-planning.md) |
| **page-source-vs-find-element** | page_source vs find_element、UI 自動化效能 | ⭐⭐⭐⭐ | 已排 6/20，極具長尾 |
| **empty-result-ambiguity-in-filter-testing** | 篩選沒結果、自動化測試 empty | ⭐⭐⭐ | 已排 6/6 |
| **not-just-make-manual-script-automate** | 手動測試轉自動化、UI 自動化分工 | ⭐⭐⭐ | 6 月中後（已完成草稿） |
| **notest-ambiguity-skip-vs-low-confidence** | AI 測試 pass fail 不夠、notest 歧義 | ⭐⭐⭐ | 6 月中後 |
| **pom-refactor-from-runnable-to-maintainable** | POM 重構、Page Object Pattern | ⭐⭐⭐ | 暫不發布（作為個人技術與工程備忘） |
| **letter-to-new-qa-two-day-regression** | 新進 QA、兩天回歸測試 | ⭐⭐ | 5/24-25（已建議） |
| **ai-test-output-default-reader-is-ai** | AI 測試案例讀不懂、AI 預設讀者 | ⭐⭐ | 5/28-30（已建議） |
| **qa-report-workplace-wisdom** | 測試報告對牛彈琴、向上管理 | ⭐⭐ | 6 月 |
| **ai-replacement-accountability-checklist** | AI 取代 QA、當責清單 | ⭐⭐ | 6 月 |

## 從長尾力看「接下來該發什麼」

> 🕐 **2026-06-08 現況**：本段下方三篇 ⭐⭐⭐⭐ 候選中，frontend-ui（6/3）、page-source（6/6）已上稿，bug-triage 已降級為規劃檔。**接下來的真實排程以上方「📌 接下來節奏」表為準**，本段保留作歷史推理脈絡。

原本排程：letter-to-new-qa（5/24）→ ai-test-output（5/28-30）→ empty-result（6/6 排程）→ page-source（6/20 排程）

**但長尾力角度建議調整**——目前**最強的長尾候選**有三篇是「完稿即可、未排程」：
1. ⭐⭐⭐⭐ **bug-triage-six-patterns-industry-survey**
2. ⭐⭐⭐⭐ **frontend-ui-vocabulary-for-qa**（5/25 framing 校準完成）
3. ⭐⭐⭐⭐ page-source-vs-find-element（已排 6/20）

**新建議節奏（長尾優先版 + MoT 雙語規劃）**：

| 順序 | 日期 | 文章 | 長尾 | 主題線 | 備註 |
|---|---|---|---|---|---|
| 1 | 5/21 | letter-to-new-qa | ⭐⭐ | 線四（測試紀律） | ✅ **已上稿** |
| 2 | 6/3 | **frontend-ui-vocabulary-for-qa** ⭐ | ⭐⭐⭐⭐ | 線二 / 線八 | ✅ **已上稿** |
| 3 | 6/6 | **page-source-vs-find-element** | ⭐⭐⭐⭐ | 線三 | ✅ **已上稿** |
| 4 | 6/6 | **empty-result-ambiguity-in-filter-testing** | ⭐⭐⭐ | 線五 | ✅ **已上稿** |
| 5 | 6/7 | **ai-replacement-seminary-calling** | ⭐⭐ | 線七 | ✅ **已上稿** |
| 6 | 6/8 | **qa-report-workplace-wisdom** | ⭐⭐ | 線六 | ✅ **已上稿** |
| 7 | 6/11（排程） | **bug-triage-six-patterns** | ⭐⭐⭐⭐ | 線十 / 線八 | ✅ **已生成並排程**（前公司 F+E 第一手 + 業界 survey） |
| 8 | 6/14（排程） | **ai-test-output-default-reader** | ⭐⭐ | 線二 | ✅ **已生成並排程**（配對 yes-man，規劃檔為 [ai-test-output-default-reader-is-ai-planning.md](ai-test-output-default-reader-is-ai-planning.md)） |
| 9 | 6/11（排程） | **how-to-start-low-pressure-book-club** | — | 線十一 | ✅ **已生成並排程**（規劃檔為 [how-to-start-low-pressure-book-club-planning.md](how-to-start-low-pressure-book-club-planning.md)） |

> ⚠️ 線六提醒：qa-report（線六）已於 6/8 上稿——「未來 4-6 週避開線六」的時鐘從 6/8 起算，下一篇線六約等到 7 月中後。

**主要調動**：把兩篇 ⭐⭐⭐⭐ 的 SEO 強文（frontend-ui-vocabulary + bug-triage）排前面，ai-test-output 推到 6 月中。**6/20 之前累積 3 篇 ⭐⭐⭐⭐ + 1 篇英文 MoT 版，加速 Google 收錄 + 國際 backlink**。

**主要調動**：把兩篇 ⭐⭐⭐⭐ 的 SEO 強文（frontend-ui-vocabulary + bug-triage）排前面，ai-test-output 推到 6 月中——這樣 **6 月前累積到 3 篇 ⭐⭐⭐⭐ 長尾文，加速 Google 收錄**。

## MoT 論壇試水的英文翻譯選擇

⚠️ **時程（2026-06-08 定）**：六月不推廣。MoT 試水延到**報名 iThome 鐵人賽的當週**才啟動——報名動作本身就是「我準備好對外了」的觸發點，試水溫剛好搭著那股氣勢一起做。這仍是推廣節奏的躍進（從內部試水→國際社群），[blog_promotion_stance](C:\Users\user1\.claude\projects\c--Users-user1-Documents-GitHub-jiamingla-github-io\memory\blog_promotion_stance.md) memory 已同步此決定；真的要推之前再評估一次心理準備度。

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

### 翻譯次選（5/25 升級）：[frontend-ui-vocabulary-for-qa](frontend-ui-vocabulary-planning.md)

**5/25 framing 校準後升級為翻譯次選**——理由比 ai-as-yes-man 更強：

1. **31 個 UI 詞彙幾乎全是英文** ——translation friction 最低
2. **題目稀缺**——「frontend UI vocabulary for testers」這個 angle 英文圈也少見
3. **不依賴中文文化脈絡**——沒有「煩」「忠心」「我懂了我爸」這類翻不過去的東西
4. **長尾力 ⭐⭐⭐⭐**——SEO 雙語都強
5. **發稿規劃明確**：中文版 5/28-30 發、等 **1 週** 後（~6/5-7）做 adapted 英文版

**英文版的 adapt 重點**（不是純翻譯）：
- Framing 改成 **"A tester's lens on frontend UI patterns"**——強調 testing heuristics，不是 vocabulary lookup
- 開場 disarm senior readers：「You may already know some of these. The value isn't the definitions — it's the test heuristics in the third column.」
- 「最小生存集合」→ "starter kit" / "essentials"
- 「**PDT 的反向應用**」→ "**AI as a vocabulary mirror**" 或 "**reverse exploratory testing**"
- 自貶式句子 → "I had to look this up too"（humble but not self-deprecating）

→ 詳細 adapt 筆記見 [frontend-ui-vocabulary-planning.md](frontend-ui-vocabulary-planning.md) 頂部「MoT 英文版的差異化」段。

### 翻譯第三順位：[ai-as-yes-man-rd-pm-trust-calibration](/post/ai-as-yes-man-rd-pm-trust-calibration/)

1. **MoT 受眾近期火紅議題**：AI in testing
2. **觀點尖、辨識度高**——「AI 不是你的 QA，是你的 Yes Man」這種主張在英文圈也少見
3. 但**剛 5/20 發、還沒累積中文讀者數據**——讓中文版再跑 2-4 週看反應再決定

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
