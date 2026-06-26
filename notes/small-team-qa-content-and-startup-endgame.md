# 規模維度盲點 + 單兵/小團隊 QA 內容線 + 「新創第一位測試工程師」職涯願景（戰略檔）

**建立**：2026-06-17
**狀態**：🌱 戰略檔——內容 gap + 新職涯願景，待發展成具體文章 + 鐵人賽方向
**起源**：6/17 user 跟資深學長（新創、4 人團隊）吃飯，發現**寫了 20 篇、只有 yes-man 能分享給他**——其餘都預設「大組織」脈絡、對小團隊幫不上。同時 surface 職涯願景：**兩三年後想成為新創的第一位測試工程師**。
**對應主題線**：線十二（單兵 QA 自動化，[sole-qa-bottom-up-automation](sole-qa-bottom-up-automation.md)）為主場 + ai-era Gap 5（中文圈方法論稀缺）

---

## 戰略 gap：20 篇裡 19 篇預設「大組織」

**為什麼**：user 的 lived experience 全在大公司 → 每個觀察自帶「有 PM/RD 分工、有主管層級、有跨部門政治、有 N 個 APP 規模」的預設。對 4 人新創全不存在（一人多角、需求在老闆腦裡、沒人逼你、沒有無主之地因為就那幾人）。

**yes-man 能分享的原因 = 線索**：它的主詞是「**AI**」不是「組織」。
→ **越靠 AI / 思維 / 第一性原理 = 越跨規模；越靠組織 / 人 / 政治 = 越鎖大公司。**

---

## 規模維度 lens：哪些線通用 vs 哪些被大組織鎖死

| 對小團隊**通用**（AI / 思維 / 哲學） | 被**大組織鎖死**（組織 / 人 / 政治） |
|---|---|
| 線一 PDT（思維、不靠規模） | 線六 大人學 / 向上管理（預設主管層級） |
| 線十二 單兵 QA 自動化（**本來就為這個**） | 線十 無主之地 / bug 治理（4 人哪來無主） |
| first-principle、驗證哲學（跨規模） | PM-QA 介面 schema（預設專職 PM） |
| 線二 AI literacy（小團隊更依賴 AI） | 回歸 vs 冒煙配置（預設有人壓你） |
| yes-man（**唯一學長能用的**） | bug 標題指南 / 六模式（預設多人協作） |

---

## 重點 reframe：既有大主題出「小團隊版」（不是補新題、是換脈絡）

| 大組織版（已寫 / 在寫） | → 小團隊 / 新創版（空白） |
|---|---|
| 無主之地：3000 個 bug 沒人管 | 4 人團隊 bug 根本沒流程，**要不要建？還是憑感覺** |
| PM-QA 介面 schema | 沒有 PM、需求在老闆腦裡，**QA 怎麼問出驗收條件** |
| 回歸 vs 冒煙（主管壓力） | 新創沒人逼你，**你自己怎麼決定測到哪就夠** |
| 單兵 QA 自動化（線十二） | **這條線就是答案**——只是還沒動筆 |
| bug 治理六模式 | 4 人團隊的 bug 就丟一個 channel，**怎麼不漏** |

---

## 🟢 你已經有單兵實證了：smoke 框架（2026-06-17）

> 今早焦慮「我沒單兵作戰經驗、不知道哪些能寫」——**但你手上的 smoke 框架就是單兵實戰**：

- 一個人（「發想與維護：Elijah」）設計一套服務 **7 個 APP、4 種架構**的冒煙框架、共用 `pages/` 一行未改（`AutoTesting/Author/smoke_script/`，去識別版 [smoke-test-golden-set-spec](smoke-test-golden-set-spec.md)）
- 「給 AI 半小時調定位器、人工 review」= 單兵 + AI 的真實工作法
- **這比大多數「新創第一位 QA」更硬的單兵實戰**——你不是沒經驗、是還沒意識到這就是那個經驗

→ 寫單兵 / 小團隊文時，**這套框架是你最強的第一手素材**（去識別後）。連 [writing-without-lived-experience](writing-without-lived-experience-honest-stance.md) 的「能寫 vs 別硬寫」：smoke 框架是 ✅ 能寫的真實經驗，不是推演。

---

## 🛠️ 願景的工程版宣言（6/17 user surface）：「1 個是能力、20 個是工程，我願意試」

> 「管理好一個 APP 的自動化測試腳本是做得到的，但管理好二十個是工程挑戰——我也願意去嘗試看看。」

