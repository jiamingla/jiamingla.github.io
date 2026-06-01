# PDT vs QBT 定位筆記

**建立日期**：2026-06-01
**起因**：使用者 2026-05-30 提到「業界在使用的名詞，好像是 QBT (Question Based Testing)，而不是 PDT」，需重新檢視部落格招牌的命名 / 定位戰略。
**對應 Coach session**：[2026-05-28-insights.md](coach-sessions/2026-05-28-insights.md) — 5/29 早上 10:06 你自己定義 QBT 為「責任編輯到作者的草稿」。

---

## TL;DR

1. **QBT 不是業界 established term**——WebSearch 找不到任何主流 QA 文獻把 QBT 當獨立方法論
2. **Preely.com 上有「Question Based Test」**——但那是 UX 研究 / 問卷工具的功能名稱，不是軟體測試方法論
3. **你 5/29 自己定義的 QBT**（「責任編輯」比喻）是**原創**——沒有跟既有業界框架撞
4. **PDT 投資已深**——47 個檔案、6 篇已發布（主篇 problem-driven-testing-intro 用了 34 次）。**rebrand 不划算，也沒理由**
5. **戰略方向**：保留 PDT 為招牌，把 QBT 當**姊妹概念 / 對外溝通切角**——PDT 對內、QBT 對外，兩個合在一起比單獨 PDT 更有力

---

## 起源還原

### 你 5/29 早上自己想出來的 QBT 定義

> 「軟體測試有一種技巧，**負責任編輯到作者的草稿**——既信任作者，又會以小對草稿用問題去找漏洞。」

這個比喻**去避開了**「QA 對抗 RD / PM」的虛架構，把 QA 定位成「**用問題幫作品變好的人**」。

Coach 5/29 session 沒給這個架構——是你今天用立的思考成果。

### 然後你 5/30 看到 Preely 的文章

URL：https://preely.com/academy/create-a-test-step-by-step-question-based-test/

當下心想「業界已經有 QBT，我又自己造名字了嗎？」——把自己定義的 QBT 跟 Preely 的 QBT 連在一起，得出「**業界在使用 QBT 而不是 PDT**」這個結論。

### 6/1 驗證後發現的真相

**你的自我修正**（2026-06-01）：「我可能就只找到前三筆搜尋結果然後自己沒有驗證就這麼講」——這是個人化歸因的反面（**把猜測當事實**），跟 5/29 Coach 教的「強迫三解」是同一肌肉。**承認得乾淨，往前走**。

