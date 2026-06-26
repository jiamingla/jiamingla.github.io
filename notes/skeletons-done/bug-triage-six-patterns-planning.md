# 【寫作規劃】bug-triage 六種模式對照——素材、揭露邊界與待思考問題

> 📂 **這是 meta 規劃檔,不是文章本身**(2026-06-08 從 `source/_drafts/` 移來)。
> 文章會在揭露邊界想清楚後**另外生成**到 `source/_drafts/bug-triage-six-patterns-industry-survey.md`。
> 兩者刻意做出差異:**這份**放素材、決策、待答問題;**那篇**才是要發布的成品。
>
> 素材來源:2026-05-13 為線十「無主之地」做業界 survey 時浮現,發現 survey 本身就值得獨立成篇。

---

## 🔑 2026-06-08 的策略轉折(讀者必先看)

原本定位:**純業界 survey**(低風險,因為「不是公司內部觀察」)。

新決定:**用兩間「前公司」的真實處理流程當第一手錨點 + 業界 survey 補其餘**。

這個轉折是**雙面刃**,務必意識到:

- ✅ **更強**:第一手經驗比引用 Atlassian / Google blog 更稀缺、更有可信度,「我真的在這兩種 pattern 裡待過」是別人抄不走的 angle
- ⚠️ **更危險**:第一手公司流程的**可識別性遠高於**抽象 survey。原本「低風險」的前提**不再成立**——揭露邊界從此是這篇的 gating decision
- 🚧 **現公司**:Pattern A(PM 預設)難去識別化,傾向**不寫現公司**,只用兩前公司 + 業界其他四格

相關紀律:memory [feedback_person_names_in_notes](C:\Users\user1\.claude\projects\c--Users-user1-Documents-GitHub-jiamingla-github-io\memory\feedback_person_names_in_notes.md)(新內容用 pseudonym / role label)、roadmap 對 [cross-app-locator-strategy](cross-app-locator-strategy.md) 的「含公司指紋、blog 化需洗」註記。

> 🟢 **2026-06-08 gating 通過**:揭露邊界五題已答(見下方 A 組)。可識別性不是阻力(本就要放 LinkedIn)、無情緒包袱、現公司不寫、流程講抽象。**可進入文章生成**,剩下 B / C / D 是寫作工藝決策、非擋路石。

---

## ❓ 需要你好好思考的問題

### A. 揭露邊界 ✅ 已定案（2026-06-08）——gating 通過

| # | 問題 | 決定 |
|---|---|---|
| 1 | 兩間前公司各落在哪個 pattern？ | **兩間都是 F + E 的組合**：按 component / owner 分派（F）+ 每週團隊內跨職能會議（E 輕量版，cross-functional team、非跨部門大委員會）推動。⚠️ **2026-06-08 修正**：原寫「C（QA 第一手）+ F + E」，但使用者對「QA 是否第一手收 bug」沒把握 → **拿掉 C**。前公司只示範 F+E；C（QA 預設）那格改用業界高合規 case、不掛自己。文章三處已改 |
| 2 | 會不會被反推出是哪間？ | **不擔心**——本來就打算放 LinkedIn，去識別化不是阻力 |
| 3 | NDA / 營業秘密？ | **講抽象一點即可**——保持流程層級，不帶具體工具 / 數字 / 專案名 |
| 4 | 對前公司有情緒嗎？ | **沒有**——中立性風險低，不會變「抱怨前東家」 |
| 5 | 現公司寫不寫？ | **不寫**（選 a 完全不提）——文章不含現公司，不缺這段 |

> 🟢 **gating 通過**：五題全綠燈，可以生成文章。

**A1 的意外收穫（要寫進文章）**：兩間前公司都不是「純 pattern」，而是 **F + E 的組合**。這正好**印證文章核心論點**——「業界沒有單一最佳解、純 pattern 是簡化、真實世界都是混合制」。第一手案例不只是 anchor，更是論點的活證據。

**對結構的連帶影響**：
- 第一手錨點 = 兩間前公司的 **F + E 組合**（按 component 分派 → 團隊內跨職能會議推動）；**不宣稱 QA 第一手**（沒把握）
- C（QA 預設）那格 + A. PM 預設 / B. Tech Lead / D. Unassigned，全改用業界公開 case 補（見 B 組問題 7）
- 現公司（原本的 A：PM 預設）**整段拿掉**——「自我定位指南」框架改由「我待過的 F+E 組合 vs 業界其他模式」承載，不依賴現公司

