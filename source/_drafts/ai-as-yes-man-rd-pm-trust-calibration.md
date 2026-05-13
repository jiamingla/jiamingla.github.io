---
urlname: ai-as-yes-man-rd-pm-trust-calibration
title: 你以為 AI 在當你的 QA，其實它在當你的 Yes Man——給 RD/PM 的三個提問清單
date: 2026-08-01 22:00:00
tags: [軟體測試, AI 測試, 跨團隊協作, RD, PM, 問題驅動測試, 測試結果歧義, AI 取代, 品質工程]
---

> ✏️ 這是一篇種子稿。是 [notest-ambiguity-skip-vs-low-confidence](notest-ambiguity-skip-vs-low-confidence.md) 的**姐妹篇**——同一個母題（AI 跑測試的判讀問題）、不同讀者（RD/PM 不是 QA）。**這篇先於 notest 上稿**（2026-05-13 訂），notest 之後從 schema 層延伸。

---

## 預設讀者（2026-05-13 確定）

**寫給 RD 和 PM 看**——特別是**已經開始用 AI 幫自己跑測試的 RD/PM**，繞過了傳統 QA 流程。

這跟 QA 那篇的讀者起點完全不同：

| 維度 | QA 那篇 | 這篇（RD/PM） |
|---|---|---|
| 讀者起點 | 已有 `pass / fail` schema、會 review 結果 | **沒有 schema**——AI 跑完就看綠燈/紅燈 |
| 失敗模式 | 把不確定塞進 `notest`、欄位坍縮 | **過度信任 AI 的綠燈**、把 AI 的不質疑當測完了 |
| 真正的問題 | schema 設計不夠細 | **缺少 QA 的懷疑體質** |
| 該帶走什麼 | 多軸 schema + 信心度當屬性 | 哪些問題要問 AI 的測試報告才不會出事 |

**核心句**：QA 升級的是欄位設計；RD/PM 該升級的是**對 AI 的提問習慣**。

---

## 寫作風險備忘

風險比 QA 那篇低，但仍有兩處要注意：

1. **不要點名具體 AI 工具 / vendor**（Cursor / Copilot / Cline / browser-use 等）——這篇的論述對所有 LLM-based AI testing 都成立，點名會招來貼標反應，反而失去普遍性
2. **「AI 是你的 Yes Man」這句要框架成普遍現象，不是針對讀者**——用 QA 圈共同觀察的口吻，不要寫成「你以為你會看 AI 結果但其實不會」這種逼迫式語氣。讀者是 RD/PM 不是 QA，挑釁太重會關閉他們

---

## 緣起（觸發點，不直接當文章 hook）

QA 那篇從**主管問同事**為什麼有那麼多 `notest` 切入，意識到「中間態坍縮」是個共通母題。但 QA 那篇預設讀者已經有 schema 在用——對 RD/PM 來說，**他們連這個問題的入口都還沒到**：

> 「我讓 AI 幫我寫測試、跑測試、給我結果——它說 OK 就是 OK 吧？」

這篇要讓 RD/PM 意識到：**AI 給你的綠燈跟 QA 給你的綠燈，是兩種完全不同的綠燈**。前者需要你補上自己的懷疑；後者已經內建了一個對你的產品挑刺的人。

---

## 文章主結構（草擬）

### 一、開場：你已經讓 AI 幫你跑測試了，但你怎麼知道它沒在敷衍你？

**Hook**：

> 你做完一個 feature，叫 AI 幫你跑測試。  
> 它跑了。它說 OK。你 push 上去。  
> ——但你怎麼知道它**真的測了**你以為它測的東西？

不從技術層切入，從**信任層**切入。RD/PM 不在乎 schema，他們在乎「**我這次能不能下班**」。

### 二、核心論點：AI 不是你的 QA，是你的 Yes Man

這節是文章的脊椎——把 RD/PM 對 AI 的角色認知撐開：

| 角色 | 職業反射 | 對你的態度 |
|---|---|---|
| **QA** | 找出你想不到的失敗路徑 | 對你的產品**有敵意**（健康的敵意） |
| **AI** | 盡量回應指令、給看起來像答案的東西 | 對你**過度配合**——對齊壓力讓它傾向給合理答案 |

**關鍵差異**：QA 知道自己會有盲點，所以會主動懷疑；AI **不知道自己有盲點**，所以會把「不確定」也包裝成「OK」。

舉一個常見場景：

> 你叫 AI 測「使用者登入後可以看到首頁」。AI 跑了一輪，回報 `pass`。  
> 但它實際上做了什麼？可能它真的開瀏覽器測了、可能它讀 code 推測能通過、可能它只 mock 了登入 API。  
> **報告長一模一樣，背後的可信度差三個量級**。

### 三、三個必須問 AI 的問題

文章的 actionable 主體——給 RD/PM 一份**明天就能用的提問清單**：