這句把抽象願景落成**具體的工程動作**：

| 規模 | 性質 | 對應 |
|---|---|---|
| 管好 **1 個** APP 自動化 | **個人能力**（已證明：回歸腳本、單一 app） | 執行者 |
| 管好 **20 個** | **工程挑戰**——逼出的不是「更努力測」、是「設計一套讓 20 個都被涵蓋的系統」 | **定義者 / 架構者** |
| **「我願意去嘗試」** | = 願意從執行者走向定義者 | **這就是 mission statement 的動作、是在選那條路** |

**為什麼這句重要**：
- 「1 是能力、20 是工程」這個切分很準——**規模逼出系統設計**，而系統設計正是 Head / 新創第一位 QA 的核心（不是「測更多」、是「設計涵蓋的架構」）
- 正面回答 6/17 早上「**修一個 bug 怎麼驗 20 個 APP**」（成本難 × N）——「管好 20 個」就是那題的解
- 20 個規模下，「**AI 找 locator、人決定預期結果**」這條分工線才真正划算（1 個自己做還好、20 個非分工不可）——smoke 框架（7 app）已是這個工程的進行式
- **這是願景跟現況的接點**：不必等到去新創，「從 1 到 N 的規模化」現在的 smoke 框架就在練

---

## 🎯 職涯願景：新創的第一位測試工程師（6/17 新 surface）

> user：「單兵策略就是我想寫的，我也算期待兩三年後能夠成為新創的第一位測試工程師。」

### 跟 6/1「RD Head-style QA Head」endgame 的關係（待釐清、別急著解）

| | 6/1 endgame：RD Head-style QA Head | 6/17 endgame：新創第一位測試工程師 |
|---|---|---|
| 組織規模 | 大組織 | 小團隊 / 新創 |
| 角色 | 帶人、規模化、product-embedded leadership | 單兵、一人多角、從零建造 |
| 政治 | 高（跨部門、向上管理） | 幾乎無 |
| 接的位置 | 接 Head 的椅 | 全新白紙 |

**看似衝突，但 reconcile 很漂亮——而且兩條本質是同一套能力（user 6/17 點出）**：

**共同點（兩個 endgame 都需要、都在練）**：
- **看懂局**（讀組織 / 產品 / 政治的真實結構）
- **破局思維**（不被現狀框住）
- **跟不同人交涉的能力**（PM / RD / 主管 / 老闆）
- **帶人**——**「第一位測試」意味著後續是這個第一位去招、去帶第二位**。所以新創第一位 QA **不是永遠單兵**，是「**從零 founder QA 職能 → 帶第二、第三位**」= **從白紙長出來的 Head**

→ **兩個 endgame 不是分岔、是同一套能力、不同起點**：
| | 大組織 QA Head | 新創第一位測試工程師 |
|---|---|---|
| 起點 | 接 Head（Ming）的椅、繼承既有團隊 | 白紙、從零蓋 QA 職能 |
| 終點 | 帶人、調度、product-embedded | **一樣帶人**（招並帶第二位）、定義整間公司品質 |
| 共同能力 | 看懂局 + 破局 + 跨人交涉 + 帶人 | 同左 |

- 補充：新創第一位也是**「定義者」最純形態**（沒遺留流程 / 政治、從白紙定義品質）——貼 mission statement「從執行者升級成定義者」（[ai-era-tw-qa-needs](skeletons-active/ai-era-tw-qa-needs.md)）
- **這正是「別把對方定格、人會成長」用在自己身上**（連 [facing-overwhelm](skeletons-active/facing-overwhelm-via-steelmanning-regression-vs-smoke.md)）——endgame 在演化，但**核心能力不變、所以現在練的不會白費**

→ **好消息**：因為兩條共用能力，**現在不必急著二選一**——你在大組織練的「看懂局 / 破局 / 交涉 / 帶人」，去新創一樣用得上。8 月底心理體檢時定的是「**起點選哪個**」、不是「能力練哪套」（能力同一套）。

---

## niche 機會（⚠️ 2026-06-17 查證後大幅下修，別當藍海）

> 🔍 **查證紀錄**：user 提醒「別在沒驗證前宣稱藍海」（QBT/Preely 那課）。WebSearch 後結果↓——**「單兵 / 新創第一位 QA」根本不是藍海**。

