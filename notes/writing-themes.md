# 寫作主題線地圖（Writing Themes Map）

**最後更新**：2026-06-01（13 條主題線，6/1 新加線十三：書評 / 跟測試學派對話）
**並進文件**：
- [writing-roadmap.md](writing-roadmap.md) — 進度快照、寫作節奏、發稿順序（操作型，常看）
- [tools-roadmap.md](tools-roadmap.md) — 工具優先策略

> 這份檔案是**長期主題版圖**——10 條主題線各自累積到哪、缺什麼。比 roadmap 較少更新，主要在「新題目該歸到哪條線、這條線該不該加題、整體版圖均衡嗎」這類**策略性問題**浮現時來查。
>
> 日常操作問題（這週發什麼、下篇排誰、誰跟誰之間要間隔幾天）請看 [writing-roadmap.md](writing-roadmap.md)。

---

把現有文章 + 草稿 + 規劃題目按主題線整理。每條線都看得出累積到哪、缺什麼。

## 線一：PDT 招牌主張線

**已交付**：[problem-driven-testing-intro](/post/problem-driven-testing-intro/)（2026-04-24）

**規劃中**：
- PDT × 醫生問診類比（深度類比，主菜）
- PDT × 廣度類比（記者 / 偵探 / 讀者，4 種職業同構）
- 詳細提案見 [analogy-series-proposals.md](analogy-series-proposals.md)
- [ ] 從 Self-review Agent 學到的事：我如何把 PDT 變成自動化提示（佔位符：先做工具，再產出這篇）
- 🆕 **〈AI Coach 沒給安慰：當你需要的不是被理解，是被點破〉**（5/14 D 文，PDT 哲學延伸）→ [insights](coach-sessions/2026-05-14-insights.md)
- 🆕 **〈跨對話的記憶才是 AI 助理的真正價值〉**（5/14 E 文，跟 tools-roadmap 合流）→ 同上
- 🆕 **〈彌補設計與體驗的斷層：QA 的「負熵」任務〉**（5/31 C 文）。核心：QA 應主動填補架構設計與終端使用者體驗之間的品質落差。
- 🆕 ⭐⭐ **〈B 堆是流量不是存量：QA 是 AI 流水線的上游活水〉**（5/21 A 文）。**核心**：AI 文件查不到、靠經驗才追得到的 bug 不會被補完，是**持續產生的流量**——QA 是上游活水不是執行末梢。**跨線**：也呼應線二 AI literacy。**可發性極高**（純論述、無人事指紋），等 prototype 動工後素材會更紮實 → [5/21 insights](coach-sessions/2026-05-21-insights.md)

**狀態**：招牌主張已立，類比系列是補強深度。**短期內最值得動**，因為這條線在部落格定位的權重最大。**新加 5/21 A 文是這條線往「AI 時代 QA 定位」的重要拓展**。

---

## 線二：AI 取代 / 當責系列

**已上稿**：
- [spec-maintenance-gray-zone](/post/spec-maintenance-gray-zone/)（2026-05-03）
- [boredom-is-a-signal](/post/boredom-is-a-signal/)（2026-05-06，與 spec-maintenance 互為鏡像）
- [frontend-ui-vocabulary-for-qa](/post/frontend-ui-vocabulary-for-qa/)（2026-06-03，與線八交叉）
- [ai-replacement-seminary-calling](/post/ai-replacement-seminary-calling/)（2026-06-07，信仰收尾，與線七交叉）

**完稿待上**：
- [ai-replacement-accountability-checklist](../source/_drafts/ai-replacement-accountability-checklist.md)（四份當責清單，暫緩發布待改寫）

