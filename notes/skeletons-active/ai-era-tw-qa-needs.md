# AI 時代台灣 QA 需要什麼（5 Gaps 總藍圖）

**建立**：2026-06-11
**狀態**：🌱 骨架——5 個 gap + 對應 article / sequel candidates + 對話深化
**起源**：6/11 早上對話 surface 的 strategic mission 框架。**5 gaps 是 strategic mission level、UI 自動化系列等是 tactical thread**。此檔當 portfolio 總藍圖、不是文章本身。

---

## TL;DR

| Gap | 主題 | 對應既有 / 未來 article |
|---|---|---|
| **1** | 設計 schema vs execute case | UI 自動化系列 5 篇 / [first-principle](software-testing-first-principle.md) / [PM-QA 介面](pm-qa-interface-structured-workflow.md) / yes-man / **〈Bug 標題撰寫指南〉⭐⭐⭐⭐ NEW**（內部教學版去識別化、6/16-18 候選） |
| **2** | 跨角色責任編輯（QBT framework） | QBT 主篇待寫 / PM-QA 介面 / [pdt-vs-qbt-positioning](pdt-vs-qbt-positioning.md) |
| **3** | incident review 文化 / 資產 vs 負債 | [bug-triage-pm-turnover-cost](bug-triage-pm-turnover-cost.md)（aviation framing） / brand-value / smoke-test |
| **4** | AI calibration 中道（不恐慌不崇拜） | yes-man / spec-maintenance / boredom / [AI 耐性赤字（successor reflection）](successor-communication-and-ai-impatience.md) 待寫 |
| **5** | 中文圈方法論稀缺 + 跨領域 framework 引入 | first-principle / ai-test-case-reading-bottleneck（神經科學） / Herzberg × QA / aviation × QA |

---

## Gap 1：設計 schema vs execute case

### 主問
「**AI 時代 QA 還需要寫測試案例嗎？**」當 AI 能 generate / run / assert，QA 的價值不在 execute、是在 **define what to test + 怎麼讀 result**。

### 🔑 核心釐清：schema asset vs test report excel

這兩個常被混為一談、但本質不同：

| | **Schema Asset**（producer-facing） | **Test Report Excel**（consumer-facing） |
|---|---|---|
| 性質 | **跨場景可累積**的 design framework | **一次性 deliverable**、跟特定 release 綁 |
| 重用性 | 設計一次、跨 release / 跨產品多次使用 | 每個 release 重做、不能跨用 |
| 對外可見 | 不直接 visible、是後台 IP | **內外都 visible**——report 是 schema 的 receipt |
| 對內 | 減少每次從零定義、給後輩接手用 | 每次都得 from scratch |

#### 具體 5 個 schema asset 例子（vs 對應 excel）

| Schema Asset（重用） | 對應 Report Excel（一次性） |
|---|---|
| **PM-QA 介面 SOP**：PM 寫 spec 必填欄位 X/Y/Z + 異常路徑 checklist | APP A v1.2 的 spec 文件本身 |
| **Bug severity rubric**：S1=blocker、S2=major、S3=minor、S4=cosmetic 的判定規則 | APP A v1.2 bug list：3 個 S1、5 個 S2... |
| **異常 vs 正常路徑 mapping**：網路斷 / OOM / auth fail 各對應的標準測試 vector | APP A v1.2 異常測試結果：12 通過、3 fail |
| **Coverage gap dashboard schema**：什麼算 covered / 缺什麼 / 用什麼 metric | APP A v1.2 dashboard 截圖 |
| **AI report 對齊 ground truth schema**：AI 判 PASS 的人工抽樣規則、AI 跳測重審判定流程 | AI 報告 vs 人工對照表 |

→ **好的 excel report 是好的 schema 的 output**。

#### 6/3 Lead 講「Report 優先程度比較高」的真實意涵

不是「**請多寫 report**」（那是 execute 任務）、是「**Report 是 Lead 評估你價值的 window**」。每份 report = 你 schema 質量的 demonstration moment。

