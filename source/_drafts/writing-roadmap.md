# 寫作路線圖（Writing Roadmap）

**最後更新**：2026-05-08
**對應策略**：寫作目前以「累積、SEO 自然成長」為導向，不主動對外推廣。
**並進文件**：[tools-roadmap.md](tools-roadmap.md)（工具優先策略，文章是副產品）

> ⚠️ **每次發新文章後都要回來更新此檔**：把該篇從「完稿待上」移到「已上稿」表格，並更新主題線狀態。這個 roadmap 是 live 文件，stale 之後會比沒有更糟。

---

## 進度快照（2026-05-08）

### 推廣里程碑

- **2026-05-07：第一次對外分享**——把 [rethinking-regression-test-value](/post/rethinking-regression-test-value/) 貼給一位 QA 同事看（暫無具體回饋，但無負面反應）。詳見 memory: `blog_promotion_stance.md`

### 已上稿（11 篇，依日期倒序）

| 日期 | 文章 | URL slug | 主題線 |
|---|---|---|---|
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

### 完稿草稿待上稿（7 篇）

| 文章 | 主題線 | 狀態備註 |
|---|---|---|
| [ai-replacement-accountability-checklist](ai-replacement-accountability-checklist.md) | AI 取代 / 當責 | 完稿（2026-04-28） |
| [ai-replacement-seminary-calling](ai-replacement-seminary-calling.md) | AI 取代 / 信仰 | 完稿（2026-04-28） |
| [qa-report-workplace-wisdom](qa-report-workplace-wisdom.md) | 大人學 / 向上管理 | 完稿，已清公司指紋 |
| [letter-to-new-qa-two-day-regression](letter-to-new-qa-two-day-regression.md) | 新進 QA / 回歸方法論 | 完稿 |
| [pom-refactor-from-runnable-to-maintainable](pom-refactor-from-runnable-to-maintainable.md) | 技術深度 / 教材潛力 | 草稿，等思考完才動 |
| [empty-result-ambiguity-in-filter-testing](empty-result-ambiguity-in-filter-testing.md) | 測試設計 / 篩選功能 | 完稿，**押 2026-06-06 發布** |
| [page-source-vs-find-element](page-source-vs-find-element.md) | 自動化效能 / Appium | 完稿，**押 2026-06-20 發布** |

### 草稿（已寫但尚未確認完稿，2026-05-08 加入）

| 文章 | 主題線 | 狀態備註 |
|---|---|---|
| [survival-kit-when-test-stage-down](survival-kit-when-test-stage-down.md) | 突發狀況 / QA 當責 / 信仰 | 草稿，敘事＋決策＋信仰三層合流（原 partial-report-and-responsibility 已合併進來） |

### 規劃文件（_drafts/，不會直接成為文章）

- [analogy-series-proposals.md](analogy-series-proposals.md) — PDT 類比系列（醫生 / 記者 / 偵探 / 讀者）
- [book-ideas-qa-growth-guide.md](book-ideas-qa-growth-guide.md) — 讀書延伸題目（《QA 職涯手冊》七個切角）
- [tools-roadmap.md](tools-roadmap.md) — PDT/Self-Review Agent 工具路線

### 已歸檔

- `archive/idea-2.md` — AI 取代系列原始素材（已被 accountability-checklist 與 seminary-calling 吸收）

---

# 主題線地圖

把現有文章 + 草稿 + 規劃題目按主題線整理。每條線都看得出累積到哪、缺什麼。

## 線一：PDT 招牌主張線

**已交付**：[problem-driven-testing-intro](/post/problem-driven-testing-intro/)（2026-04-24）

**規劃中**：
- PDT × 醫生問診類比（深度類比，主菜）
- PDT × 廣度類比（記者 / 偵探 / 讀者，4 種職業同構）
- 詳細提案見 [analogy-series-proposals.md](analogy-series-proposals.md)

**狀態**：招牌主張已立，類比系列是補強深度。**短期內最值得動**，因為這條線在部落格定位的權重最大。

---

## 線二：AI 取代 / 當責系列

**已上稿**：
- [spec-maintenance-gray-zone](/post/spec-maintenance-gray-zone/)（2026-05-03）
- [boredom-is-a-signal](/post/boredom-is-a-signal/)（2026-05-06，與 spec-maintenance 互為鏡像）

**完稿待上**：
- [ai-replacement-accountability-checklist](ai-replacement-accountability-checklist.md)（四份當責清單）
- [ai-replacement-seminary-calling](ai-replacement-seminary-calling.md)（信仰收尾）

**狀態**：核心論述已打到位（spec / 煩 / 當責 / 呼召），四篇形成完整系列。**待上稿的兩篇可以排進接下來的節奏**。

---

## 線三：技術實戰 / 自動化