**規劃中**：
- 🆕 **[ai-as-yes-man-rd-pm-trust-calibration](../source/_drafts/ai-as-yes-man-rd-pm-trust-calibration.md)** — 給 RD/PM 的 AI 測試結果信任校準（三個必問問題）。**主論點**：AI 不是你的 QA，是你的 Yes Man——QA 內建對你產品的敵意懷疑，AI 內建對你的對齊配合。**跟 [notest-ambiguity](../source/_drafts/notest-ambiguity-skip-vs-low-confidence.md) 是姐妹篇**：QA 升級 schema、RD/PM 升級提問習慣，[PDT Coach 工具](tools-roadmap.md) 填中間。**起源**：2026-05-13 跟 notest 那篇同源討論。**順序**：**先於 notest 上稿**（2026-05-13 訂）——awareness（這篇）→ tooling（notest）→ 配合 [accountability-checklist](../source/_drafts/ai-replacement-accountability-checklist.md) 形成「問題 → 責任 → 工具」三連發弧線。**配對篇**：跟 [ai-test-output-default-reader-is-ai](../source/_drafts/ai-test-output-default-reader-is-ai.md) 形成「**Working with AI Output**」雙篇——本篇講「問」、配對篇講「讀」
- 🆕 **[ai-test-output-default-reader-is-ai](../source/_drafts/ai-test-output-default-reader-is-ai.md)** — 為什麼 AI 給的測試案例讀起來特別累？因為它的預設讀者不是你。三層 mismatch（專業 / 語言 / 基礎假設）+ 四個讀 AI 輸出的具體技巧（為自己 prompt design / 詞彙考試 / 翻譯 / glossary）。**起源**：2026-05-14 寫 [frontend-ui-vocabulary](../source/_drafts/frontend-ui-vocabulary-for-backend-qa.md) 篇時衍生出來的更大命題。**讀者**：中文圈 QA + 單一專業背景——這是**繁體中文 QA 部落格的 differentiator**（英文圈不討論這個 angle）。**配對**：跟 [yes-man](../source/_drafts/ai-as-yes-man-rd-pm-trust-calibration.md) 形成「**Working with AI Output 雙篇**」（會問 + 會讀）

**狀態**：核心論述已打到位（spec / 煩 / 當責 / 呼召），四篇形成完整系列。**待上稿的兩篇可以排進接下來的節奏**。新加的 yes-man + ai-test-output-default-reader 形成「**Working with AI Output**」雙篇（會問 + 會讀），讓這條線從「**AI 取代焦慮**」往「**AI literacy 操作技能**」進化——半徑更廣、actionable 更強，也都是 PDT Coach 工具對外推廣的合理性背書文。

---

## 線三：技術實戰 / 自動化

**已上稿**：
- [Selenium 踩坑筆記](/post/selenium-troubleshooting/)
- [Appium v2 → v3 遷移](/post/appium-v2-to-v3-migration/)
- [語音測試 × FFmpeg](/post/audio-testing-ffmpeg/)
- [page-source-vs-find-element](/post/page-source-vs-find-element/)（2026-06-06，UI 自動化 cost model）

**完稿待上**：
- 暫無

**規劃中/草稿**：
- 🆕 **[not-just-make-manual-script-automate](../source/_drafts/not-just-make-manual-script-automate.md)** — 〈你從不知道，我想做的不只是將手動測試給自動化〉。**主論點**：手動測試案例直接翻譯成自動化腳本是業界最常見的浪費——兩者本質上是不同物種，該分工而非轉換。手動專責探索 + UX 判斷 + 關鍵 path；自動化專責 API / DB / 結構性資料一致性。**起源**：2026-05-15 對話。骨架已建（前言 + 五節 + 結語）、4 個反思問題嵌入待答。**形成 UI 自動化子三部曲**：[boredom-is-a-signal](/post/boredom-is-a-signal/)（該不該自動化）→ 本篇（該驗什麼）→ page-source-vs-find-element（怎麼驗有效率）
- [pom-refactor-from-runnable-to-maintainable](../source/_drafts/pom-refactor-from-runnable-to-maintainable.md)（草稿階段，教材潛力，可考慮給同事看）
- 🆕 ⭐⭐ **〈一份測試 lib 服務 20 個 APP——元素定位的漸進式抽象策略〉**（5/28 從工作觀察整理）。**主論點**：跨產品線共用測試 lib 的元素定位設計——漸進式三階段（fallback chain → LocatorStrategy → per-APP class），「重複 3 次才抽象」「抽通用 pattern 不抽 APP」。**起源**：2026-05-28 cross-app-locator-strategy 工程備忘。**含公司指紋需洗**，但長尾力極強。**跟 pom-refactor 形成「POM 雙篇」**：pom-refactor 處理 single APP「能跑→可維護」、本篇處理「single APP → multi APP」規模化。詳見 [cross-app-locator-strategy.md](cross-app-locator-strategy.md)
- Claude Code + MCP 寫 Android 自動化測試（Python）
- 語音測試之二：延遲、回聲、背景噪音的自動化驗證