6/3 Lead 提的 4 條具體要求，**全是 schema-level 指令**（不是「測這幾個 case」）：
- **「bug 描述要更具體**（「一分鐘內閃退」不要寫「放一段時間」）」 = schema-level：**description precision**
- **「手動+自動報告一起貼」** = schema-level：**reporting structure**
- **「AI 報告要先自己看再上報」** = schema-level：**AI integration discipline**
- **「補 AI 跳過沒測的部分」** = schema-level：**coverage gap awareness**

Lead 在告訴你：「**用你的 schema 質量 demonstrate 給我看**」——不是「請執行更多 case」。

### 6/11 對話深化（user Q&A）

**Q: 我的 daily work 70% execute / 30% design**——70/30 比例對嗎？  
→ 對 current APP QA scope 是真實狀態；但要往 RD Head-style QA Head 走、比例要慢慢反過來。**不是急著翻轉、是慢慢累積 schema asset、用 schema 提升 execute 效率**。

**Q: 怎麼證明「我有 design + 駕馭 AI 能力」？「扭轉第一印象很難」？**  
→ **這正是你 6/10 寫的「AI 耐性赤字」的個人活案例**（連 [successor-communication-and-ai-impatience](successor-communication-and-ai-impatience.md)）。

> Reframe：不是「他們錯了 → 我要 argue 扭轉」（argue 框架、產挫折），是「**他們目前看到 70% execute = 真實狀態。還沒累積夠 demonstrate moments**」（demonstrate 框架、產耐性）。

具體 demonstrate moments（已有 + 進行中）：
- ✓ 6/2 IB 事件：誠實 → Head → Lead 拍板（見 [2026-06-01-insights](coach-sessions/2026-06-01-insights.md)）
- 🔄 比較表 prototype（in progress）
- 🎯 **6/3 Lead 提的 4 條 schema-level 要求 = 天然 demonstrate 入口**

**下次 report 機會的 hook**：給「**schema-level summary**」而非 raw list：

> 「v1.2 測試結果：通過層面 A/B、gap 在 C（**需 PM 補 spec**）、AI 跳測層面 D（**我重審後判斷風險低**、原因 X）」

→ schema 設計能力 + AI 中立判讀**自然隱含**在 report、Lead 一眼看見。

### 🔑 6/11 後續發現：「Excel 弱」自我評價 mislabel + 策略 precision

user 6/11 下午 share「**Bug 標題撰寫指南（QA 新人必讀・內部版）**」→ **這份指南本身就是 textbook schema asset**（公式 + 526 筆真實數據 backing + 改寫前後 + checklist + 速查卡 + 練習題、多層次 schema design）。

#### 自我評價校正

| 之前以為 | 實際（指南 evidence） |
|---|---|
| schema 弱 | **schema 強**（指南是 SOP 級設計） |
| Excel skill 弱 | 你已會做 schema asset、**指南就是** |
| 不擅長 design | 指南是多層次 design |

→ 真正 gap 更精準：「**在既有 legacy template 政治脈絡內 deploy schema 質量的能力**」（不是 schema design 能力本身）。

#### 環境校正（user 6/11 surface）

部門 excel template 是 **legacy system**：
- 部門建立時就有 template、現在大家在「**修修補補**」維護模式
- 已有 app sheet 等方式追蹤上千 excel 既有架構
- 一部分是主管 upward reporting 數字
- **改 template 架構要內部審核**

→ 「build master template」不適用、要 navigate existing。

#### 策略 3 tier（替代原「master template」hook）

| Tier | 動作 | 政治 cost |
|---|---|---|
| **1** 不改 template | 在現有結構內、**填寫時用 schema-driven 思維**（bug 描述用指南標準格式、coverage 填法 surface gap schema） | 0 |
| **2** 小修 template | propose 一兩個 schema-aligned tweaks、走內部審核 | 中（學 stakeholder negotiate） |
| **3** 累積 internal SOP | bug 標題指南這種 document、持續累積、變部門資產 | 0（**你已在做**） |

→ schema 質量在「**填寫 + 累積 SOP**」、不在「**改 template**」。

#### Huge article candidate：〈Bug 標題撰寫指南〉去識別化版

「Bug 標題撰寫指南」內部版**去識別化後是 ⭐⭐⭐⭐ 長尾 article candidate**：

