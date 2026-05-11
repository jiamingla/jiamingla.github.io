# 寫作路線圖（Writing Roadmap）

**最後更新**：2026-05-11
**對應策略**：寫作目前以「累積、SEO 自然成長」為導向，不主動對外推廣。
**並進文件**：[tools-roadmap.md](tools-roadmap.md)（工具優先策略，文章是副產品）

> ⚠️ **每次發新文章後都要回來更新此檔**：把該篇從「完稿待上」移到「已上稿」表格，並更新主題線狀態。這個 roadmap 是 live 文件，stale 之後會比沒有更糟。

---

## 進度快照（2026-05-11）

### 推廣里程碑

- **2026-05-07：第一次對外分享**——把 [rethinking-regression-test-value](/post/rethinking-regression-test-value/) 貼給一位 QA 同事看（暫無具體回饋，但無負面反應）。詳見 memory: `blog_promotion_stance.md`

### 已上稿（12 篇，含排程；依日期倒序）

| 日期 | 文章 | URL slug | 主題線 |
|---|---|---|---|
| 2026-05-13 ⏰排程 | 測試站登入壞了那天：我真的測完了嗎？ | ten-minute-test-plan-when-test-stage-down | 突發應變 / 自我審視 / 信仰 |
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
| [ai-replacement-accountability-checklist](ai-replacement-accountability-checklist.md) | AI 取代 / 當責 | 完稿（2026-04-28） |
| [ai-replacement-seminary-calling](ai-replacement-seminary-calling.md) | AI 取代 / 信仰 | 完稿（2026-04-28） |
| [qa-report-workplace-wisdom](qa-report-workplace-wisdom.md) | 大人學 / 向上管理 | 完稿，已清公司指紋 |
| [letter-to-new-qa-two-day-regression](letter-to-new-qa-two-day-regression.md) | 新進 QA / 回歸方法論 | 完稿(20260511下一篇想這個方向) |
| [empty-result-ambiguity-in-filter-testing](empty-result-ambiguity-in-filter-testing.md) | 測試設計 / 篩選功能 | 完稿，**押 2026-06-06 發布** |
| [page-source-vs-find-element](page-source-vs-find-element.md) | 自動化效能 / Appium | 完稿，**押 2026-06-20 發布** |

### 草稿（已寫但尚未確認完稿）

| 文章 | 主題線 | 狀態備註 |
|---|---|---|
| [pom-refactor-from-runnable-to-maintainable](pom-refactor-from-runnable-to-maintainable.md) | 技術深度 / 教材潛力 | 草稿，等思考完才動 |

> 註：原 survival-kit-when-test-stage-down 在 5/11 重寫為 [ten-minute-test-plan-when-test-stage-down](/post/ten-minute-test-plan-when-test-stage-down/)，主軸從「Survival Kit 三件事」改為「ACC 自審覆蓋率」，已排程 5/13 上稿。

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
- [ ] 從 Self-review Agent 學到的事：我如何把 PDT 變成自動化提示（佔位符：先做工具，再產出這篇）

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
- [page-source-vs-find-element](page-source-vs-find-element.md)（押 2026-06-20，UI 自動化 cost model）

**規劃中/草稿**：
- [pom-refactor-from-runnable-to-maintainable](pom-refactor-from-runnable-to-maintainable.md)（草稿階段，教材潛力，可考慮給同事看）
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

## 線九：突發狀況 / 自我審視 / 工程紀律（2026-05-08 新加）

**起源**：2026-05-08 測試站登入服務壞掉、所有功能因相依登入無法測試。Jersey Su〈計畫趕得上變化〉與 James Whittaker 的 ACC 框架打開了一條新的寫作主軸。

**已排程上稿**：
- [ten-minute-test-plan-when-test-stage-down](/post/ten-minute-test-plan-when-test-stage-down/)（排程 2026-05-13）— 三層合流：ACC 自審覆蓋率 → 報告寫法的小聲音 → 忠心信仰收尾。原 Survival Kit 三件事框架在 5/11 重寫中被 ACC 工具線取代

**規劃中**：
- 工程化的「應變紀律」：how to plan for tools failing
- 「降級交付」的職場政治學：怎麼讓人理解 vs 怎麼讓人原諒
- Survival Kit 三件事（重寫前的原版被 ACC 取代，但仍是有效題材——可獨立成篇）

**狀態**：5/8 開出來，5/11 完成重寫並排程 5/13。線九首發已就位。

---

# 整體寫作節奏（2026-05-11 校準）

> 上次校準是 2026-05-08。這幾天的進展：線九首發 ten-minute-test-plan 5/11 重寫完成並排程 5/13、引入 ACC 框架、〈如何閱讀一本書〉跨領域類比加進 PDT 那篇、PDT 首篇加入 Bach / Kaner 兩句英文金句 + 延伸閱讀區塊。

## 庫存壓力（持續）

目前 **6 篇完稿草稿沒上**：
- 4 篇彈性發布：accountability-checklist、seminary-calling、qa-report-workplace-wisdom、letter-to-new-qa
- 2 篇排程發布：empty-result（6/6）、page-source（6/20）

寫作不缺東西，**缺的還是發稿節奏**。

## 接下來 1-2 週的建議發佈節奏

1. ~~survival-kit-when-test-stage-down~~ → **ten-minute-test-plan-when-test-stage-down** — ✅ **已排程 2026-05-13**
2. **letter-to-new-qa-two-day-regression** — 跟 ten-minute 是「兩天回歸 × 有限時間 × 覆蓋率焦慮」同一題的兩個面向（**內省版** / **教材版**）。**建議三到五天內接著發**，形成雙篇記憶點。目標發稿：2026-05-16 前後
3. **ai-replacement-accountability-checklist + seminary-calling** — AI 取代系列雙篇，連發效果好
4. **qa-report-workplace-wisdom** — 大人學 / 向上管理（注意：跟 ten-minute 結尾隱約撞「報告 vs 真實品質」，建議排在 #3 之後拉開距離）

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

# 2026 年中目標：iThome 鐵人賽（探索中）

> ℹ️ 關於鐵人賽的評估（包含機會成本、3個主題方向與 4 個月準備期排程等），因篇幅較長，已獨立至專屬規劃文件：
> 👉 [ithome-ironman-2026-planning.md](ithome-ironman-2026-planning.md)