**狀態**：基礎已建立 + 兩篇深度文（POM 設計、page_source 效能）即將上線。POM + page_source 上稿後會把「PDT 高層次主張 → 工程實踐」的橋接補完。**新增 not-just-make-manual-script-automate（骨架已建）會跟 boredom + page-source 形成「UI 自動化三部曲」**。**5/28 新加 cross-app-locator-strategy 跟 pom-refactor 形成「POM 雙篇」**——子線（UI 自動化設計）累積深度大幅提升。

---

## 線四：測試紀律 / 方法論

**已上稿**：
- [黑箱測試的限制與策略](/post/black-box-limitations-and-strategy/)
- [太多「無意義」的回歸測試嗎？](/post/rethinking-regression-test-value/)
- [PDT](/post/problem-driven-testing-intro/)
- [letter-to-new-qa-two-day-regression](/post/letter-to-new-qa-two-day-regression/)（2026-05-22，跨線十一）

**規劃中**：
- 回歸測試的精簡 SOP（接 rethinking-regression-test-value）
- 灰箱測試的入門路徑（接 black-box-limitations-and-strategy）
- Bug Report 寫作教學：初階 QA 最常被退件的原因
- 🆕 **〈「首次下載」這三個字其實有三種意思〉**（5/13 B 文，純技術 / 零風險，可立刻動筆）→ [insights](coach-sessions/2026-05-13-insights.md)

**狀態**：這是部落格最厚的一條線。Bug Report 寫作教學 SEO 長尾值得早寫。**5/13 B 文是這條線目前最容易動筆的——零風險、有技術深度、跟 PDT 提問精準度同源**。

---

## 線五：自動化決策 / 測試設計

**已上稿**：
- [boredom-is-a-signal](/post/boredom-is-a-signal/)（與 spec-maintenance 鏡像對）
- [empty-result-ambiguity-in-filter-testing](/post/empty-result-ambiguity-in-filter-testing/)（2026-06-06，篩選 empty 歧義五種解法）

**規劃中**：
- 🆕 **[notest-ambiguity-skip-vs-low-confidence](../source/_drafts/notest-ambiguity-skip-vs-low-confidence.md)** — AI 跑測試標 `notest`：跳過 vs 低信心 vs 執行失敗 vs 無判斷規則。**母題與 empty-result 同源**（「中間態被當成終態」），是它的姐妹篇。起源：2026-05-13 主管的提問。**讀者已確定**：QA，且預設只有 `pass/fail`（走 B 路線：公開＋去個人化，避免「應測但測不想」的自我揭露被同公司同事對號入座）。**觸發**：等 empty-result（6/6）上稿後再啟動。**配對作品**：[ai-as-yes-man-rd-pm-trust-calibration](../source/_drafts/ai-as-yes-man-rd-pm-trust-calibration.md) 是 RD/PM 視角的姐妹篇（見線二）——**先於本篇上稿**，本篇接著從 schema 層延伸
- 篩選功能的組合爆炸：Pairwise / 正交實驗設計入門
- PDT 視角下，篩選功能真正會壞掉的 7 個地方
- 自動化的 ROI 怎麼算？我用篩選功能算給你看
- 🔗 **[not-just-make-manual-script-automate](../source/_drafts/not-just-make-manual-script-automate.md)**（主要落線三，但跨線五——「該自動化什麼」這題的具體解，呼應 boredom-is-a-signal 從「該不該」進一步到「該驗什麼」）

