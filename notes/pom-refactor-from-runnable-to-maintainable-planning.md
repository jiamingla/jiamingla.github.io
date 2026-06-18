# POM 重構實戰：規劃與思考備忘錄

> 📂 **定位**：此篇為 [pom-refactor-from-runnable-to-maintainable](../source/_drafts/pom-refactor-from-runnable-to-maintainable-planning.md) 的規劃文件。用於整理文章的個人故事背景，以及在 AI 時代重新審視 POM 技術價值的思考。

---

## 📌 個人故事背景（情感引子）

*   **大四實習的啟蒙**：
    大四實習時第一次接觸到 POM（Page Object Model）這個設計模式。那時候只覺得它是一個「把元素定位點集中放到 Class 屬性」的排版技巧。
*   **如今的頓悟與實踐**：
    多年以後，在職場上面對真實且龐大、脆弱的自動化專案，經歷了無數次 UI 改版導致腳本全面崩潰的痛楚，才終於明白大四學到的這個概念是多麼強大。這篇文章要寫出這種**「多年前種下的子彈，如今正中紅心」**的真實體會，向讀者傳遞：設計模式不是死板的教科書，而是前人踩坑後的求生指南。

*   **履行開台宣言的承諾**：
    此篇技術實踐正是為了回應開台藍圖 [testing-manifesto.md](../source/_posts/testing-manifesto.md) 中，至今仍標註為「仍規劃中」的 **Page Object Pattern (POM)** 技術支柱。撰寫並發表此文，代表完成了開台初期承諾的核心技術版圖。

---

## 🤖 在 AI 時代重新定義 POM 的價值

當執行測試、撰寫或維護腳本的代理人從「人類」漸漸變成「AI Agent」時，傳統的 POM 不僅沒有過時，反而展現了全新的戰略優勢：

### 1. 為 AI 建立一套「樂高積木（Tool API）」
*   如果我們給 AI 原始的 `driver.find_element` 控制權，AI 在自動生成或維護測試時，必須面對混亂的 HTML 結構、隨機變動的 CSS/XPath，這極易導致 AI **幻覺（Hallucination）**或生成極其脆弱的代碼。
*   如果我們將頁面封裝成乾淨的 Page Object，給 AI 提供如 `LoginPage.login(user, pwd)` 這樣高語義的 Method，對 AI 來說這就是一組**已經封裝好的「Tool / Skill」**。AI 只需要專注於「呼叫 Tool 拼接業務意圖」，出錯率會降低 80% 以上。

### 2. 隔離 AI 的修改邊界（Context Isolation）
*   當 UI 改版時，如果沒有 POM，AI 需要去掃描並修改 50 個相關的測試測試檔案，這會消耗極大的 Context Window，且極易在修改過程中引入新的 Bug。
*   在 POM 架構下，UI 改動的影響範圍被**完全限縮在特定的 Page Object 類別中**。我們（或 AI）只需要修改單一檔案的定位點或行為，其餘的測試案例一個字都不需要改。這讓 AI 進行「自我修復（Self-healing）」的成本和風險降到最低。

### 3. 人類與 AI 的新分工（Human-AI Partition）
*   **人類的職責**：看懂系統的「局」，負責設計與定義高品質、高語義的 Page Object 介面（API），確保底層定位與等待機制的硬度。
*   **AI 的職責**：利用人類提供的高階 Page Object 積木，自動撰寫、生成、排列組合出數百條不同的測試案例。
*   **結論**：**POM 寫得好不好，直接決定了你的自動化架構對 AI 協作是否友善。**

#### 🎯 分工的精準切法（2026-06-17 user surface）：沿 POM 三層切

> **「這樣的分工相對理想：給 AI 找元素定位器、給人類決定測試的預期結果。」**

把分工**對齊到三層責任分離**，會發現它不是隨便分、是**切在 AI 的能力邊界上**：

| POM 三層 | 性質 | 該歸誰 | 為什麼 |
|---|---|---|---|
| **Selector（找東西 / where）** | 機械式 pattern-matching：在 XML 裡找元素 | **AI** | 這正是 AI 強項；smoke 框架實證「給 AI 半小時調定位器」 |
| **Wait（時機）** | 多半機械、可模板化 | AI / 框架 | 等待條件可標準化 |
| **Assertion（預期結果 / what's correct）** | **判斷 + oracle**：什麼叫「對」 | **人類** | **AI 沒有 ground truth、會幻覺**；「預期結果」是測試意圖、是人不可取代的那塊 |

→ **這條分工線的本質**：沿著「**機械 vs 判斷**」「**pattern-matching vs oracle**」切。AI 接「東西在哪」（可窮舉、可驗證），人接「什麼才對」（需要 domain 判斷、沒有絕對基準）。
→ **深層連動**：「預期結果 = oracle = AI 最不可靠的部分」直接接 [proving-a-bug-is-gone](proving-a-bug-is-gone-verification-philosophy.md)（沒有 gold standard / oracle 問題）+ [pass-fail-not-enough](../source/_drafts/pass-fail-not-enough-for-ai-testing.md)（verdict vs confidence）。也呼應 POM 鐵律「**assertion 不該進 PageObject、它是測試意圖**」——測試意圖屬於人。
→ **金句候選**：「AI 負責找到『東西在哪』，人負責決定『什麼才算對』。前者可以窮舉、後者需要判斷——這條線就是 AI 時代 QA 不可取代的邊界。」