**已上稿**：
- [Selenium 踩坑筆記](/post/selenium-troubleshooting/)
- [Appium v2 → v3 遷移](/post/appium-v2-to-v3-migration/)
- [語音測試 × FFmpeg](/post/audio-testing-ffmpeg/)

**完稿待上**：
- [pom-refactor-from-runnable-to-maintainable](pom-refactor-from-runnable-to-maintainable.md)（教材潛力，可考慮給同事看）
- [page-source-vs-find-element](page-source-vs-find-element.md)（押 2026-06-20，UI 自動化 cost model）

**規劃中**：
- Claude Code + MCP 寫 Android 自動化測試（Python）
- 語音測試之二：延遲、回聲、背景噪音的自動化驗證

**狀態**：基礎已建立 + 兩篇深度文（POM 設計、page_source 效能）即將上線。POM + page_source 上稿後會把「PDT 高層次主張 → 工程實踐」的橋接補完。

---

## 線四：測試紀律 / 方法論

**已上稿**：
- [黑箱測試的限制與策略](/post/black-box-limitations-and-strategy/)
- [太多「無意義」的回歸測試嗎？](/post/rethinking-regression-test-value/)
- [PDT](/post/problem-driven-testing-intro/)

**完稿待上**：[letter-to-new-qa-two-day-regression](letter-to-new-qa-two-day-regression.md)（新進 QA 信，兩天回歸方法論）

**規劃中**：
- 回歸測試的精簡 SOP（接 rethinking-regression-test-value）
- 灰箱測試的入門路徑（接 black-box-limitations-and-strategy）
- Bug Report 寫作教學：初階 QA 最常被退件的原因

**狀態**：這是部落格最厚的一條線。Bug Report 寫作教學 SEO 長尾值得早寫。

---

## 線五：自動化決策 / 測試設計

**已上稿**：[boredom-is-a-signal](/post/boredom-is-a-signal/)（與 spec-maintenance 鏡像對）

**完稿待上**：[empty-result-ambiguity-in-filter-testing](empty-result-ambiguity-in-filter-testing.md)（押 2026-06-06，篩選 empty 歧義五種解法）

**規劃中**：
- 篩選功能的組合爆炸：Pairwise / 正交實驗設計入門
- PDT 視角下，篩選功能真正會壞掉的 7 個地方
- 自動化的 ROI 怎麼算？我用篩選功能算給你看

**狀態**：empty-result 上稿後這條線變得很厚——「該不該自動化」+「怎麼設計」都打到了。延伸題目都有素材，等情緒回流再寫。

---

## 線六：職涯 / 大人學 / 向上管理

**已上稿**：[QA 績效指標視角](/post/qa-performance-metrics-perspective/)

**完稿待上**：[qa-report-workplace-wisdom](qa-report-workplace-wisdom.md)（已清公司指紋）

**規劃中**：
- PM 要的不是測試報告，是決策依據
- 從需求會議抓出「沒說出口的驗收條件」
- 三種 PM 類型 × QA 協作策略（重交付 / 重數據 / 重用戶）

---

## 線七：信仰 / 基督徒工作觀

**已上稿**：boredom-is-a-signal 結尾的禱告（小型）

**完稿待上**：[ai-replacement-seminary-calling](ai-replacement-seminary-calling.md)（信仰深寫）

**規劃中**：
- 基督徒的測試視角：挑錯這份工作的召命與價值（深度版）

**狀態**：差異化品牌的核心。**不宜連發**，與其他線輪流上稿。

---

## 線八：入門 / 長尾 SEO

**規劃中**：
- Bug Report 寫作教學（流量穩、長尾高）
- 測試工程師養成書單／學習路徑（合流到 [book-ideas-qa-growth-guide.md](book-ideas-qa-growth-guide.md)）

**狀態**：品牌目前缺，**短期內加一篇 Bug Report 教學會讓部落格定位更完整**。

---

## 線九：突發狀況 / Survival Kit / 工程紀律（新加，2026-05-08）

**起源**：2026-05-08 測試站登入服務壞掉、所有功能因相依登入無法測試。Jersey Su〈計畫趕得上變化〉的 Survival Kit 比喻打開了一條新的寫作主軸。

**草稿（待自己審）**：
- [survival-kit-when-test-stage-down](survival-kit-when-test-stage-down.md) — 三層合流：Survival Kit 三件事 → 報告寫法的小聲音 → 「忠心」信仰收尾（原 partial-report 已合併進此篇）

**規劃中**：
- 工程化的「應變紀律」：how to plan for tools failing
- 「降級交付」的職場政治學：怎麼讓人理解 vs 怎麼讓人原諒

**狀態**：5/8 一個工作日生出一篇厚度足夠的合流草稿（~1500 字）。**這條線首發已就緒，等審完就可以排上稿節奏**。