**狀態**：empty-result 上稿後這條線變得很厚——「該不該自動化」+「怎麼設計」都打到了。延伸題目都有素材，等情緒回流再寫。notest-ambiguity 是新加入的「同母題姐妹篇」，把這條線從「篩選功能特化」推廣到「AI 測試判讀」這層更抽象的命題。

---

## 線六：職涯 / 大人學 / 向上管理

**已上稿**：
- [QA 績效指標視角](/post/qa-performance-metrics-perspective/)
- [qa-report-workplace-wisdom](/post/qa-report-workplace-wisdom/)（2026-06-08，已清公司指紋）

**完稿待上**：
- 暫無

**規劃中**：
- PM 要的不是測試報告，是決策依據
- 從需求會議抓出「沒說出口的驗收條件」
- 三種 PM 類型 × QA 協作策略（重交付 / 重數據 / 重用戶）
- 🆕 **〈我寫文章很犀利，講話會自我審查〉**（5/12 B 文，可較早動筆）→ [5/12 insights](coach-sessions/2026-05-12-insights.md)
- 🆕 **〈客服跑來敲門那天：30 分鐘串 4 個角色〉**（5/12 A 文，等案例累積 1-2 次再寫）
- 🆕 **〈「該做」與「想做」之間，QA 容易把自己騙過去〉**（5/13 A 文，跟 5/12 B 文可合寫成系列）→ [5/13 insights](coach-sessions/2026-05-13-insights.md)
- 🆕 **〈訪談非測試導向的 PM：問事實不問需求〉**（5/13 C 文，等案例累積）
- 🆕 ⭐ **〈「不是退讓，是調整佔用」〉**（5/14 A 文，三天故事收尾，等 3 週後檢查點過了再寫）→ [5/14 insights](coach-sessions/2026-05-14-insights.md)
- 🆕 **〈中午被否定三次後：「方案不好」vs「你不在那個位置上」〉**（5/14 B 文，需洗指紋）
- 🆕 **〈被動承接員 vs 主動承接員 vs Owner 敘事〉**（5/14 C 文，等 6-8 週累積實際嘗試經驗）
- 🆕 ⭐ **〈會議後的失落感，是 senior 的成本還是失敗？〉**（5/20 F 文，純個人反思、無人事指紋、可較早動筆，跟下一篇可合寫成情緒覺察雙篇）→ [5/20 insights](coach-sessions/2026-05-20-insights.md)
- 🆕 **〈「自我打折」的習慣：用時間打折、錯誤打折、判斷力打折換對方舒適〉**（5/20 D 文，跟 F 文可形成 mini 系列，無風險）
- 🆕 **〈90/10 節奏：純默默累積會崩潰、純爭取會被擠壓——中間的呼吸法〉**（5/20 A 文，要 4-6 週實踐後再寫）
- 🆕 **〈八個月醞釀的爆發：為什麼第一二個月失敗的提案，第八個月可以成功〉**（5/20 B 文，等 800 case 提案最終結果再寫，需洗 case 數字指紋）
- 🆕 **〈大人學三選項框架的應用：我怎麼把『砍一半測試案例』分成 ABC 三條路〉**（5/20 C 文，同 B 等結果）
- 🆕 **〈Facilitator 角色：當你不是會議主角，會議反而走得更遠〉**（5/20 E 文，要累積 2-3 個案例）
- 🆕 ⭐ **〈昨天會議我輸的不是表達，是地基〉**（5/21 B 文，無人事指紋、純方法論、可較早動筆）。**核心**：把猜測當事實講被抓——自檢動作「主管反問『你怎麼知道』我答得出來源嗎？」→ [5/21 insights](coach-sessions/2026-05-21-insights.md)
- 🆕 **〈借用主管框架推自己的事〉**（5/21 D 文，等 G 動作累積 4-5 筆案例）。**核心**：把 Lead 在會議上認可的「規劃 vs 執行可以分開」用在他沒講的地方
- 🆕 **〈prototype 的權力學：當「貢獻者」不搶「設計者」椅子〉**（5/21 C 文，等 prototype 真做出來 + 洗指紋）
- 🆕 ⭐ **〈品牌價值的真實體現：在異常發生時，誰接住了狀況？〉**（5/31 A 文）。**核心**：真正的價值不在於順利交付，而在於系統發生異常時的應變與防禦。
- 🗄️ **〈馬拉松配速：看別人超車忍不住跟，才是會崩的點〉**（5/21 E 文，**抽屜文**，自省題密度過載先存著）
- 🗄️ **〈我把「想要」偽裝成「怕失去」三個月了〉**（5/21 F 文，**深抽屜**，需要 6-12 個月時間消化）