- **中文圈稀缺**：沒人寫好的 bug 標題寫法文
- **SEO 強**：「bug 標題寫法」「QA bug report 範例」「bug 標題格式」
- **已有 polished 版本**（effort 低 = 去識別化 + 改寫）
- **連 6/11 上稿的 [bug-triage cluster](/post/bug-triage-six-patterns-industry-survey/)**：bug 治理 → **bug 標題** → bug triage
- **直接呼應 6/3 Lead 提的「bug 描述要更具體」**——demonstrate 你 own 這個 schema thinking

去識別化要點：
- 真實產品名（強棒旺旺來 / 長線聚寶盆 / 處置神器 / 美股集大成 等）→ 抽象化「產品 A / B / C」或通用例子
- Jira 真實單號 / 內部產品名稱 → 改編
- **526 筆內部數據 → 保留 statistical observation、抽象化 source**（「我撈了我們近半年 526 筆 bug」→「我撈了某中型 QA 團隊半年數百筆 bug」）
- 部門人名（小明 / 林恩如 / 權證小哥）→ 全部 mask
- 「真實壞例」section → 保留結構、用通用化案例

排程候選：**6/14 ship A 之後、6/16-18 動筆**（趁 bug-triage cluster reader pipeline active）。

### Open questions（給未來自己想）

- [ ] 怎麼把 schema 變成可遞交給後輩接手的 asset？（連 Mentorship 線十一、**bug 標題指南本身就是一個範本**）
- [ ] schema asset 累積到什麼 threshold 算「**從 execute 升為 design 主導**」？（量化 indicator）
- [ ] 70/30 比例 → 50/50 → 30/70 的時程合理嗎？（馬拉松配速）
- [ ] 「**在 legacy template politics 內 deploy schema**」這個能力怎麼練？除了 bug 標題指南、還有哪些既有 SOP 我已經做了 / 可以做？
- [ ] Tier 1（填寫 schema-driven）vs Tier 2（小修 template）的 trade-off：什麼時候該 push Tier 2、什麼時候停在 Tier 1？

---

## Gap 2：跨角色責任編輯（QBT framework）

### 主問
「**QA 是 PM-RD 之間的責任編輯嗎？**」（連 5/29 你自己 surface 的「責任編輯」隱喻 + 6/4 PM-QA 介面）

### Open questions
- [ ] 「責任編輯」對中文圈讀者夠不夠 grok？需不需要更 visceral 的比喻？
- [ ] 我目前怎麼跟 PM 互動？被動接需求 / 主動定義 schema / 結構化異步
- [ ] 我目前怎麼跟 RD 互動？挑錯 / 提建議 / **同謀**

### 對應 article
- [pdt-vs-qbt-positioning](pdt-vs-qbt-positioning.md)（戰略討論）
- [pm-qa-interface-structured-workflow](pm-qa-interface-structured-workflow.md)（骨架）
- QBT 主篇待寫（等 PDT 顯性化第二份 + 讀者反應）

---

## Gap 3：incident review 文化 / 資產 vs 負債（aviation framing）

### 主問
「**Bug list 是資產還是負債？**」軟體業缺事故分類 framework、決定整個 backlog culture。

### Open questions
- [ ] 我所屬團隊的 bug list 文化在 spectrum 哪裡？（負債極端 ←→ 資產極端）
- [ ] 我能不能 build individual 級的 incident classification？不依賴組織授權
- [ ] 中文圈誰在做這個議題？SEO 機會 + 潛在結盟對象

### 對應 article
- [bug-triage-pm-turnover-cost](bug-triage-pm-turnover-cost.md)（含 aviation framing 升級 + 6 個候選標題）
- [brand-value-and-smoke-test-proposal](brand-value-and-smoke-test-proposal.md)（連動）
- 6/10 已發 [bug-triage-six-patterns-industry-survey](/post/bug-triage-six-patterns-industry-survey/)

---

## Gap 4：AI calibration 中道（不恐慌、不崇拜）

### 主問
「**我自己跟 AI 互動的 calibration 在哪？**」你已寫 yes-man / spec-maintenance / boredom 處理「AI 是 partial 認知」。**還沒寫**：個人層級的 AI 耐性赤字。