---

# 整體寫作節奏（2026-05-08 校準）

> 上次校準是 2026-05-06。這幾天的進展：boredom 已上稿、empty-result + page-source 兩篇技術深度文寫好排程、線九（Survival Kit）開出來。

## 庫存壓力（仍存在）

目前 **7 篇完稿草稿沒上**：
- 5 篇彈性發布：accountability-checklist、seminary-calling、qa-report-workplace-wisdom、letter-to-new-qa、pom-refactor
- 2 篇排程發布：empty-result（6/6）、page-source（6/20）

寫作不缺東西，**缺的還是發稿節奏**。

## 接下來 1-2 週的建議節奏

每 3-5 天上一篇，把彈性庫存清完：

1. **letter-to-new-qa-two-day-regression** — 新進 QA 教材，溫度高
2. **pom-refactor**（思考完之後）— 技術深度，可介紹給同事
3. **ai-replacement-accountability-checklist + seminary-calling** — AI 取代系列雙篇，連發效果好
4. **qa-report-workplace-wisdom** — 大人學 / 向上管理

## 下一篇要新寫的

**〈測試機掛了那天：QA 的 Survival Kit〉**（線九主菜）

理由：
- 情緒新鮮（今天剛發生）
- 主題線完全空白，新內容會打開部落格的新切面
- 跟既有的當責 / PDT / 不和諧感主題連結度高
- Jersey Su 的 Medium 文剛好提供類比的 reference point

## 接下來 1 個月的寫作目標

庫存清完後動的新題目：

1. **PDT × 醫生問診類比**（補招牌主張深度，[analogy-series-proposals 主菜](analogy-series-proposals.md)）
2. **Bug Report 寫作教學**（補入門 / SEO 長尾，品牌缺）

寫完這兩篇 + Survival Kit，部落格從「招牌＋零散技術文」推進到「招牌 × 技術 × 入門 × 信仰 × 職涯 × 突發應變」**七線並進**。

## 與工具路線的分工

從 2026-05-04 起採取「先工具、後文章」策略（見 [tools-roadmap.md](tools-roadmap.md)）：

- **寫作**：思想沉澱、長期 SEO、未來職涯資本
- **工具**：日常工作生產力、可被同事 / 主管看見的具體產出

兩條線會在某些題目交會。例如做完 self-review agent 用一個月後，可以寫一篇「我把 PDT 變成工具學到的事」——**先工具、後文章**會比硬擠出來的方法論文章紮實。

POM 那篇也可以走類似路線：文章先發、之後可能變成內部 workshop / 同事 onboarding 教材。

---

# 2026 年中目標：iThome 鐵人賽（探索中，2026-05-06 加入）

## 為什麼現在要思考這件事

鐵人賽是 30 天連續發文的公開承諾，每年 9 月開賽、7-8 月開放報名。對目前狀態的我來說，它有獨特的意義——不只是「對外曝光」，更是**一份時間投資能解決兩件事**：對外可見的職涯資產 + 對內可用的工作工具（如果方向選對）。

但它也是一個會打破目前所有節奏的決定，需要在報名前認真想清楚。

## 策略意義（機會 vs. 成本）

**機會面**：
- 30 天連載是公開承諾，逼出產量與紀律——比自己慢慢寫更銳利
- 鐵人賽的「比賽身分」會中和推廣焦慮：不是自我行銷，是參賽
- 完賽本身就是職涯資產（履歷、面試話題），**它是一份主管可見、不必主動推就會被看見的證據**
- 對「沒做出明顯文化推動」的自評，鐵人賽是看得見的紀律標的

**真實成本**：
- 30 天連續發文，每篇 1000-2500 字（目前水準），等於上班同時每天擠 1-2 小時
- 直接擠壓 [tools-roadmap.md](tools-roadmap.md) 的 self-review agent 進度
- 鐵人賽的速度不可能維持目前品質——一定會降一檔
- 跟「不主動推廣」立場衝突，但比一般推廣更能找到舒服的姿態

## 三個主題方向

### 方向 A：PDT 三十日——從方法論到日常戰術
30 天全寫 PDT 不同切面：定義、類比（醫生／記者／偵探／讀者）、PDT 在需求訪談、PDT 在回歸、PDT × AI、PDT × 信仰收尾。

- **優勢**：招牌主張集中強化，30 篇下來等於把 PDT 寫成一本書（呼應 [book-ideas-qa-growth-guide.md](book-ideas-qa-growth-guide.md)）
- **風險**：題目單一，第 18-22 天容易進入撞牆期

### 方向 B：給新進 QA 的 30 課
每天一個 lesson — Bug report、回歸方法、自動化判斷、向上管理、不和諧感、PDT 入門⋯⋯