> **線六近期密度警示（5/21 更新）**：PDT Coach 五場 session 累計孕育 **19 個**自省 / 大人學題目（5/12-5/21）。**這條線嚴重過熱、且自省深度持續加深**——寫的時候務必分散到其他線、不要連發，否則部落格會給人「自省過載 / 心靈雞湯」的觀感。建議跟線一（PDT 哲學）、線四（方法論）、線三（技術實戰）輪流發；**同時間發兩篇線六的話兩篇至少要相隔 3-4 週**。
>
> 此警示的具體輪替紀律 + 4-6 週發稿順序，見 [writing-roadmap.md](writing-roadmap.md) 「整體寫作節奏」段。

---

## 線七：信仰 / 基督徒工作觀

**已上稿**：
- boredom-is-a-signal 結尾的禱告（小型）
- [ai-replacement-seminary-calling](/post/ai-replacement-seminary-calling/)（2026-06-07，信仰深寫）

**完稿待上**：
- 暫無

**規劃中**：
- 基督徒的測試視角：挑錯這份工作的召命與價值（深度版）

**狀態**：差異化品牌的核心。**不宜連發**，與其他線輪流上稿。

---

## 線八：入門 / 長尾 SEO

**已交付**：
- [frontend-ui-vocabulary-for-qa](/post/frontend-ui-vocabulary-for-qa/)（2026-06-03，與線二交叉）

**規劃中**：
- Bug Report 寫作教學（流量穩、長尾高）
- 測試工程師養成書單／學習路徑（合流到 [book-ideas-qa-growth-guide.md](book-ideas-qa-growth-guide.md)）
- 🆕 **[bug-triage-six-patterns-industry-survey](../source/_drafts/bug-triage-six-patterns-industry-survey.md)** — 業界 Bug 預設指派的六種 pattern 對照（PM / Tech Lead / QA / Unassigned / Committee / CODEOWNER）+ 七種 backlog workaround（bug bash / bankruptcy / Zero bug / Severity-only / Fix-it Friday / SLA-based / Embedded QA）。**起源**：2026-05-13 為線十做業界 survey 時發現本身就值得獨立成篇。**讀者**：QA 為主，PM / Tech Lead 也讀得進去。**SEO**：「bug triage」是穩定長尾關鍵字。**配對**：是線十兩篇的入門前傳，**發稿順序未定**（先入門引流 / 後深度延伸都可）

**狀態**：品牌目前缺，**短期內加一篇 Bug Report 教學會讓部落格定位更完整**。線八現有四篇規劃 + bug-triage-six-patterns + frontend-ui-vocabulary 形成「入門三線」覆蓋——「Bug Report 教學」打**內容寫作入門**、「Bug Triage Pattern」打**組織流程入門**、「Frontend UI Vocabulary」打**詞彙跨領域入門**。三線都吃 SEO 長尾。

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