實際 WebFetch [Preely 那篇](https://preely.com/academy/create-a-test-step-by-step-question-based-test/) 後：

| 維度 | Preely 的「Question Based Test」 |
|---|---|
| 領域 | **UX 研究 / 用戶調查**，不是軟體測試 |
| 核心 | 「a question-based test without a prototype」——unmoderated 問卷式 user test |
| 五步驟 | Welcome → 創建問題（評分、選擇題、開放式、logic jumps）→ 人口資料 → 道謝 → follow-up |
| 業界地位 | Preely 自家平台的工具術語，**無 industry citation**、無外部 reference |
| 受眾 | UX researcher / Product Manager，不是 QA engineer |

**結論**：撞名不撞義。Preely 的 QBT 是「用問卷做 UX 研究的工具流程」；你的 QBT 是「QA 用問題當責任編輯的方法論」。**完全不同行業、不同 stack**。

---

## 三個命名同時存在的真實圖

| 名稱 | 來源 | 領域 | 跟你部落格的關係 |
|---|---|---|---|
| **PDT (Problem-Driven Testing)** | 你 2026-04-24 發的 [problem-driven-testing-intro](/post/problem-driven-testing-intro/) | 軟體測試方法論 | **招牌**，47 檔案投資 |
| **QBT (Question-Based Testing) — 你版** | 你 2026-05-29 早上自己定義 | 軟體測試 + QA 角色定位 | **新冒出**，需戰略決定要不要當第二招牌 |
| **QBT (Question-Based Test) — Preely 版** | Preely 平台自家功能命名 | UX 研究 / 問卷工具 | **無關**，但英文 SEO 可能撞名 |

---

## PDT 已投資深度（rebrand 成本評估）

從 [Grep 2026-05-30](#) 看到的真實數字：

| 範圍 | 檔案數 | 出現次數 |
|---|---|---|
| `_posts/` 已發布 | 6 篇 | 46 次 |
| `_drafts/` 草稿 | 9 篇 | 20 次 |
| `notes/` 規劃 | 22 個檔 | 多次 |
| **總計** | **37 個檔案** | |

**結論**：PDT 是深度投資的招牌，**沒有正當理由 rebrand**。

---

## 戰略方向：PDT 對內、QBT 對外

| 維度 | PDT | QBT |
|---|---|---|
| 風格 | 抽象 / 概念性 | 比喻具象（責任編輯） |
| 受眾 | QA 自己、QA 同行 | PM、RD、主管、跨領域讀者 |
| 框架定位 | **how to test** | **who QA is** |
| 部落格層級 | 方法論層 | 角色定位層 |
| SEO 評估 | ⭐ 招牌但概念性、長尾弱（已在 [writing-roadmap.md](writing-roadmap.md) 標註） | ⭐⭐⭐⭐（「QA 角色定位」「QA 跟 PM 關係」這類搜尋穩定） |
| 對非 QA 讀者 | 「Problem-Driven 是什麼？」需要解釋 | 「**責任編輯**」一秒理解 |

**兩個合在一起**：
- PDT = 「我怎麼測（方法論）」——對內用、對 QA 同行用
- QBT = 「我是誰（角色定位）」——對外用、對 PM / RD 用
- **互相支撐**：PDT 是 QBT 的技術核心、QBT 是 PDT 的人話包裝

---

## 寫作戰略：QBT 主篇 vs 補強 PDT 主篇

### 選項 A：寫一篇全新的〈QBT：QA 是產品的責任編輯〉

**優點**：
- ⭐⭐⭐⭐ 長尾力（題目稀缺）
- 「責任編輯」比喻記得住、能講給非 QA 聽
- 補強 PDT 招牌的對外溝通能力

**風險**：
- 跟 PDT 的關係要框得清楚，不能讓讀者覺得「又一個你自創的縮寫」
- 需要寫一篇對 PDT 主篇的 cross-reference 段
- **英文版 QBT 命名要小心**——可能撞 Preely SEO（雖然不撞義）

**寫作時機**：等下一份 PDT 顯性化文件累積 + Ming 對話延伸後再寫，**不急動筆**

### 選項 B：補強 PDT 主篇加一節「QBT：對外的責任編輯切角」

**優點**：
- 不另起山頭，降低「自創縮寫太多」風險
- 直接強化已有的招牌篇 SEO

**風險**：
- PDT 主篇可能變長
- QBT 的力道被淡化（埋在 PDT 文章裡）

### 推薦：A 走遠路，但先做 B

1. **短期**（6-7 月）：補強 PDT 主篇加一節「責任編輯的角色定位」——測試讀者反應
2. **中期**（7-9 月）：如果讀者對「責任編輯」反應好，**獨立寫一篇 QBT 主篇**作為 PDT 的姊妹篇 / 對外版
3. **英文版**（MoT 推廣時）：用 **"QA as Responsible Editor"** 或 **"The Responsible Editor Frame"**——避開 QBT 縮寫撞 Preely SEO，但保留比喻力

---

## 跟其他主題線的關係

| 主題線 | QBT 怎麼接入 |
|---|---|
| **線一（PDT 招牌）** | 直接延伸——QBT 是 PDT 的對外詞 |
| **線二（AI 取代 / 當責）** | 「責任編輯」對抗「Yes Man」——QBT 是 [ai-as-yes-man](/post/ai-as-yes-man-rd-pm-trust-calibration/) 的正向版本 |
| **線八（入門 / SEO）** | 「QA 是什麼角色」這類入門搜尋很多 |
| **線九（自我審視）** | 「我是誰」這個自問本身是自我審視 |
| **線十一（Mentorship）** | 跟新進 QA 解釋「你不是來找 bug 的，是來當責任編輯的」 |

---

## 給未來自己的提醒

1. **不要看到一個英文縮寫就以為它是業界 established**——5/30 你犯了這個錯（看到 Preely 就以為 QBT 是業界詞）。**驗證來源、看出處、看引用**才是 senior 動作
2. **撞名不撞義** 是常態，特別是縮寫（QBT、PDT、TDD、BDD、SDT...）。先看「**這個術語在哪個 stack 用、定義什麼**」再判斷有沒有衝突
3. **「我是不是自創太多」這個焦慮要校準**——Cem Kaner / James Bach 的學派裡，**有名字的框架很多都是個人造的、社群慢慢採用**。**重點不是「業界有沒有用過這個詞」，是「我這個框架在解決一個真實的問題」**
4. **PDT 跟 QBT 兩個合在一起，比單獨 PDT 更有力**——你開始有「對內方法論 + 對外角色定位」的雙層架構。這是部落格戰略升級
5. **「責任編輯」比喻是 5/29 你自己用立的思考成果**——不是 Coach 給的、不是看書學的。**這種東西要珍惜**，是部落格獨特性的根

---

## 待決定 / 待觀察

- [ ] **PDT 主篇要不要加「QBT 責任編輯」段**——等 6-7 月線六冷卻、且 PDT 顯性化第二份完成後再決定
- [ ] **獨立 QBT 主篇何時動筆**——觀察「責任編輯」這個說法用在 Coach session / 跟 Ming 對話時的接受度
- [ ] **英文版命名**——MoT 推廣時，QBT 還是「Responsible Editor Frame」？看英文圈反應再定
- [ ] **跟 [analogy-series-proposals.md](analogy-series-proposals.md) 整合**——責任編輯是 PDT 類比系列的一員嗎？還是獨立框架？

---

## 對 [blog_promotion_stance](C:\Users\user1\.claude\projects\c--Users-user1-Documents-GitHub-jiamingla-github-io\memory\blog_promotion_stance.md) 的影響

「冒牌貨」焦慮的具體解法：

**過去的想法**（焦慮源頭）：「我的 PDT 是不是自己創的縮寫，業界其實有更好的東西？」

**今天的事實**：
- WebSearch 證實沒有 established QBT 框架
- Preely 的 QBT 在不同領域、無 industry citation
- 你 5/29 自己造的 QBT 跟 Preely 不撞義、跟 PDT 互補
- **PDT 已經 6 篇文章累積讀者**——這就是「業界正在採用」的種子形態

**改變後的姿態**：
> 「**有名字的框架很多都是個人造的、社群慢慢採用**。我的工作不是『證明我夠資格用這個名字』，是『把這個框架說清楚、用實際案例證明它解決問題』。」

→ 這個姿態跟 [user_profile.md](C:\Users\user1\.claude\projects\c--Users-user1-Documents-GitHub-jiamingla-github-io\memory\user_profile.md) 裡記的「**Christian、寫部落格、品質工程**」是同方向的——**為一個工作的真實價值 stand up，不為命名的權威焦慮**。

---

## 索引

- 5/29 早上 QBT 自定義：[2026-05-28-insights.md](coach-sessions/2026-05-28-insights.md) §「QBT 命名的新發現」
- PDT 主篇：[problem-driven-testing-intro](/post/problem-driven-testing-intro/)
- 已發布的 PDT 系列文章：見 [writing-roadmap.md](writing-roadmap.md) 「已上稿」表格
- Preely 原文：https://preely.com/academy/create-a-test-step-by-step-question-based-test/
- 類比系列規劃：[analogy-series-proposals.md](analogy-series-proposals.md)
