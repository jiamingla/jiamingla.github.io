---
urlname: ai-test-output-default-reader-is-ai
title: 為什麼 AI 給的測試案例讀起來特別累？因為它的預設讀者不是你
date: 2026-08-15 22:00:00
tags: [軟體測試, AI 測試, AI literacy, 跨領域, 閱讀策略, prompt design, 品質工程]
---

> ✏️ 這是一篇種子稿。是 [ai-as-yes-man-rd-pm-trust-calibration](ai-as-yes-man-rd-pm-trust-calibration.md) 的**配對作品**——yes-man 講「**怎麼問 AI**」，本篇講「**怎麼讀 AI 給的東西**」。兩篇合稱「**Working with AI Output**」雙篇。
>
> **起源**：2026-05-14 從 [frontend-ui-vocabulary-for-backend-qa](frontend-ui-vocabulary-for-backend-qa.md) 衍生——寫那篇時意識到「AI 預設讀者不是你」是個更大的命題，值得獨立成篇。

---

## 預設讀者（2026-05-14 確定）

**主要讀者：中文圈 QA + 單一專業背景的 QA**——特別是：

- 中文母語但要讀 AI 用英文 jargon 為主的測試案例
- 專精單一領域（後端 / 行動 / 自動化 / API）但 AI 給的測試案例跨領域
- 開始用 AI 寫測試案例，發現「**讀** AI 給的東西比想像中累」

**這是繁體中文 QA 部落格的 differentiator**——大部分英文 AI/testing 部落格**不會討論**「英文 jargon 對非母語讀者的隱形負擔」這個面向。

**核心訊息**：你讀 AI 測試輸出會累，**不是你能力不足，是 AI 預設讀者不是你**——而這可以調整。

---

## 寫作風險備忘

中度風險：

- **不能寫成「AI 不好」的調性**——你的部落格主軸是「**AI 為殼、方法論為內**」（見 [tools-first 策略](C:\Users\user1\.claude\projects\c--Users-user1-Documents-GitHub-jiamingla-github-io\memory\project_tools_first_strategy.md)），這篇要 stay on brand。框架成「AI 預設行為合理，但**人類讀者該知道怎麼適應**」
- **避免「中文 / 英文好壞」的政治雷區**——只談「非英文母語讀英文 jargon 的認知負擔」，不評價語言優劣
- **不點名 AI 工具 / vendor**——這個觀察對所有 LLM-based 測試輸出都成立，點名招敵人

---

## 緣起

寫 [frontend-ui-vocabulary-for-backend-qa](frontend-ui-vocabulary-for-backend-qa.md) 時我意識到——「**我看不懂 skeleton loading**」這個現象本身就是個更大命題：

> AI 寫測試案例時，**預設讀者剛好是另一個 AI**——一個讀過全 corpus、跨所有專業、英文流利的讀者。但**真實讀者**是專精某一兩個領域、中文為主、英文 jargon 半懂的人類 QA。

這個 mismatch **不是 bug、不是品味問題、也不是 AI 該被改**——它是 LLM 在 cross-domain corpus 上訓練的結構性結果。但人類讀者需要知道：你不是失格的讀者，**你是 AI 預設讀者光譜外的讀者**——你可以調整。

---

## 文章主結構（草擬）

### 一、開場：你讀 AI 給的測試案例會覺得累嗎？

可能的開頭：

> 你有沒有過這個經驗——叫 AI 幫你寫測試案例，跑出來這麼一段：
>
> > 「驗證 modal 彈出時應觸發 focus trap，並在 ESC 鍵按下時 dismiss，同時保留前一個 active element 的 focus state。」
>
> 你讀了三次，每個詞似懂非懂——`focus trap`？`active element`？  
> 然後**你停了下來，懷疑自己是不是該換工作**。
>
> 別急著責怪自己。**AI 寫的這段測試案例，從來就不是寫給你看的**——它的預設讀者，是另一個 AI。

### 二、三層 mismatch：AI 預設讀者 vs 真實讀者

| 層次 | AI 預設讀者特徵 | 真實 QA 讀者特徵 |
|---|---|---|
| **專業廣度** | 跨所有 specialty（前/後/行動/a11y/DevOps/security...） | 通常專精 1-2 個 |
| **語言** | 英文流利、jargon 不費力 | 中文母語、英文 jargon 半懂 |
| **基礎假設** | 假設讀者讀過 React / Vue / Material Design 文件 | 通常沒讀過、或只讀過自己工作用的 |

這三層加起來——**每個術語就像一個小門檻**。AI 不知道哪幾個門檻對你存在，全部寫在一起，你的閱讀體驗就是**連續跨欄**。

### 三、為什麼這個 mismatch 結構性存在

不是 AI 在偷懶——是 **LLM 訓練語料的結構性結果**：

1. **訓練語料是全 corpus** —— StackOverflow / GitHub / MDN / 設計部落格全混在一起
2. **沒有讀者畫像** —— AI 不知道你是 backend QA 還是 frontend designer
3. **英文 jargon 是 corpus 的 lingua franca** —— 即使 AI 用中文回答，jargon 仍是英文（`focus trap` 永遠不會被翻成「焦點陷阱」，因為這個翻譯沒在語料裡）
4. **AI 預設「讀者也讀過全 corpus」** —— 因為訓練 AI 的就是讀過全 corpus 的「讀者」

