# PM 流動率的 bug backlog 成本（待思考）

**建立**：2026-06-10 之後（6/10 [〈你的團隊 Bug 預設給誰？業界六種 Bug 分派模式對照〉](/post/bug-triage-six-patterns-industry-survey/) 上稿後現場 surface）
**狀態**：🌱 骨架——記 observation + 兩個 framing 選項，**等思考完再決定深寫哪個**
**起源**：上稿後注意到一個 6/10 文章沒寫的 hidden cost——「Pattern A（PM 預設）」搭配「PM 流動率不低」會出現 routing knowledge 不穩、backlog 質量受 PM 任期影響的二級 fail mode

---

## 核心 observation（user 自己 surface）

> 「這裡不只 QA 會報很多 bug、客服 / RD / PM 自己也會報很多。這些目前預設都是 assign 給 PM，但 **PM 的流動率不低**，我其實也困惑什麼是最佳解。」

### Thesis-level framing：bug list 資產 vs 負債（**對話後深化**）

> 「我覺得這其實很看整個團隊是否把 bug list 看為一種資產而不是負債。」

→ 這是 sequel 的 **thesis-level** framing（比「Pattern A 二級 fail mode」深一層）：

| 視角 | bug list 是 | 對應動作 | 對應 6/10 文章的 pattern |
|---|---|---|---|
| **Liability 派** | technical debt 的具體形式 | 清掉就好 → bankruptcy 合理 | Bug bankruptcy workaround 的 cultural root |
| **Asset 派** | user feedback corpus + domain knowledge + quality signal + tacit routing knowledge | 清掉 = discarding partial information | 任何 pattern 配 archival + indexing |

**這個 framing 直接連 [first-principle](software-testing-first-principle.md)「三方 partial」**：bug = software partial 的 evidence。Liability 派 = discarding partial 證據；Asset 派 = preserving 證據用來 calibrate 後續 gap。

### PM 交接的 4 種真實 pattern（user 觀察、上稿後現場 evidence）

| 交接方式 | bug 怎麼處理 | 對 backlog 質量影響 |
|---|---|---|
| **不交接** | 幾百個不知道狀態的 bug 留在 backlog | 隨時間累積成 zombie inventory |
| **離職前一次性全關**（bug bankruptcy 個人版） | 「彼此交接少了點負擔（大概）」 | 6/10 文章寫過：真 bug 被殺、假信號、QA 情緒代價 |
| **調部門但仍可 follow** | 後續還能找到原 PM 問 / 或重新 assign 給對的人 | 中——routing knowledge 半保留 |
| **離職且無 handover** | bug routing knowledge 隨人走 | 最差——backlog 質量隨 PM 任期長短不一致 |

→ **6/10 文章寫了 Bug bankruptcy 的 fail mode、沒寫為何會發生**——這 4 種 pattern 解釋了 hidden trigger：**交接成本 + PM turnover 是 bankruptcy 的 hidden cause**。

### 「管好 bug 是誰的 KPI」——organizational root cause

> 「管好 bug 是誰的 KPI、這裡我可以去問問看 Head。」

連到 [2026-05-12-insights.md](coach-sessions/2026-05-12-insights.md)「**不是部門績效**」洞察——但升級到 KPI 層：**沒人被 measure on bug backlog quality → 必然無主之地**。

這是線十「無主之地」框架的 **organizational root cause**——之前的 framing 停在「沒人天然該收這個 inbox」，但更上一層是「**沒人的 KPI 包含這件事**」。

### 🛫 Aviation 安全文化類比（**sequel 的主 thesis 升級**）

