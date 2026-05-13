---
urlname: bug-triage-six-patterns-industry-survey
title: 你的團隊 Bug 預設給誰？業界六種主流 Triage 模式對照
date: 2026-09-15 22:00:00
tags: [軟體測試, Bug 治理, 跨團隊協作, 組織設計, 入門, QA, PM, 品質工程]
---

> ✏️ 這是一篇種子稿。素材來源：2026-05-13 為線十「無主之地」做業界 survey 時浮現，發現 survey 本身就值得獨立成篇。

---

## 預設讀者（2026-05-13 確定）

**主要讀者：QA**——但 PM / Tech Lead / EM 等任何設計 bug workflow 的角色都讀得進去。

預設讀者**沒意識到自己的團隊在哪個 pattern**——只覺得「我們團隊就這樣」。文章要做的事是：**讓他能定位自己、看到代價、知道有別的選擇**。

**SEO 角度**：「bug triage」「bug 指派」「bug 預設」是穩定的入門關鍵字，這篇的長尾流量值會比論述文高。

---

## 寫作風險備忘

低風險（這是業界 survey 不是公司內部觀察）：

- **不點名自家團隊**（Pattern A：PM 預設）為「最差 pattern」——介紹時保持中性，講出 A 的合理場景
- Pattern A 的優缺點要平衡寫，不要當稻草人；自家團隊看到不會覺得被點名

---

## 緣起

2026-05-13 寫線十時，user 問到「業界主流預設是什麼？」我整理出六種 pattern + 七種 backlog 處理實作，發現：

1. **業界沒有單一最佳解**——六種並存就是證據
2. **七種 backlog 實作全是 workaround**（bug bash 是 surge / bankruptcy 是放棄 / Fix-it Friday 是定期掃除）
3. **這個 survey 本身就值得獨立成篇**——SEO 流量會比線十兩篇加起來都高

---

## 文章主結構（草擬）

### 一、開場：你的團隊 bug 預設給誰？

讓讀者先回答這個問題再讀下去——把文章變成「**自我定位指南**」。

可能的開頭：

> 你的團隊收到一個新 bug 的時候，預設 assignee 是誰？  
> 是 PM？Tech Lead？QA？還是「未分派」？  
> 你可能從來沒問過這個問題——它就是這樣，預設是繼承來的。  
> 但這個「預設」靜悄悄決定了三件事——你的 backlog 會怎麼長、**誰會 burn out**、哪些 bug 永遠不會被修。

### 二、六種主流預設指派 pattern

完整對照表 + 各自代表場景：

| Pattern | 預設給誰 | 適用場景 | 優點 | 缺點 |
|---|---|---|---|---|
| **A. PM 預設** | Product Manager | B2C 消費型、product-led 組織 | 商業優先級準 | 缺技術深度估 severity / dedup |
| **B. Tech Lead 預設** | RD lead / 模組 owner | 工程主導 startup、infra team | 修復難度估得準 | 商業權重失衡 |
| **C. QA 預設** | QA team / QA lead | 金融、醫療、enterprise 高合規 | dedup / severity calibration 一致 | **QA 變 default janitor** |
| **D. Unassigned queue** | 任何人 pick up | Open source、客服中心 | load 平均 | **無主之地 / bug 老化** |
| **E. Triage Committee** | 每週跨部門會議 | 中大型公司（MS / Google 經典） | 顯式 ownership | meeting 開銷大、bug 等下次會議 |
| **F. Component / CODEOWNER** | 程式區域 owner | 大型 codebase | domain expertise | 跨模組 bug 卡住 |

每個 pattern 各寫 2-3 段：典型公司型態、會被什麼問題反噬、**你怎麼認出自己在這個 pattern**。

### 三、七種「處理 backlog」的實作（workaround 級）

| 實作 | 邏輯 | 局限 |
|---|---|---|
| **Bug bash** | 釋出前團隊集中獵 bug、有時帶獎勵 | 釋出前 surge capacity，**不解 backlog** |
| **Bug bankruptcy** | 定期把 N 天以上未處理 bug 全 close | 真 bug 被殺、**假信號** |
| **Zero bug policy** | bug 24-48h 內必 triage | 需專職時間 |
| **Severity-only triage** | 只看 S1 / S2，S3 / S4 永遠在 backlog | paper cuts 累積、體驗折損 |
| **Fix-it Friday / Bug-fix sprint** | 每隔 N sprint 撥時間清 backlog | 治標、不改流程 |
| **SLA-based response** | 客戶報的有 response SLA，內部報沒有 | **二級制度**、內部 bug 餓死 |
| **Embedded QA / shift-left** | QA 跟 dev team 同坐、開發中即時 triage | 需組織結構改造 |

**重點 framing**：這七種**沒有一個真正解決問題**——它們都是 workaround。**業界至今沒有結構性的 backlog 治理共識**。

### 四、為什麼沒有銀彈

論述橋樑：bug backlog 是「**四角色（客服 / RD / PM / QA）混合語料**」（呼應線十的結構性洞察 #2）——

- 客服寫情緒體驗、RD 寫 stack trace、PM 寫影響範圍、QA 寫測試紀錄——**很少有人類同時讀得流利這四種語言**
- 所以哪個 pattern 都會 fail 在某一面：A 不懂技術語言、B 不懂客戶語言、C 把 QA 累壞、D 沒人讀
- **唯一的結構性出路是換工具，不是換 pattern**

這節是文章銜接到「為什麼需要 AI 補位」的橋樑——如果跟線十兩篇配對發，這節就是 setup。

### 五、定位自己 + QA 的生存指南

不管哪個 pattern，QA 通常會被當 default janitor。給 QA 三個策略選擇：

1. **抵抗**：把自己的角色講清楚——「我不是 default assignee」（要主管支持，難度高）
2. **改革**：推動 pattern 切換（中型團隊有機會，大公司困難）
3. **妥協 + 自救**：接受角色，但**用工具減負**（這條接線十的 AI 補位論點）

### 六、結語

> 業界沒有一個 bug triage pattern 是完美的。但選擇 pattern 不是隨機——**它反映你的組織是用什麼語言在思考品質**。
>
> 知道自己在哪個 pattern，至少能**停止把組織問題當成自己的問題**。

---

## 跟其他線的關係

| 主題線 | 關係 |
|---|---|
| **線八（入門 / 長尾 SEO）** | 本篇主場 |
| **線十（無主之地）** | 本篇是線十的入門前傳——讀者先讀本篇定位，再讀線十看 AI 補位的合理性 |
| **線六（職涯 / 大人學）** | 第五節「QA 生存指南」有 overlap |

---

## 寫作前還沒解決的

- [ ] 每個 pattern 的具體公司案例——可以引用哪些公開 case？需要研究（Atlassian / Google / Microsoft 的 engineering blog）
- [ ] Pattern A 的中性化——自家團隊在 A，寫的時候要保持中立、不貶低
- [ ] 第六節結語的「組織用什麼語言思考品質」這句要展開還是收住？
- [ ] 與線十的發稿先後——本篇可以**先於線十兩篇上稿**（當入門引子帶流量），也可以**後上**（當深度延伸的回頭課）。哪個對 SEO 比較好？
- [ ] 文章長度——六種 pattern + 七種 workaround，全展開可能太長。要不要把 workaround 那節壓成精簡版、把「為什麼沒有銀彈」加重？

---

## 一句話定位

> 業界沒有銀彈 bug triage 模式——但你知道自己在哪個 pattern，至少能**停止把組織問題誤認成個人問題**。