### B. 第一手 vs 二手怎麼編織

6. **主從**:兩間前公司是「主菜」還是「佐證」?整篇變回憶錄 vs survey 為骨幹、前公司當 2 個 anchor case 嵌進對照表
7. **補格**:前公司案例放進六格的哪兩格?剩下四格用業界公開 case(Atlassian / Google / Microsoft engineering blog)補——哪些 case 可引用?需要研究
8. **稻草人風險**:第一手經驗會讓「保持中性、不當稻草人」更難(原始備忘第 22-28 行已提醒 Pattern A 的中性化)。前公司那兩格更要刻意寫出優點

### C. 標題 / 定位的差異化(meta 檔 vs 未來文章)

9. **標題分流** ✅:這份規劃檔用 meta 標題,未來文章保留催讀標題〈你的團隊 Bug 預設給誰?〉
10. **定位微調** ✅:文章定位微調為「我待過的 F+E 組合 vs 業界其他模式」,SEO 主關鍵字保住
11. **Triage 中文備註** ✅(2026-06-08):「Triage 不是中文 QA 常見詞」→ (a) 標題改〈業界六種主流 **Bug 分派(Triage)** 模式對照〉;(b) 前言加 gloss 段落,說明 bug triage = bug 分派 / 分流,後文兩詞交替使用。呼應 memory [feedback_word_choice_xuepiian](C:\Users\user1\.claude\projects\c--Users-user1-Documents-GitHub-jiamingla-github-io\memory\feedback_word_choice_xuepiian.md)

### D. 原本就還沒解決的(保留)

11. **發稿先後**:本篇可**先於**線十兩篇(當入門引子帶流量),也可**後於**(當深度延伸的回頭課)。哪個對 SEO 比較好?
12. **長度控制**:六 pattern + 七 workaround 全展開可能太長。要不要把 workaround 那節壓成精簡版、把「為什麼沒有銀彈」加重?
13. **結語收放**:第六節「組織用什麼語言思考品質」這句要展開還是收住?

---

## 📦 素材庫(未來文章的原料,先別當定稿)

### 預設讀者(2026-05-13 確定)

**主要讀者:QA**——但 PM / Tech Lead / EM 等任何設計 bug workflow 的角色都讀得進去。

預設讀者**沒意識到自己的團隊在哪個 pattern**——只覺得「我們團隊就這樣」。文章要做的事是:**讓他能定位自己、看到代價、知道有別的選擇**。

**SEO 角度**:「bug triage」「bug 指派」「bug 預設」是穩定的入門關鍵字,長尾流量值比論述文高。

### 緣起的三個發現

1. **業界沒有單一最佳解**——六種並存就是證據
2. **七種 backlog 實作全是 workaround**(bug bash 是 surge / bankruptcy 是放棄 / Fix-it Friday 是定期掃除)
3. **這個 survey 本身就值得獨立成篇**——SEO 流量會比線十兩篇加起來都高

### 六種主流預設指派 pattern

| Pattern | 預設給誰 | 適用場景 | 優點 | 缺點 |
|---|---|---|---|---|
| **A. PM 預設** | Product Manager | B2C 消費型、product-led 組織 | 商業優先級準 | 缺技術深度估 severity / dedup |
| **B. Tech Lead 預設** | RD lead / 模組 owner | 工程主導 startup、infra team | 修復難度估得準 | 商業權重失衡 |
| **C. QA 預設** | QA team / QA lead | 金融、醫療、enterprise 高合規 | dedup / severity calibration 一致 | **QA 變 default janitor** |
| **D. Unassigned queue** | 任何人 pick up | Open source、客服中心 | load 平均 | **無主之地 / bug 老化** |
| **E. Triage Committee** | 每週跨部門會議 | 中大型公司(MS / Google 經典) | 顯式 ownership | meeting 開銷大、bug 等下次會議 |
| **F. Component / CODEOWNER** | 程式區域 owner | 大型 codebase | domain expertise | 跨模組 bug 卡住 |

每個 pattern 各寫 2-3 段:典型公司型態、會被什麼問題反噬、**你怎麼認出自己在這個 pattern**。
→ 其中兩格將改用前公司第一手案例填(見問題 A1、B7)。