### Open questions
- [ ] **個人層級**：怎麼避免被 AI 即時回饋訓練成耐性赤字？（你 6/10 reflection 已 surface）
- [ ] **團隊層級**：我們對 AI 的共識在哪？沒共識誰該推 framework？
- [ ] **公開層級**：中文圈缺「AI calibration 中道」文章嗎？（觀察：**極缺**——大部分中文 AI × QA 文章不是吹 AI 就是嚇 QA）

### 🔑 6/11 新加 personal layer 維度

從 Gap 1 Q3 對話 surface 出來：**「扭轉別人第一印象很難」≈「人際反饋週期月級、我希望秒級」≈ 個人被 AI 訓練的耐性赤字 wired**。

→ Gap 4 不只是「**團隊 / 公開層級對 AI 的 calibration**」，還包括「**個人層級避免被 AI 訓練的耐性赤字扭曲對組織 / 人際的耐性**」。

### 對應 article
- 既有：[yes-man](/post/ai-as-yes-man-rd-pm-trust-calibration/) / [spec-maintenance](/post/spec-maintenance-gray-zone/) / [boredom](/post/boredom-is-a-signal/)
- 待寫：**〈AI 時代組織耐性赤字〉**（從 [successor-communication-and-ai-impatience](successor-communication-and-ai-impatience.md) 寫成完整文）—— **6 月底 anchor 候選**

---

## Gap 5：中文圈方法論稀缺 + 跨領域 framework 引入（台灣特殊脈絡）

### 主問
「**我部落格在中文 QA 圈的 niche 一句話定位是什麼？**」中文 QA 圈缺好的方法論文章 + 跨領域 framework 引入幾乎沒人做（你已引入：神經科學 / 統計學 / 航空業 / Joe 論斷 / Herzberg / 責任編輯 / 馬拉松配速）。

### Open questions
- [ ] 一句話定位：PDT 招牌？跨領域思考？組織派 QA？
- [ ] 台灣 QA 圈有哪些「無主之地」議題？（連線十、可挖掘）
- [ ] MoT / Context-Driven 中文化 / 鐵人賽——哪些通路最 fit niche？

### 對應 article（已引入跨領域 framework 的）
- [first-principle](software-testing-first-principle.md)（含統計學 × 航空業）
- [ai-test-case-reading-bottleneck](ai-test-case-reading-bottleneck.md)（神經科學）
- [letter-to-new-qa-two-day-regression](/post/letter-to-new-qa-two-day-regression/)（Herzberg 雙因子）
- [bug-triage-pm-turnover-cost](bug-triage-pm-turnover-cost.md)（aviation 安全文化）

---

## 跨 Gap 的元問題（最深一層）

如果要把 5 個 gap 合成一個 **一句話 mission statement**：

> **「我想成為 AI 時代台灣 QA 從『執行者』升級成『定義者』的中文圈方法論引路人。」**

🤔 **這個句子你接受嗎？想改成什麼版本？**

- 接受 = 鐵人賽方向自然定（A 升級版 PDT × PM-QA 結構化 + 跨領域 framework）
- 想改 = 你想成為什麼？這個答案決定下半年所有 article 排序

---

## 使用方式（給未來自己）

1. **不要一次答 11+ 個問題**。一週挑 1-2 個、寫在 daily reflection 裡、慢慢沉澱
2. **8 月底鐵人賽心理體檢前**自然會有答案——5 gap 的 personal answers 直接決定鐵人賽方向
3. **新文章 idea 出現時**、優先 mapping 到對應 gap（如果不 fit 任何 gap、可能 niche 偏了）
4. **每個 Coach session 後**檢查：今天的反思是否更新了某個 gap 的 open questions？

---

## 索引

- 6/11 起源對話：本檔開頭「起源」段
- 5 gaps 出處：今天早上對「下一篇寫什麼」的 brainstorm
- 個人層級耐性赤字 reflection：[successor-communication-and-ai-impatience](successor-communication-and-ai-impatience.md)
- 鐵人賽 endgame 連結：[ithome-ironman-2026-planning](ithome-ironman-2026-planning.md)
- 跟 [first-principle](software-testing-first-principle.md)：三方 partial frame 是 Gap 1 的理論底層
- 跟 [pdt-vs-qbt-positioning](pdt-vs-qbt-positioning.md)：QBT 框架是 Gap 2 主軸