詳見 [pdt-coach-session-2026-05-12-insights.md](coach-sessions/2026-05-12-insights.md) 末段「後續延伸觀察」。

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
- 🆕 **合寫候選素材**：金流測試的「四層卡點」是另一個「無主之地」具體案例——2026-05-12 PDT Coach session 浮現，詳見 [pdt-coach-session-2026-05-12-insights.md](coach-sessions/2026-05-12-insights.md) 文章 C。可以跟 bug-triage agent 案例合寫成「兩個無主之地」。

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

## 線十一：Mentorship / 新人帶領與認知設計（2026-05-27 新加）

**已上稿**：
- [letter-to-new-qa-two-day-regression](/post/letter-to-new-qa-two-day-regression/)（2026-05-22，跨線四）

**草稿**：
- [cant-teach-while-doing.md](cant-teach-while-doing.md)（生鮮觀察備忘，我懂了我爸做水電為什麼沒辦法邊教邊做）

**規劃中**：
- 詳細大綱與規畫見 [mentorship-newcomer-onboarding.md](mentorship-newcomer-onboarding.md)
- [ ] PDT 帶人法：與其教新人「怎麼測」，不如教他「怎麼問」（將 PDT 問診思維移植給新人）
- [ ] 文件是防禦，PDT 是進攻：如何為新人打造一套認知緩衝區？（以 Living Doc + AI Agent 沙盒打造 Onboarding 系統）

**狀態**：這是為了解決線六（大人學/自省）過載而新闢的專業管理/認知實踐線。第一篇「水電工老爸」情懷與深度並存，第二篇和第三篇直接橋接 PDT 方法論與工具，極具長尾和差異化定位。

---

## 線十二：單兵 QA 的自動化革命 / Bottom-up 導入實踐（2026-05-27 新加）

**規劃中**：
- 詳細戰術地圖與四部曲規劃見 [sole-qa-bottom-up-automation.md](sole-qa-bottom-up-automation.md)
- [ ] **〈單兵 QA 的第一個月：不要大張旗鼓，要「悄悄進行」的影子自動化〉**（政治安全與生存策略，主打「個人工作法改造」）
- [ ] **〈從「痛點工具」起步：如何用 20% 的腳本解決 80% 的每日重複勞動？〉**（痛點驅動、主攻 API/DB 與資料生成，避開重型 UI 框架陷阱）
- [ ] **〈送給 RD 的「特洛伊木馬」：如何把自動化腳本包裝成開發利器？〉**（包裝成 CLI 幫 RD 解放環境預備痛點，結成同盟）
- 🆕 **〈QA 的底線防禦：如何用一套「冒煙測試」解決 PM 的品質認知落差〉**（5/31 B 文）。**核心**：面對 PM 只看 Happy Path 的現況，主動建立基礎自動化防線（Smoke Testing）。
- 🆕 **〈當「業務手感」遇到「技術野心」：QA 如何與 AI 研究員共生？〉**（5/31 D 文）。**核心**：探討如何利用研究員對技術突破的追求，來解決 QA 的業務痛點。
- [ ] **〈把「影子」搬上檯面：如何用數據向主管與 PM 兌換正式的自動化頻寬？〉**（用時間節省與 bug 攔截數據，將影子 CI 兌換為正式 Sprint 頻寬）

**狀態**：與 Rickhw 等顧問式/管理層 top-down 測試策略形成強烈對比。專為初階、單兵、資源匱乏的 QA 設計的 bottom-up 革命指南。極具共鳴性、實操性與長尾 SEO 流量。

---

## 線十三：書評 / 跟測試學派對話（2026-06-01 新加）

**起源**：6/1 重新檢視部落格方向時發現的 gap——5 個月累積 12 條線、全部是「我說的」、**沒有「我跟前人學派的對話」這條線**。書評是補這個缺口最自然的方式。