這不是 bug——是 **AI 缺乏預設的「角度感知」**。它不知道**你站在哪裡看它**。

### 四、人類 QA 該怎麼讀 AI 測試輸出（具體技巧）

#### 4.1 為自己 prompt design

別讓 AI 用「預設讀者」寫——告訴它你是誰：

```
請以後端 QA 的視角寫測試案例，中文為主，
英文術語第一次出現時用括號加中文簡述。
我不熟前端 UI 詞彙，請避免假設我懂 `focus trap`、
`floating label` 這類細節，必要時請帶一句說明。
```

光是這段 prompt 加在最前面，AI 給的輸出對你會友善 60%。

#### 4.2 讀不懂的詞當作「免費的詞彙考試」

別跳過不懂的詞——把它當 PDT 的反向應用：

> **AI 給的每個你不懂的詞 = 你下一節該學的詞**

這正是 [frontend-ui-vocabulary-for-backend-qa](/post/frontend-ui-vocabulary-for-backend-qa/) 的核心——學完那一輪詞彙，前端方向你就**至少不會被卡住**。

#### 4.3 翻譯 → 才給團隊

別把 raw AI 輸出貼給團隊。先翻譯：

- 把英文 jargon 換成你團隊用的詞（或括號加註）
- 把跨領域 reference 拿掉（你團隊不需要的）
- 把 AI 的 ambiguous 部分明確化（補上「在我們情境下這代表 X」）

**這也是 [yes-man 提問清單](/post/ai-as-yes-man-rd-pm-trust-calibration/) 第三個問題的延伸**——AI 跳過了什麼、隱含了什麼，讀的時候要主動補上。

#### 4.4 建立你自己的 glossary

每次學到新詞，記下來。一年累積下來，你就是團隊裡那個「**AI 翻譯員**」——這比硬補英文程度更實用、更可被同事看見。

### 五、跟 yes-man 配對：Working with AI Output 雙篇

| 篇 | 動詞 | 核心問題 |
|---|---|---|
| [yes-man](source/_drafts/ai-as-yes-man-rd-pm-trust-calibration.md) | **問** | AI 跑出綠燈時，你該問哪三個問題才不會出事？ |
| 本篇 | **讀** | AI 給的輸出讀起來累，該怎麼讀才不被詞彙磨損？ |

兩篇放一起，QA 在 AI 時代的兩個核心技能就齊了——**會問 + 會讀**。

### 六、結語：AI 是免費的詞彙考試

> 你讀 AI 測試輸出會累——這不是你的問題，是 AI 沒有預設讀者畫像。  
> 但這個現象有個正向解讀：
>
> **AI 的輸出，是你最便宜的『下一階能力檢測』**。你讀不懂的詞，正好是你下次該學的詞。
>
> 跟 AI 一起工作幾年，你會發現自己的詞彙、視野、跨領域感知都被它**動拉**著擴張——這比上課還有效。
>
> 只要你**不被詞彙嚇退、不誤把疲勞當作能力不足**。

---

## 跟其他線的關係

| 主題線 / 篇 | 關係 |
|---|---|
| **線二（AI 取代 / 當責）** | 主場——AI literacy 是這條線的自然延伸 |
| **線一（PDT）** | 4.2 的「免費詞彙考試」是 PDT 的反向應用——別人給的東西暴露你沒問過的問題 |
| **線八（入門 / 長尾 SEO）** | 「為什麼 AI 給的測試案例讀起來累」這個 query 搜尋友善 |
| **配對篇：[yes-man](source/_drafts/ai-as-yes-man-rd-pm-trust-calibration.md)** | 「**Working with AI Output**」雙篇——會問 + 會讀 |
| **子題篇：[frontend-ui-vocabulary-for-backend-qa](source/_drafts/frontend-ui-vocabulary-for-backend-qa.md)** | 本篇是 vocab 篇的**抽象版**——vocab 是「這些詞是什麼」、本篇是「**為什麼 AI 用了你不懂的詞**」 |

---

## 寫作前還沒解決的

- [ ] **中文圈 differentiator** 要不要寫得更明確？還是只在 framing 暗示？
- [ ] 第四節「具體技巧」做成 checklist 還是流暢散文？
- [ ] 例子怎麼選——「`focus trap` 我看不懂」這個例子要不要換成更普及的？
- [ ] 結語的「動拉」這個動詞——太特別還是有畫面？看寫的時候感覺
- [ ] **觸發條件**：跟 yes-man 同期或緊接著上稿，當「Working with AI Output 雙篇」連發
- [ ] 4.1 的 prompt 範例要不要做更完整（含 token 預算、輸出格式期待等）？還是保持精簡？

---

## 一句話定位

> 你讀 AI 測試輸出會累，不是因為你能力不足——是因為 **AI 預設讀者剛好是另一個 AI**，而你不是。但這個現象正面看：**AI 的輸出，是你最便宜的下一階能力檢測**。