> **起源**：user 看完 YouTube〈[四個小錯誤，炸掉半個互聯網【讓編程再次偉大#40】](https://youtu.be/eF0SFyCGWlg)〉後 surface 的更深層 framing。
>
> User 原話：「**那幾百個 bug 其實屬於重大事故、真正值得記錄下來的其實很少**……後端 / 運維 bug（像影片提到的 AWS 事故）不在我目前 QA 部門範圍、有點可惜。」

#### 為什麼 aviation framing 比 PM turnover 升一級

| 維度 | PM turnover sequel（原 skeleton） | **Aviation framing**（升級版） |
|---|---|---|
| Thesis 層級 | organizational fix | **culture critique**（行業層級） |
| 公司指紋 risk | 中（易讀「我們公司」） | **無**（純行業論述） |
| SEO cluster | bug triage 長尾 | **「軟體 QA 安全文化」「post-mortem」「incident review」**新 cluster |
| 跟 6/4 reflection 連動 | 弱 | 強——「**接近組織不是工程**」+「**資產 vs 負債**」的具體 manifestation |
| 跟 first-principle 連動 | 中 | **強**——「三方 partial」直接對應「incident 是 archival evidence、bulk close = discarding partial」 |

#### 行業文化對比

| 維度 | 航空業 | 軟體 QA（目前） |
|---|---|---|
| 重大事故 review | 強制（regulatory、IATA / FAA） | 通常只 PIR、且只看 outage |
| 事故分類 framework | 完整（incident / accident / serious incident / precursor） | **無**——所有 bug 同類 |
| Archive 文化 | 公開、行業共享、進入規範 | bulk close + bankruptcy |
| Investigation 標準 | 跨組織、強制 root-cause | 視團隊文化、無強制 |
| 學習機制 | AAR（After Action Review）系統化 | 視團隊、無系統化 |

→ **Sequel 新 thesis**：「**軟體 QA 需要一個 incident classification framework、區分『真事故』vs『noise』、才能有 archival 文化。沒有分類就沒有 archive、沒有 archive 就無從學習——這正是 Bug bankruptcy 被視為「正常做法」的真實 root cause。**」

#### 對 PM turnover 維度的影響

PM turnover 不必當主軸、但可以保留為 **supporting case**：
- 「PM 一次清掉 backlog」是因為**沒有 incident classification**——清掉跟 archive 沒區別
- 航空業若 PM-equivalent role 換手不會 bulk close incident report、因為**那些是行業資產**
- → 揭露 PM turnover 在 aviation framing 裡 **變成「症狀」、不是「病因」**——更安全 + 更深

### 候選文章標題（user surface 後給未來自己挑、不急）

| # | 標題 | 風格 / 強項 |
|---|---|---|
| 1 | 〈軟體 QA 沒有航空業的事故 review 文化：為什麼 Bug bankruptcy 變成「正常」做法？〉 | 對照型 + 問題開門、SEO 中等 |
| 2 | 〈四個小錯誤、半個互聯網——軟體業缺的不是技術、是事故分類的文化〉 | 呼應影片標題、數字 hook、最抓眼球 |
| 3 | 〈Bug list 是資產還是負債？從航空業看軟體 QA 的盲點〉 | 短、SEO 友善、thesis 直接放標題 |
| 4 | 〈「真正值得記下來的其實很少」：為什麼軟體 QA 沒有 archival 文化？〉 | 用 user 自己的反思當 hook、最 authentic |
| 5 | 〈我們把 backlog 當垃圾、航空業把 incident 當教材——軟體業缺的事故分類學〉 | 對偶句、有 punch、narrative drive |
| 6 | 〈Bug bankruptcy 是行業常態、但這是好做法嗎？航空業給 QA 的一堂課〉 | 質疑既有實踐、反思 tone |

→ 標題決定 thesis 強度：1/3 較收斂、2/5 較大膽、4 最 authentic、6 反思型。

### 6/10 文章寫了什麼 / 沒寫什麼（updated）：

| 維度 | 6/10 文章 |
|---|---|
| Pattern A「PM 預設」的基本 fail mode：缺技術深度估 severity / dedup | ✓ |
| Pattern A 的**二級 fail mode：PM 流動率 → routing knowledge 不穩 → backlog 質量受 PM 任期影響** | ✗ |
| 四角色（客服 / RD / PM / QA）都是 bug originator | ✓（緣起的三個發現） |
| **不同 originator 的 routing 需求其實不同**（PM 報的 vs 客服報的） | ✗ |

→ 上稿後 surface 的這個 dimension、**是 6/10 文章的天然 sequel candidate**。

---

## 兩個 framing 選項（待你決定）

### Option A：Sequel——〈Pattern A 的 hidden cost：PM 流動率的 bug backlog 殺手〉

| 維度 | 評估 |
|---|---|
| SEO | ⭐⭐⭐（sequel 通常被 search engine cluster + 提升原文 ranking） |
| 寫作成本 | 低——context 已建（不用 re-explain Pattern A） |
| 讀者 pipeline | 高——6/10 文章 active reader 自然延伸過來 |
| 內部互引 | 強——6/10 文章可加 hook「續篇 sequel」 |
| 揭露邊界 risk | **中**——「PM turnover」在 Pattern A 框架裡是抽象的二級 fail mode、不必說是現公司 |
| 連動 | 線十「無主之地」+ 5/12 四角色 insight 自然延伸 |
| 風險 | 跟 6/10 文章框架綁定、framing 不能太離題 |

### Option B：獨立深度文——〈員工流動率是組織品質風險：bug backlog 的隱性吞噬〉

| 維度 | 評估 |
|---|---|
| SEO | ⭐⭐⭐（不同關鍵字池：「員工流動率 影響」「組織風險 品質」） |
| 寫作成本 | 高——要 re-build context、解釋 Pattern A 後再講 turnover |
| 讀者 pipeline | 中——招新 audience（PM / HR / 組織設計、不只 QA 圈） |
| 內部互引 | 弱——跟 6/10 文章關係要 explicitly 建立 |
| 揭露邊界 risk | 高——獨立框架難避開「我講的是現公司」 |
| 連動 | 跟更廣的議題（員工流動率對知識資產的影響）連動 |
| 風險 | 重新 setup context 成本高、可能 reader 覺得「跟 6/10 文章重複」 |

---

## 我的 take（不催）

**推薦 Option A（Sequel）**，理由：
1. 6/10 文章還新、reader pipeline active、續篇引流效益最大
2. PM turnover 在 6/10 文章框架裡是**天然二級延伸**、不是離題
3. 寫作成本最低（context 已建、framing 已 set）
4. 揭露邊界 risk **比 B 低**（抽象「Pattern A 的 PM turnover」vs 具體公司觀察）
5. 跟 [yes-man-sequel](yes-man-sequel-what-qa-still-owns.md) / [rethinking-regression-sequel](rethinking-regression-sequel-idea.md) 同一 sequel pattern（你已有這個 muscle）
6. **但 framing 要走「Pattern A 的二級 fail mode」**——強化 6/10、不 compete

### Option A 的揭露邊界提醒

6/10 文章決定「**現公司不寫**」——sequel 如果不小心、容易變成「我講現公司的 Pattern A 真實樣貌」。

**抽象化要點**（如果選 A）：
- 寫成「Pattern A 在高 turnover 環境下的二級 fail mode」、不寫「我們公司」
- 引用業界 PM turnover 數據（公開來源）當主 evidence、不用自己經歷
- 「最佳解」段用 framework 答（不用「我提議的解」、避免被讀成現公司提案）

---

## 候選 article outline（兩個 framing 都先草擬一版）

### A. Sequel outline

```
0. 開場：6/10 我寫了六種 pattern；上稿後我注意到一件事——
1. Pattern A 的基本 fail mode 簡述（既有讀者快速回顧、新讀者引到 6/10 連結）
2. 二級 fail mode：PM 流動率
   - Bug routing knowledge 是 tacit knowledge、跟人走
   - PM 換手 → routing decision 重 calibrate
   - Backlog 質量看 PM 任期長短不一致
3. 跨 originator 的 hidden complexity：四種人報 bug 都打到同一個 PM
4. 對 PM turnover 強的兩個方向
   - AI 補位（連 5/12 四角色語言中立 framework）
   - 混合 routing by originator
5. 結語：「實在是個好問題」——但這個好問題的存在本身就是 senior signal
```

### B. 獨立深度文 outline

```
0. 開場：員工流動率 ≠ 招募問題、是知識資產問題
1. 案例：bug routing 是 tacit knowledge——舉 Pattern A 為主例
2. 跨組織 turnover cost 的隱性吞噬（quote 業界研究）
3. 為什麼 bug backlog 對 turnover 特別敏感（tacit + cross-role mixed corpus）
4. 五個對 turnover 強的組織設計
5. 結語：HR 的指標 vs 品質的指標 = 同一個指標
```

---

## 連動到既有 framework

| 既有檔 | 連動點 |
|---|---|
| [bug-triage-six-patterns-planning](bug-triage-six-patterns-planning.md) | 原文規劃檔；sequel 寫好後在這檔末段加「續篇 idea」連結 |
| [pdt-coach-session-2026-05-12-insights](coach-sessions/2026-05-12-insights.md) | **「四角色語言混合 corpus + AI 跨角色中立」**是 sequel 第 4 節的論點 |
| [software-testing-first-principle](software-testing-first-principle.md) | sequel 可用「三方 partial」frame extended——routing knowledge 是另一方 partial |
| [pm-qa-interface-structured-workflow](pm-qa-interface-structured-workflow.md) | 「混合 routing by originator」可以連動 PM-QA 介面 schema |
| [analogy-series-proposals](analogy-series-proposals.md) | 沒直接連動 |

---

## 待答（綠燈時段想，不催）

- [ ] **Sequel vs 獨立**——選 A 還是 B？（我推 A、但你決定）
- [ ] **Thesis 升級**：sequel 要用「資產 vs 負債」當 thesis（**user 6/10 後 surface 的、比我原 outline 深一層**）、還是停在 outline 寫的「Pattern A 二級 fail mode」？傾向用 thesis-level、把 PM turnover 當論據之一
- [ ] **揭露邊界**——「PM turnover」即使抽象化，會被現公司同事讀成 in-house 觀察嗎？
- [ ] **AI 補位 vs 混合 routing**——sequel 的「對 turnover 強的方向」段、哪個深寫？
- [ ] **發稿時機**——上稿 6/10 後多久發 sequel 最 optimal？（建議 2-4 週、不超過 1 個月）
- [ ] **跟線十兩篇的關係**——sequel 是線十「無主之地」的 setup、還是 detour？

## 跟 Head 的 information gathering plan（6/1 disclosure strategy advisor approach B 風格）

「問 Head 管好 bug 是誰的 KPI」是純諮詢動作、**不徵求許可、不講 ambition、不主動推**。連動到 [ithome-ironman-2026-planning.md](ithome-ironman-2026-planning.md) 的 RD Head approach B 4 個切入問題。

**可問 Head 的 5 個問題**（一次 1-2 個、不集中問）：
1. 「我們公司 bug backlog quality 是誰的 KPI？還是沒有特定的人？」
2. 「PM 交接時、JIRA 上幾百個 bug 通常怎麼處理？有 handover SOP 嗎？」
3. 「你會把 bug list 看成資產還是負債？」（**最直接探 framing 對齊**）
4. 「Pattern A（PM 預設）的 fail mode 你怎麼看？特別是 turnover 維度」（如果他讀過 6/10 文章）
5. 「如果有人想 build 一個跨 originator 的 routing schema、你會建議從哪裡切入？」（半 disclose）

**Senior 動作標記**：「目前還沒找上我」+「我覺得有趣」這個自我覺察——對應 6/2「被看見會自然發生」mode。**不硬推、累積 framework**、等問題自然找上來。

## Self-awareness 觀察（user 自己標記）

> 「這種問題目前還沒找上我」+「我覺得這是有趣的工程挑戰」

對照模式：
- ❌「我要去推這個」（衝動模式——對應 5/31 200 行冒煙測試提案反例）
- ✅ user 的當前模式：**不硬推 + contemplate framework + 問 Head 累積 ground knowledge + 等問題自然找上來**

這跟 [2026-06-01-insights](coach-sessions/2026-06-01-insights.md) 的 6/2 IB 事件「被看見會自然發生」是同一肌肉。Sequel 寫作可以採同樣姿態——**不為了證明什麼而寫、是把 framework 留下來**。

---

## 跟其他線的關係

| 線 | 連動點 |
|---|---|
| 線八 入門 SEO | sequel 跟 6/10 文章共用 SEO cluster |
| 線十 無主之地 | sequel 是「為什麼需要 AI 補位」論點的 extra evidence |
| 線一 PDT | 「routing knowledge 是 tacit」呼應 PDT 招牌——隱性知識顯性化 |
| 線六 大人學 | 「員工流動率 vs 組織知識」這條（如果選 Option B）會落線六 |
| 線十三 書評 | 沒直接連動 |

---

## 索引

- 6/10 原文：[bug-triage-six-patterns-industry-survey](/post/bug-triage-six-patterns-industry-survey/)
- 6/10 規劃檔：[bug-triage-six-patterns-planning.md](bug-triage-six-patterns-planning.md)
- 5/12 四角色 insight：[2026-05-12-insights.md](coach-sessions/2026-05-12-insights.md)
- 線十 framework：見 [writing-themes.md](writing-themes.md) 線十段
- **Aviation framing 起源影片**：YouTube〈[四個小錯誤，炸掉半個互聯網【讓編程再次偉大#40】](https://youtu.be/eF0SFyCGWlg)〉（user 看完後 surface 升級 framing）—— 影片內容可能提到 AWS / Cloudflare / CrowdStrike 等具體 outage case，**寫作前要重看一遍取具體 case + 引用 timing**

## 待補的業界 incident case 素材（aviation framing 動筆前要 research）

寫 aviation framing 需要 1-2 個業界 incident case 當對照證據（不是 PM turnover）。建議候選：

| 案例 | 為什麼適合 |
|---|---|
| **AWS S3 outage 2017**（typo in command） | 經典「小錯誤大影響」、AWS 公開 post-mortem 是 best practice 範本 |
| **Cloudflare 2024 outages** | 「四個小錯誤」框架可能呼應、近期讀者熟 |
| **CrowdStrike 2024-07** | 全球 IT outage、影響範圍空前 |
| **Boeing 737 MAX**（aviation 反例） | 航空業也會失敗——當「culture is hard」對照 |
| **NASA Challenger / Columbia AAR** | 航空業 archival 文化的經典 demonstration |

→ 不必全寫，挑 1-2 個對比即可。先看 YouTube 影片找他用的 case 當主錨。
