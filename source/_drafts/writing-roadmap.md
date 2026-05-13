# 寫作路線圖（Writing Roadmap）

**最後更新**：2026-05-13
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
- [pdt-coach-session-2026-05-12-insights.md](pdt-coach-session-2026-05-12-insights.md) — **PDT Coach 首次使用意外牽出的三條題目**（自我審查 / 跨團隊協作 / 金流無主之地）
- [pm-bug-management-structural-DRAWER.md](pm-bug-management-structural-DRAWER.md) — 🗄️ Framing B 抽屜文（暫不發表）
- [qa-self-review-agent-prompt-v1.md](qa-self-review-agent-prompt-v1.md) — PDT Coach v1 系統 prompt


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

**規劃中**：
- 🆕 **[ai-as-yes-man-rd-pm-trust-calibration](ai-as-yes-man-rd-pm-trust-calibration.md)** — 給 RD/PM 的 AI 測試結果信任校準（三個必問問題）。**主論點**：AI 不是你的 QA，是你的 Yes Man——QA 內建對你產品的敵意懷疑，AI 內建對你的對齊配合。**跟 [notest-ambiguity](notest-ambiguity-skip-vs-low-confidence.md) 是姐妹篇**：QA 升級 schema、RD/PM 升級提問習慣，[PDT Coach 工具](tools-roadmap.md) 填中間。**起源**：2026-05-13 跟 notest 那篇同源討論。**順序**：**先於 notest 上稿**（2026-05-13 訂）——awareness（這篇）→ tooling（notest）→ 配合 [accountability-checklist](ai-replacement-accountability-checklist.md) 形成「問題 → 責任 → 工具」三連發弧線

**狀態**：核心論述已打到位（spec / 煩 / 當責 / 呼召），四篇形成完整系列。**待上稿的兩篇可以排進接下來的節奏**。新加的 yes-man 篇把這條線從「QA 觀點的 AI 取代」推到「**RD/PM 觀點的 AI 信任**」——半徑更廣，也是 PDT Coach 工具對外推廣的合理性背書文。

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
- 🆕 **[notest-ambiguity-skip-vs-low-confidence](notest-ambiguity-skip-vs-low-confidence.md)** — AI 跑測試標 `notest`：跳過 vs 低信心 vs 執行失敗 vs 無判斷規則。**母題與 empty-result 同源**（「中間態被當成終態」），是它的姐妹篇。起源：2026-05-13 主管的提問。**讀者已確定**：QA，且預設只有 `pass/fail`（走 B 路線：公開＋去個人化，避免「應測但測不想」的自我揭露被同公司同事對號入座）。**觸發**：等 empty-result（6/6）上稿後再啟動。**配對作品**：[ai-as-yes-man-rd-pm-trust-calibration](ai-as-yes-man-rd-pm-trust-calibration.md) 是 RD/PM 視角的姐妹篇（見線二）——**先於本篇上稿**，本篇接著從 schema 層延伸
- 篩選功能的組合爆炸：Pairwise / 正交實驗設計入門
- PDT 視角下，篩選功能真正會壞掉的 7 個地方
- 自動化的 ROI 怎麼算？我用篩選功能算給你看

**狀態**：empty-result 上稿後這條線變得很厚——「該不該自動化」+「怎麼設計」都打到了。延伸題目都有素材，等情緒回流再寫。notest-ambiguity 是新加入的「同母題姐妹篇」，把這條線從「篩選功能特化」推廣到「AI 測試判讀」這層更抽象的命題。

---

## 線六：職涯 / 大人學 / 向上管理

**已上稿**：[QA 績效指標視角](/post/qa-performance-metrics-perspective/)

**完稿待上**：[qa-report-workplace-wisdom](qa-report-workplace-wisdom.md)（已清公司指紋）

**規劃中**：
- PM 要的不是測試報告，是決策依據
- 從需求會議抓出「沒說出口的驗收條件」
- 三種 PM 類型 × QA 協作策略（重交付 / 重數據 / 重用戶）
- 🆕 **〈我寫文章很犀利，講話會自我審查〉**（B 文，2026-05-12 從 PDT Coach session 浮現，可較早動筆）→ 詳見 [pdt-coach-session-2026-05-12-insights.md](pdt-coach-session-2026-05-12-insights.md)
- 🆕 **〈客服跑來敲門那天：30 分鐘串 4 個角色〉**（A 文，等案例累積 1-2 次再寫）→ 同上 insights 檔

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

## 線十：無主之地 / AI 補位 / Bug 治理（2026-05-11 新加，5/11 重新 framing）

**🔗 強連結**：[tools-roadmap.md](tools-roadmap.md)——這條線是「先工具、後文章」策略的具體落地。第二篇沒實作就不要寫。

**起源**：2026-05-11 對話中浮現的雙觀察——
1. JIRA 有幾千個 bug 被忽略，QA 也沒能力清完
2. PM 也不擅長管 bug