#### 問題 1：「你測的是我要的東西，還是你決定的東西？」

防範 scope drift。AI 為了給出「合理答案」，常常會**悄悄縮小測試範圍**——你叫它測登入，它可能只測了 happy path，邊界 case、錯誤 case、不同帳號狀態全部省略。

具體該問：
- 你實際執行了哪些步驟？（不要只看結論）
- 你跳過了哪些原本該測的場景？為什麼跳過？

#### 問題 2：「你有多確定這個 pass？」

對應 QA 那篇的核心——**信心度**。讓 AI 自己回報信心，把 binary verdict 變成 verdict + confidence。

具體該問：
- 對這個 pass 你有幾成把握？（high / medium / low）
- 哪一部分讓你不確定？

> 注意：AI 自己回報的 confidence 不完全可信（它有時會過度自信），但**逼它輸出 confidence 這個動作本身**會讓它的 reasoning 更謹慎——這個現象在 LLM 研究裡叫 metacognitive prompting。

#### 問題 3：「你跳過了什麼、沒測什麼？」

這對應 QA 那篇的 `notest` 命題——但對 RD/PM 來說更陰險：**他們的 AI 測試報告通常根本沒有「跳過」這個欄位**。AI 跳過的東西會直接消失，不會出現在 dashboard。

具體該問：
- 列出所有你**想測但沒測**的項目，以及原因
- 列出所有你**根本沒考慮去測**的項目（這層 AI 通常答不出來，但問了會逼它再 review 一輪）

### 四、為什麼這三個問題會奏效

不只是禮貌——是利用 LLM 的兩個機制：

1. **Metacognitive prompting**：逼 AI 對自己的輸出做 reasoning，會降低過度自信
2. **Scope explicitness**：scope 模糊時 AI 傾向悄悄縮減；scope 被質問時 AI 會更誠實列出

技術讀者會喜歡這層解釋；非技術 PM 跳過也不影響理解。

### 五、給 PM 的特化建議（短節）

PM 用 AI 跑驗收測試的場景跟 RD 不同：

- PM 通常**沒有測試方法論**，所以更容易被綠燈說服
- PM 的 risk 是 **confirmation bias** ——他們希望 feature 過，AI 也希望給他想要的答案，兩邊一拍即合
- **特化的提問**：「假設你是這個產品最挑剔的使用者，你會怎麼戳壞它？」

把 AI 從 Yes Man 翻成 critic，是 PM 用 AI 測試最重要的 prompt design technique。

### 六、結語：升級的是提問習慣，不是工具

呼應 QA 那篇：

> QA 在重做他們的 schema 來適應 AI；你 RD/PM 該重做的是**對 AI 的提問習慣**。
>
> 工具不會自動帶來品質——**懷疑帶來品質**。AI 拿掉了 QA 那層內建的懷疑，你得自己補上。

可選收尾：
- 連結到 PDT Coach / Self-Review Agent（如果工具已上線）
- **預告**即將上線的 notest 篇（給 QA 的 schema 補篇）：「**awareness 在這篇、tooling 在下一篇**」——這篇開腦、下一篇給工具

---

## 跟姐妹篇的關係

QA 那篇 + 這篇形成**三角的兩個邊**：

- **QA 升級欄位設計**（schema） → [notest-ambiguity-skip-vs-low-confidence](notest-ambiguity-skip-vs-low-confidence.md)
- **RD/PM 升級提問習慣**（prompts） → 這篇
- **AI 工具填補中間**（PDT Coach / Self-Review Agent） → [tools-roadmap.md](tools-roadmap.md)

這篇是 PDT Coach 推廣給 RD/PM 的**合理性背書文章**——讓 RD/PM 自己意識到「我需要 QA 思維」之後，工具的價值才會被理解。

---

## 寫作前還沒解決的

- [ ] 主標題太長（「你以為...其實它在...」格式），考慮拆成短主標 + 副標
- [ ] 第五節 PM 特化要不要獨立成篇？（PM 跟 RD 看 AI 測試結果的角度其實差很多）
- [ ] 三個問題的順序——目前是 scope → confidence → skip，但「skip」放最後可能力道最強，要不要重排？
- [ ] 結語要不要直接 push PDT Coach？還是只暗示「需要外部工具」、不點名？取決於發稿時 PDT Coach 是不是已經能用
- [x] ~~觸發條件：等 notest 上稿後再啟動~~ → **改為先於 notest 上稿**（2026-05-13 訂）：awareness（這篇）→ tooling（notest）→ 配合 [accountability-checklist](ai-replacement-accountability-checklist.md) 形成「問題 → 責任 → 工具」三連發弧線

---

## 一句話定位

> 你以為你請了一個 QA，其實你請了一個 Yes Man——而 Yes Man 不會告訴你他在敷衍你。**這篇給你三個問題，逼出 AI 沒告訴你的那一半**。
