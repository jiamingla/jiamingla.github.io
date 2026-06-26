# PM-QA 介面結構化工作流

**建立**：2026-06-01
**狀態**：🌱 骨架——只記元素，**不展開內容**，等想完整再寫
**起源**：6/1 重新檢視部落格方向時 surface 的具體題目；借 Medium「結構化工作流」frame；結合 5/28 RD Head-style QA Head 願景

---

## 核心 idea

「**讓 PM 交付給 QA 變穩定的那個人**」——這個 role 是 6/1 clarified 的 endgame（**RD Head-style QA Head**：高度與產品綁定 + 大量參與會議 + 下去帶 QA 完成）的**具體 manifest**。

---

## 為什麼這題站得住（活案例已有）

- **5/30** PM Cassie 主動找你流程改革（不知怎麼寫文件給 QA）
- **5/29** Head 警告「PM 文件本質寫不全」
- **連動既有方法論**：[spec-maintenance](/post/spec-maintenance-gray-zone/) + [yes-man](/post/ai-as-yes-man-rd-pm-trust-calibration/) + 比較表 prototype + PDT 招牌

---

## 借用的 frame：Medium 〈結構化工作流〉

[原文連結](https://medium.com/@ymwkac/如何用-結構化工作流-解決低效的團體協作-291a759dec1c)

核心：
- **三策略 A/B/C**：被動配合 / 完全孤立 / 結構化異步化（推 C）
- **4 個方法**：唯一信任源文件 / 帶方案來敲門 / 異步溝通 / 客觀指標
- **金句**：「衡量協作能力 = 是否成功降低團隊溝通成本」

---

## 6/1 補充的雙向受害 reframe（user surface）

**不是「QA 被 PM 拖累」單向，是雙方都被 scope creep 打散**：

| 角色 | 面試以為 | 進來發現 |
|---|---|---|
| QA | 測 APP | APP + 其他 product / API / 跨團隊 |
| PM | 當 APP PM | 事情很雜、不能只專注 APP |

→ PM 文件品質參差**不是個人能力問題**，是雙方都被組織 scope 打散。

**這個 reframe 對文章的重要性**：把議題從「**責怪 PM**」翻成「**兩個 scope creep 受害者一起 build 防線**」——對 PM 同情、對自己解套、對讀者好 share。

---

## 三策略 A/B/C 的 QA 版（待擴展）

| 策略 | QA 版描述 | 代價 |
|---|---|---|
| A 被動 chase | 等 PM 給 / 給什麼測什麼 | 漏測回吃 QA |
| B 孤立腦補 | 自己拆需求、PM 後補資訊重 work | 重工 + 跟 PM 隔閡 |
| C 結構化 | 主動定 schema + checklist + 異步 review | 前期投資、後期高 ROI |

---

## 4 個方法 QA 化（待擴展）

| 原文 | QA 版 |
|---|---|
| 唯一信任源文件 | spec template（明確欄位 / 必填 / fall-through） |
| 帶方案來敲門 | PM 不確定時給兩種 schema 選，不是空白 |
| 異步溝通 | 用 PR review / Notion comment 流程 review PM 文件 |
| 客觀指標 | spec 完整度 checklist 評分 |

---

## Article outline（一篇深寫版）

1. 痛點開場：PM spec 一直長不一樣
2. Reframe：不是 PM 不會寫、是雙方被 scope creep、PM-QA 沒共同 schema
3. 三策略 A/B/C（QA 版）
4. 4 個方法 QA 化
5. 第一步行動：下個 ticket 寫 spec template
6. PDT 連結：結構化過程本身就是 PDT（用問題定義文件長什麼樣）

---

## 對鐵人賽的可能延伸（待想、不在這份檔展開）

A 方向「PDT 30 天」**可升級成「PDT × PM-QA 介面結構化 30 天」**：
- W1: 痛點 + 雙向 scope creep reframe（case study）
- W2: 三策略 A/B/C 深寫
- W3: 4 個方法展開
- W4: 工具 / template 實作
- W5: PDT × QBT × 結構化整合

→ 等鐵人賽方向定案後再決定 single article / SEO 輕量化系列 / 鐵人賽 spine。

---

## 對 Coin framing 的直接武器

quote 原文一句給 Coin：
> 「**衡量協作能力 = 是否成功降低團隊溝通成本**」

對 Coin 講「我在做的事是**降低 PM-QA 溝通成本**」比「我想參賽」強 10 倍——work-relevant、不是個人累積。

---

## Open questions（待想，不在這份檔展開）

- [ ] 公司指紋：寫太具體 PM-QA 場景、會洩 Cassie / Head / Lead 嗎？洗到多抽象？
- [ ] 跟 spec-maintenance / yes-man / 比較表互引（避免重複、找差異點）
- [ ] 對 Coin / Head 的具體 framing
- [ ] single article / 輕量化系列 / 鐵人賽 spine 三選一

---

## 跟其他線的關係

| 線 | 連動點 |
|---|---|
| 線一 PDT | 結構化過程**本身就是 PDT** |
| 線二 AI literacy | PM 用 AI 寫文件**更需要** schema |
| 線五 自動化決策 | spec template 是 schema 化的具體實踐 |
| 線六 大人學 | 雙向 scope creep 同理 reframe |
| 線八 入門 SEO | 「PM QA 文件 範本」長尾關鍵字 |
| 線十三 書評 | 借 Medium「結構化工作流」frame、可作對話型書評切入點 |

---

## 索引

- Medium 原文：[如何用「結構化工作流」解決低效的團體協作](https://medium.com/@ymwkac/如何用-結構化工作流-解決低效的團體協作-291a759dec1c)
- 對應 Coach session：[2026-05-28-insights.md](coach-sessions/2026-05-28-insights.md)（5/29 Head「PM 文件寫不全」+ 5/30 Cassie 主動找）
- 鐵人賽 endgame 連結：[ithome-ironman-2026-planning.md](ithome-ironman-2026-planning.md)（6/1 RD Head-style QA Head clarified）