**為什麼這條線對目前狀況特別合適**：
- **直接解 [pdt-vs-qbt-positioning.md](pdt-vs-qbt-positioning.md) 裡的 todo**：「PDT 主篇加一節『跟業界既有概念的關係』」——書評是這個 todo 最佳實踐手段
- **直接解 imposter 顧慮**：寫對話型書評 = explicitly 認祖宗、跟 established 學派 in dialogue，而不是 isolated「自創縮寫」
- **fit reward 系統**：用作者的思想當鏡子整理自己（A+C 雙 reward）
- **SEO 補強**：「XXX 書 心得」中文搜尋穩定、可補 PDT 主篇長尾弱的洞

**Archetype 選擇**：

| 類型 | 風格 | 對招牌的影響 |
|---|---|---|
| 介紹型 | 「這本書講什麼」 | 稀釋（你變 reader） |
| **對話型**（推） | 「這本書跟我招牌主張怎麼接 / 怎麼不同意」 | 強化（你變 curator + 對話者） |

**規劃中（從已內化內容開始，不用讀新書）**：

| # | 候選 | 已內化證據 | 對話角度 |
|---|---|---|---|
| 1 | **PDT × Whittaker ACC** ⭐ 試刀篇 | [ten-minute-test-plan](/post/ten-minute-test-plan-when-test-stage-down/)、[letter-to-new-qa](../source/_drafts/letter-to-new-qa-two-day-regression.md) 用了 ACC | PDT 跟 ACC 是同源還是補充？「自審覆蓋率」這個維度 |
| 2 | PDT × Bach/Kaner Exploratory Testing | 多次 reference Context-Driven 學派 | PDT 是 Exploratory Testing 的繼承還是切角？ |
| 3 | PDT × Kent Beck TDD | spec-maintenance 隱性 reference | TDD 是「先寫測試」，PDT 是「先問問題」——兩者怎麼互補 |
| 4 | Herzberg 雙因子 × QA 工作 | [letter-to-new-qa](../source/_drafts/letter-to-new-qa-two-day-regression.md) 已用 | 跨域引用——QA 工作的保健 vs 動機因子 |
| 5 | 神經科學讀程式碼 (Ivanova 2020, Siegmund 2014) × QA 閱讀 | [ai-test-case-reading-bottleneck.md](ai-test-case-reading-bottleneck.md) 已展開 | 稀有跨域題、英文圈也少見 |
| 6 | Joe〈職場討論〉「論斷層次」工具 × QA 溝通 | 多次 reference | 跨域引用——溝通是讓對方收懂，論斷是腦的交易 |

**狀態**：6/1 想法成形，未來寫。**第一篇推薦 #1 (PDT × ACC) 當試刀**——素材最熟、跟招牌最 align、不用重讀。

**跟其他線的連結**：
- **線一 PDT**：直接 supporting cast，每篇書評都鞏固 PDT 招牌
- **線八 入門 SEO**：「XXX 書 心得」「軟體測試 推薦書單」長尾關鍵字池
- **線十一 Mentorship**：書評累積到 5-6 篇後，可包成「給新進 QA 的閱讀路徑」
- **跟 [book-ideas-qa-growth-guide.md](book-ideas-qa-growth-guide.md) 的關係**：那邊是「我自己想出的書 idea」（你當作者），這條是「我讀別人的書」（你當對話者）——兩條線互補不衝突

**跟鐵人賽的關係**：
- **Option 1（推）**：書評融入鐵人賽 A 方向當 sub-thread——每週 1 天「跟某本書對話」，當 PDT 30 天的呼吸口、破純方法論的密度
- **Option 2**：書評獨立線、跟鐵人賽分開——平常 cadence 每 2-3 個月 1 篇對話型書評

**狀態**：🔒 想法成形、未來寫。試刀篇可較早動筆（不需等鐵人賽相關決定）。