### 4. 後端/API 測試中的「POM 變奏」：API Client / Service Object
*   **困惑排除**：對於「只測後端、不碰前端 UI」的 QA 而言，POM 模式（代表 Page 網頁）確實沒有用武之地。
*   **本質心法一致**：雖然 POM 不適用於後端，但它的**封裝心法（Separating Intent from Implementation）**完全是共通的。在後端測試中，我們不寫 Page Object，而是寫 **API Client Wrapper** 或 **Service Object**。
*   **痛點與解法**：不應該把 HTTP 請求的細節（URL、Header、Payload 結構、Auth 機制）散落到各個 API 測試案例中。我們應該將其封裝進一個 API Class（例如 `UserApiClient.create_member(name, age)`）。
*   **對 AI 的好處**：這同樣隔離了 API 協定的變動，並為 AI Agent 提供了乾淨的「後端 API 工具箱」，讓 AI 寫後端集成測試時，不需在程式碼中大肆猜測 HTTP 欄位，這本質上就是「POM 思維在後端的完美變奏」。

---

## 📝 文章待調整結構

*   **前言**：以大四實習時的起點作為故事開頭，拉近與讀者的距離。
*   **核心章節**：保留「三層責任分離（Selector/Wait/Assertion）」與虛擬爛 Code 對照。
*   **新增章節：〈在 AI 時代，為什麼我們比以前更需要 POM？〉**：
    *   將上述「Tool API 封裝」、「隔離 AI 修改邊界」、「Human-AI 分工」的論點寫進去，作為這篇老技術文章的**新時代 differentiator**。
*   **結語**：將 POM 與 PDT 連動，強調「POM 寫得爛，PDT 就跑不起來；POM 寫得好，AI 就能幫你跑起來」。

---

## 🟢 真實案例升級（2026-06-17）：smoke 框架是這篇所有論點的活證據

> 原本文章用**虛構 demo（shop.example.com）**示範三層責任分離。但 user 手上有一套**真實在跑的單兵 smoke 框架**（`AutoTesting/Author/smoke_script/`，去識別版見 [smoke-test-golden-set-spec](smoke-test-golden-set-spec.md)）——**它是本篇每個論點的活證據，遠比虛構 demo 有說服力。**

| 本篇論點 | smoke 框架的活證據 |
|---|---|
| **POM 橋樑：UI 變、測試意圖不變、只動那座橋** | **7 個 APP、4 種架構（Pages / 傳統原生 / 純 Compose）、共用的 `pages/` 與 `tests/` 一行未改**——所有差異全壓在各自 locator 檔。「框架是常數、adapter 是變數」 |
| **AI 角度 1+2：Tool API + 隔離修改邊界** | 「**交給 AI 半小時完成元素定位器調整、人工只做 review**」——新增一個 Pages App 約 30-40 分鐘。這就是 Tool API + self-healing 的真實 ROI |
| **AI 角度 3：Human-AI 分工** | 人定義 `pages/` 介面 + 登入版型抽象（3 版型靠 mixin），AI 補各 App 的 locator。**人設計骨架、AI 填變數** |
| **連 PDT 結語** | smoke 是「確認核心存活」的風險控制網，不是「證明無 bug」——接 [first-principle](software-testing-first-principle.md) / [proving-a-bug-is-gone](proving-a-bug-is-gone-verification-philosophy.md) |

→ **寫作建議**：虛構 demo 留作「教學用最小例」，但**主案例升級成這套真實框架**（去識別後）——「我用一套 POM 服務 N 個 APP、pages/ 一行沒改」比 shop.example.com 強十倍。
→ ⚠️ **去識別化**：smoke README 公司指紋極重（真實 app 名、package、CMoney 統一登入、ChipK）。**好消息：[smoke-test-golden-set-spec](smoke-test-golden-set-spec.md) 已是去識別版（app_a/b/c）**，直接拿那份的措辭當基底。
→ **這也是 user 的「單兵實戰」證據**——駁倒「我沒單兵經驗」的焦慮（見 [writing-without-lived-experience](writing-without-lived-experience-honest-stance.md)）。

---

## 🔗 與其他規劃/備忘檔案的關聯

*   **[smoke-test-golden-set-spec.md](smoke-test-golden-set-spec.md)（核心冒煙測試 Golden Set，已去識別）**：本篇 POM 論點的真實實作 + 去識別措辭基底（見上節）。
*   **[cross-app-locator-strategy.md](cross-app-locator-strategy.md)（跨 APP 元素定位策略）**：
    *   **實戰案例對照**：記錄了 N 個作者 App 共用測試 lib 的真實場景。不同 App 的 UI 細節（如 `resource-id` 有無、容器命名）大相逕庭，但「搜尋頁標題」或「鈴鐺按鈕」的**測試意圖完全相同**。
    *   **POM 作為橋樑的極致展現**：可作為本篇 POM 文章的**硬核技術案例**——「UI 變動、但測試意圖不變」的真實示範，說明如何透過 `LocatorStrategy` 將混亂 XML 結構封裝在 PageObject 底層，對上層測試（與 AI Agent）呈現乾淨統一介面。