| 語圈 | 真實狀況 |
|---|---|
| **英文** | **完全飽和**。專文一堆（Codacy / Codemify / 11Sigma / BrowserStack / Muuktest「0 budget」/ DEV「Lone QA Engineer」）+ 書《The QA Advantage》。**而且 framing 跟我們發想的撞**：「不只是 tester、是 shaping quality culture」（=定義者）、「small incremental improvements 建信任」（=影子工程師）、「8-12 工程師才招第一個 QA」、Playwright/API first |
| **中文** | **較薄、但不空白**。有職涯介紹型（換日線〈12 年職涯錦囊〉含新創、GoFreight QA 經驗、叡揚職涯手冊），**少有「AI 時代 × 單兵建造方法論」的深度** |

**真正的護城河不是「題目」、是「組合」**：
- 「單兵 QA」topic 不原創（英文寫爛了）——它是**載體**、不是 moat
- 真正稀缺 = **繁中 × AI 時代 × PDT 招牌 × 第一性原理/驗證哲學 × 個人敘事（水電工/Holes）** 的組合。**topic 撞沒關係，角度跟聲音不撞**
- **英文那些文章是資產**：像引用 DavidKo 一樣讀它們、站在肩上寫繁中 AI 版，**別假裝自己第一個想到**

**動筆前要做的**（同 QBT/Preely 紀律）：
- 先讀 2-3 篇英文的（Codacy / Codemify roadmap / Muuktest 0-budget），確認我的角度跟它們的差異、可引用佐證
- 中文版的差異點明確標：AI 時代 + PDT + 繁中個人敘事，不是「教你怎麼當第一個 QA」（那英文有了）

**參考來源（動筆前讀）**：
- [Codacy: First QA Engineer in a Startup](https://blog.codacy.com/first-qa-engineer-in-a-startup)
- [Codemify: QA Startup Success Roadmap](https://codemify.com/qa-startup-success-roadmap)
- [Muuktest: Build QA at a Startup, 0 Budget 5 Engineers](https://muuktest.com/blog/build-qa-startup-no-budget)
- [Medium: Build QA with Only 1 Developer and 0 Testers](https://medium.com/qevolution/how-i-would-build-a-qa-process-in-a-startup-with-only-1-developer-and-0-testers-a4060427aa58)
- 中文：[換日線〈12 年軟體測試工程師職涯錦囊〉](https://crossing.cw.com.tw/article/19008)

---

## 對鐵人賽的影響（連 [ithome-ironman-2026-planning](ithome-ironman-2026-planning.md)）

- 鐵人賽方向多一個強候選：「**單兵 / 小團隊 QA 的 30 天**」（線十二）
- vs 之前的 IT 管理（大組織）/ SD / 佛心分享——**單兵主題受眾更廣、更差異化、且對齊新 endgame**
- 若職涯往「新創第一位測試工程師」走，**鐵人賽寫單兵 = 提前打造那個身份的 portfolio**
- 待 8 月底心理體檢一起定：IT 管理（接大組織 Head）vs 單兵（接新創定義者）——**鐵人賽主題該對齊哪個 endgame**

---

## 連動

| 連動 | 關係 |
|---|---|
| [sole-qa-bottom-up-automation](sole-qa-bottom-up-automation.md) | 線十二主場——單兵自動化的具體戰術，這檔是它的戰略傘 + 職涯框架 |
| [ai-era-tw-qa-needs](skeletons-active/ai-era-tw-qa-needs.md) | Gap 5 niche + mission statement「定義者」 |
| [ithome-ironman-2026-planning](ithome-ironman-2026-planning.md) | 鐵人賽方向 + endgame |
| [facing-overwhelm](skeletons-active/facing-overwhelm-via-steelmanning-regression-vs-smoke.md) | 「人會成長（含自己）」用在 endgame 演化 |
| yes-man（[/post](/post/ai-as-yes-man-rd-pm-trust-calibration/)） | 唯一跨規模通用的既有文——示範「靠 AI 主詞 = 跨規模」 |

---

## 待答

- [ ] **endgame 釐清**（8 月底）：大組織 QA Head vs 新創第一位測試工程師——序列、還是二選一？
- [ ] 第一篇小團隊文寫哪個？（傾向線十二既有的「單兵第一個月：悄悄進行的影子自動化」——已有骨架）
- [ ] 鐵人賽主題：單兵 30 天 vs IT 管理 30 天——對齊哪個 endgame
- [ ] 「既有大主題出小團隊版」要系統化做（每篇配一個小團隊版）、還是隨機長？
- [ ] 要不要在 [writing-themes](writing-themes.md) 加「規模維度」當貫穿所有線的 lens（本檔是那個 lens 的詳述）