### 七種「處理 backlog」的實作(workaround 級)

| 實作 | 邏輯 | 局限 |
|---|---|---|
| **Bug bash** | 釋出前團隊集中獵 bug、有時帶獎勵 | 釋出前 surge capacity,**不解 backlog** |
| **Bug bankruptcy** | 定期把 N 天以上未處理 bug 全 close | 真 bug 被殺、**假信號**。**QA 情緒代價**（2026-06-08 加，源自現職、通用化寫）：不修「一個」PM 很容易，但一次宣告幾百個破產，對 QA 是「我記錄這些有沒有意義」的動搖；長期養出「反正會被清就別認真記」的心態。假信號是雙向的（對上騙管理層、對下消耗 QA 信任）。文章已寫進第二節 |
| **Zero bug policy** | bug 24-48h 內必 triage | 需專職時間 |
| **Severity-only triage** | 只看 S1 / S2,S3 / S4 永遠在 backlog | paper cuts 累積、體驗折損 |
| **Fix-it Friday / Bug-fix sprint** | 每隔 N sprint 撥時間清 backlog | 治標、不改流程 |
| **SLA-based response** | 客戶報的有 response SLA,內部報沒有 | **二級制度**、內部 bug 餓死 |
| **Embedded QA / shift-left** | QA 跟 dev team 同坐、開發中即時 triage | 需組織結構改造 |

**重點 framing**:這七種**沒有一個真正解決問題**——它們都是 workaround。**業界至今沒有結構性的 backlog 治理共識**。

### 論述橋樑:為什麼沒有銀彈

bug backlog 是「**四角色(客服 / RD / PM / QA)混合語料**」(呼應線十的結構性洞察 #2)——

- 客服寫情緒體驗、RD 寫 stack trace、PM 寫影響範圍、QA 寫測試紀錄——**很少有人類同時讀得流利這四種語言**
- 所以哪個 pattern 都會 fail 在某一面:A 不懂技術語言、B 不懂客戶語言、C 把 QA 累壞、D 沒人讀
- **唯一的結構性出路是換工具,不是換 pattern**

這節是文章銜接到「為什麼需要 AI 補位」的橋樑——如果跟線十兩篇配對發,這節就是 setup。

### QA 生存指南(第五節素材)

不管哪個 pattern,QA 通常會被當 default janitor。給 QA 三個策略選擇:

1. **抵抗**:把角色講清楚——「我不是 default assignee」(要主管支持,難度高)
2. **改革**:推動 pattern 切換(中型團隊有機會,大公司困難)
3. **妥協 + 自救**:接受角色,但**用工具減負**(這條接線十的 AI 補位論點)

### 候選結語

> 業界沒有一個 bug triage pattern 是完美的。但選擇 pattern 不是隨機——**它反映你的組織是用什麼語言在思考品質**。
>
> 知道自己在哪個 pattern,至少能**停止把組織問題當成自己的問題**。

---

## 跟其他線的關係

| 主題線 | 關係 |
|---|---|
| **線八(入門 / 長尾 SEO)** | 本篇主場 |
| **線十(無主之地)** | 本篇是線十的入門前傳——讀者先讀本篇定位,再讀線十看 AI 補位的合理性 |
| **線六(職涯 / 大人學)** | 第五節「QA 生存指南」有 overlap |

---

## 未來文章的 frontmatter 草案(生成時搬進 _drafts/,date 改實際發布日)

```yaml
urlname: bug-triage-six-patterns-industry-survey
title: 你的團隊 Bug 預設給誰？業界六種主流 Triage 模式對照
date: <實際發布日>
tags: [軟體測試, Bug 治理, 跨團隊協作, 組織設計, 入門, QA, PM, 品質工程]
```

候選開頭:

> 你的團隊收到一個新 bug 的時候,預設 assignee 是誰?
> 是 PM?Tech Lead?QA?還是「未分派」?
> 你可能從來沒問過這個問題——它就是這樣,預設是繼承來的。
> 但這個「預設」靜悄悄決定了三件事——你的 backlog 會怎麼長、**誰會 burn out**、哪些 bug 永遠不會被修。

一句話定位:

> 業界沒有銀彈 bug triage 模式——但你知道自己在哪個 pattern,至少能**停止把組織問題誤認成個人問題**。