- **優勢**：教材姿態降低 imposter syndrome；組合既有素材容易；可介紹給同事
- **風險**：少了招牌主張穿透力，比較像 QA 入門大全

### 方向 C：把 PDT 變成工具——一個 QA 的 30 天工具化日誌（**目前傾向**）
邊做 self-review agent 邊寫——Day 1-7 概念與 prompt 設計、Day 8-14 第一版實作、Day 15-21 真實工作測試與迭代、Day 22-28 放大成 PDT Agent、Day 29-30 反思。

**為什麼推**：
- **強迫**把 [tools-roadmap.md](tools-roadmap.md) 從計畫變現實——這條策略最大的風險就是拖
- 鐵人賽 30 天交付 ≈ self-review agent 的 MVP 時程
- 寫日誌不是寫教學，內容每天有真實進度，不會撞牆
- 主管可見度問題**翻轉成優勢**：他不是看到我寫部落格，是看到我**在做工具**——工具是他語言裡的「在做事」
- 完賽當天手上有兩樣東西：能用的 self-review agent + 30 篇紀錄。**這份組合對職涯的重量遠大於 30 篇純方法論**

## 4 個月準備期排程（2026-05 至 2026-08）

| 期間 | 動作 |
|---|---|
| 5-7 月 | 把現有完稿庫存全部上稿（清掉壓力，騰出 8 月專注準備） |
| 6 月起 | 開始建 self-review agent（如果走方向 C）——9 月開賽時不是從零開始，是記錄一個已跑三個月工具的優化過程 |
| 8 月 | 排 30 天 outline，**至少預寫 5-7 篇 buffer**（家庭事 / 病假時不致斷賽） |
| 8 月底 | 心理體檢：還有沒有想做？是不是被「應該要做」綁架？ |

---

## 釐清「是否準備好」——給自己的問題清單

報名前要誠實回答自己的問題（沒有對錯，但有需要釐清）：

### 1. 對外發表的試水
過去從沒在測試社群外公開推廣，從 0 直接跳到 30 天連載是大躍進。**先做一次小規模試水可能比直接報名更扎實**——例如：在 6-7 月把一篇現有文章丟到 MoT 論壇或 Medium，看看能不能承受不熟悉的回饋（或 0 回饋）。試水的結果會告訴你 30 天連載扛不扛得住。

> 進度：2026-05-07 已做第一次「同事級」試水（貼給 QA 同事看）。下一階段可考慮匿名／國外圈。

### 2. 主管可見度的盤點
- 主管會不會在 9 月看到你連續 30 天發技術文？大概率會（鐵人賽在台灣 QA 圈太顯眼）
- 如果他看到，反應會是「這個人有在學」還是「上班時間在做這個？」
- 如果不確定，**現在主動跟他打個招呼**（「我考慮 9 月參加鐵人賽，下班時間寫」）會比讓他自己發現好十倍
- 這個對話本身也是測試器：他的反應會告訴你你跟主管的信任在哪一檔

### 3. 時程現實感
- 你現在 5-7 天一篇是因為你寫得認真。鐵人賽是每天一篇——同樣的標準守不住
- 你能接受文章品質掉一檔嗎？對品牌會不會有反噬？（鐵人賽讀者其實比較吃「有沒有持續」而不是每篇深度）
- 9 月有沒有家庭事、健康風險、工作大型上線可能跟賽期撞？

### 4. 工具路徑的承諾（如果走方向 C）
等於是把 self-review agent 從「想做」綁定成「9 月一定要有 MVP」。**現在能不能對這個承諾說 yes？** 如果還沒準備好對工具負責，方向 A 或 B 比較適合。

### 5. 心理底線
**最重要的問題**：如果你做了 14 天就斷賽，你會怎麼看自己？
- 如果答案是「沒關係，我學到一些東西」——可以報
- 如果答案是「我會否定自己之前所有的累積」——**現在還不是時候，先把心理基礎建起來再說**

---

## 不報的退路也是一條路

無論最後報不報，都不影響：

- **持續寫作這件事本身**（你已經證明會寫，2026-01 至 2026-05 累積 11 篇上稿 + 7 篇完稿待上）
- **tools-roadmap.md 的 self-review agent**（這件事獨立進行）
- **部落格的長期累積跟 SEO**（時間複利會替你做事）

鐵人賽是**加速器**，不是必經之路。如果今年發現條件不到位，明年再說也是合理的選擇——你不會因為晚一年而失去什麼，反而可能用那一年累積出更好的內容跟更穩的心理基礎。

> **選擇報**，是用一段密集投資換一份具體可見的職涯資產。
> **選擇不報**，是用持續累積換更穩的長期路徑。
> 兩條路都不是逃避，看哪條更貼合此刻的你。