原本想寫成「鏡像對 / 結構分析」（Framing B），但同一天稍晚重新 framing 為**「正因為這是無主之地，AI 是天然的接手者」（Framing C）**——避開了對人的批評，且跟 tools-first strategy 完全合流。

**結構性洞察**：主管其實知道 backlog 沒在整理，但「不是部門績效」——這項工作落在組織縫隙裡，每個角色都有合理的不做理由（principal-agent problem）。**正因如此，AI 工具是補這個縫隙的最自然候選**。

**結構性洞察 #2（2026-05-13 補）**：bug backlog 不是 QA 累積物，是**四角色（客服 / RD / PM / QA）的輸入流混合語料**。每個 originator 用自己的語言寫 ticket——客服寫情緒體驗、RD 寫 stack trace、PM 寫影響範圍、QA 寫測試紀錄——**但很少有人類專家同時精通讀這四種語言**。資深 QA 通常只讀得懂 RD + 自己、資深 PM 只讀得懂客服 + 自己。

這個觀察讓 AI 的合理性論點**升級了一階**：

- ❌ 舊論點：「AI 比較快」——「快」會被追上，論點隨時可被新工具威脅
- ✅ 新論點：「**AI 對四種輸入語言都沒有 in-group bias**」——「跨角色語意中立」是 LLM 的結構優勢，不是速度問題

**對兩篇文章的影響**：
- 第一篇：「QA 是 default assignee 不是 originator」這個 reframe 讓論述更乾淨
- 第二篇：AI 是「**跨角色語意翻譯者**」這個定位，比「自動化 triage」強很多

詳見 [pdt-coach-session-2026-05-12-insights.md](pdt-coach-session-2026-05-12-insights.md) 末段「後續延伸觀察」。

**規劃中（現狀 + 解方，雙篇）**：

### 1. 〈我手上有 3,000 個 bug，但這不是我的績效〉
- QA 視角的隱形勞動 + 現狀觀察
- 主軸：自己面對 backlog 的真實處境 → 為什麼不主動清 → 為什麼這仍然是問題
- **第一人稱誠實面對，不指控 PM 主管**——把問題的存在當作後續工具的合理性論證
- 可較早寫，當第二篇的前傳

### 2. 〈AI 是「無主之地」的天然守門員：我怎麼做了一個 bug-triage agent 把績效縫隙補起來〉
- 跟 tools-roadmap 直接合流——可能是 PDT agent 的延伸應用，或一個獨立的 bug-triage agent
- 主軸：你做了什麼工具、解決了什麼、學到什麼
- PM 不擅長管 bug 這個觀察**藏在背景**，不正面寫
- **沒有實作就不要動筆**
- 🆕 **合寫候選素材**：金流測試的「四層卡點」是另一個「無主之地」具體案例——2026-05-12 PDT Coach session 浮現，詳見 [pdt-coach-session-2026-05-12-insights.md](pdt-coach-session-2026-05-12-insights.md) 文章 C。可以跟 bug-triage agent 案例合寫成「兩個無主之地」。

### 🗄️ 深度版（抽屜文，暫不發表）：[pm-bug-management-structural-DRAWER.md](pm-bug-management-structural-DRAWER.md)

5/11 對話中曾考慮 Framing B（PM 鏡像 / 結構分析）——這個版本論述更深、更勇敢，但對現任主管 / PM 風險高。最後決定**寫成抽屜文存著、不為發表**——免得寫作能量被時間沖淡。

該檔案內含：完整重啟條件、寫作骨架（六節）、紅線提醒、自由筆記區。

**重啟條件（任一成立可考慮潤色發表）**：
- 已離開現在公司一段時間
- 已升到能影響 KPI 設計的位置
- 已累積 2-3 篇結構分析文（讀者已建立「觀察者」印象）
- 跟現在主管 / PM 已無共事關係

**Framing 原則（精簡版）**：

- ✅ 把「無人管理」的事實當成 AI 工具的合理性論證，不當成對人的批評
- ✅ 加入「我也是共犯」的自我反思（不是只有別人不做）
- ✅ 引用既有概念當底氣：principal-agent problem

**延伸題目（暫存）**：
- 〈「緩衝工作」的職場政治學：為什麼最重要的事最沒人做〉
- 〈隱形勞動的可見化：QA 怎麼把 backlog 治理變成可被主管看見的成果〉

**狀態**：🔒 **想法成形、等工具實作**

**觸發條件**：
- **第一篇**：較彈性——內部試水累積 2-3 次成功後就可以動，預估 2026 Q3
- **第二篇**：硬性——等 bug-triage / PDT agent 出第一個能用的版本，**自己用過至少 4 週**，有實際使用故事再寫

Framing C 已經把這條線從「潛在威脅」翻轉成「潛在加分」——主管讀到反而會點頭（「對，這沒人管，你做工具補上」）。**原本的 promotion 顧慮 #3 不再是這條線的主要風險**。

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
