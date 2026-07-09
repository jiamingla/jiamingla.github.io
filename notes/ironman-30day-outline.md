# 鐵人賽 30 天 Outline（IT 管理主題競賽向，2026-07-09 草）

> 主題：**QA 走向組織 / 管理——一個測試工程師的「看懂局」30 天**。對齊 endgame（RD Head-style QA Head）、差異化最強（QA×管理幾乎沒人寫）、素材最厚。
> 標記：`[骨架]`＝skeletons-active 已有、`[已發可改寫]`＝從已上稿延伸、`[buffer✅]`＝已轉成 _drafts、`[缺]`＝要新寫。
> ⚠️ 每天目標字數降一檔（800-1500），求「持續」不求「深度」。開賽前先存 7-10 篇 buffer。

---

## 週一（Day 1-6）：立論——QA 為什麼該有組織視角

| Day | 題目 | 來源 |
|---|---|---|
| 1 | 開場：一個測試工程師，為什麼開始看「局」而不只看 bug | [缺] 序 |
| 2 | 問題驅動測試（PDT）：把「提問」從測試對象搬到組織 | [已發可改寫] problem-driven-testing-intro |
| 3 | **可測試性是「治理問題」不是「技術問題」** | [buffer✅] testability-is-governance |
| 4 | 「無主之地」：公司裡那些沒人的 KPI 涵蓋的品質破口 | [骨架] bug-triage-pm-turnover-cost / product-line-doc-maintenance-orphan |
| 5 | 老闆要的不是綠燈，是心安 | [已發可改寫] qa-report-workplace-wisdom |
| 6 | 週回顧 + 一個小結（維持節奏、低負擔日） | [緩衝日] |

## 週二（Day 7-13）：bug 治理與 PM-QA 介面

| Day | 題目 | 來源 |
|---|---|---|
| 7 | 你的團隊 bug 預設給誰？六種 triage 模式 | [已發可改寫] bug-triage-six-patterns |
| 8 | 公司把 bug 當資產還是負債？ | [骨架] bug-triage-pm-turnover-cost（航空業 framing） |
| 9 | bug 管理是一門專業，但它不是任何人的 KPI | [骨架] bug-management-is-a-profession-pm-gap |
| 10 | 我想成為讓「PM 交付給 QA 的品質」變穩定的人 | [骨架] pm-qa-interface-structured-workflow |
| 11 | PM 更像客戶關係管理，不是同事 | [骨架/coach 7/03] 衍生角度 |
| 12 | 產品線文件的孤兒工作：沒人的 KPI，卻是 schema 資產 | [骨架] product-line-doc-maintenance-orphan |
| 13 | 週回顧（低負擔日） | [緩衝日] |

## 週三（Day 14-20）：AI 時代的 QA 組織

| Day | 題目 | 來源 |
|---|---|---|
| 14 | AI 找 locator、人定 oracle：一個單兵的 AI 分工中場報告 | [骨架] ai-finds-locator-human-defines-oracle |
| 15 | pass/fail 對 AI 還夠用嗎？（結果 schema） | [已發可改寫] pass-fail-not-enough-for-ai-testing |
| 16 | 可維護性 = AI 要修改的最小單位有多小 | [骨架] maintainability-is-ai-min-edit-unit |
| 17 | 技術上「理論最優」為何敗給「組織現實」 | [骨架] theory-optimal-loses-to-org-reality |
| 18 | AI 當 yes man：RD/PM 信任校準 | [已發可改寫] ai-as-yes-man |
| 19 | 醫院電子化是 AI 導入的鏡子：陣痛是常態 | [骨架/_drafts] hospital-emr-mirrors-ai-adoption |
| 20 | 週回顧（低負擔日） | [緩衝日] |

## 週四（Day 21-27）：診斷、看懂局、實戰

| Day | 題目 | 來源 |
|---|---|---|
| 21 | 「App 壞了」常常是誣賴：從後端到 GPU 的診斷分層 | [buffer✅] app-broken-is-misattribution |
| 22 | flaky 不是隨機，是資訊：一個社群頁閃退偵探 | [骨架] flaky-is-information-not-randomness |
| 23 | 本地能跑、CI 不能：多半是環境差異 | [骨架] local-runs-ci-fails-environment-diff |
| 24 | 回歸 vs 冒煙：從對方的角度 steelman | [骨架] facing-overwhelm-via-steelmanning |
| 25 | 一套框架測 N 個 App：框架是常數、adapter 是變數 | [骨架/已發延伸] white-label / POM |
| 26 | 對的工具用錯時機（大人學/DOD） | [已發可改寫] right-tool-wrong-time |
| 27 | 週回顧（低負擔日） | [緩衝日] |

## 週五（Day 28-30）：收束——從執行者到定義者

| Day | 題目 | 來源 |
|---|---|---|
| 28 | 難量化的能力，怎麼變成看得見的形狀 | [骨架/coach] 難量化≠沒價值 |
| 29 | 小團隊 QA 與「新創第一位測試工程師」的 endgame | [骨架] small-team-qa-content-and-startup-endgame |
| 30 | 收：一個測試工程師的「看懂局」30 天學到什麼 | [缺] 結 |

---

## 缺口盤點（哪幾天沒現成料、要新寫）

- **Day 1（序）、Day 30（結）**：純新寫，但這兩篇最好留到最後、由 30 天內容長出來。
- **緩衝日（6/13/20/27）**：刻意放低負擔（週回顧 / 讀者問答 / 一張圖），對抗撞牆期。
- 其餘 24 天**全部有骨架或已發文可改寫**——素材夠，主要工作是「轉寫 + 降字數 + 去識別」。

## Buffer 轉寫優先序（開賽前存 7-10 篇）

1. ✅ testability-is-governance（Day 3 旗艦）
2. ✅ app-broken-is-misattribution（Day 21）
3. ai-finds-locator-human-defines-oracle（Day 14）
4. maintainability-is-ai-min-edit-unit（Day 16）
5. theory-optimal-loses-to-org-reality（Day 17）
6-7. flaky / local-runs-ci（Day 22-23）

> ⚠️ 去識別：Day 3/14/16/17/21/22/23/25 全出自 smoke 專案、**指紋最重**，轉寫務必抽象化（設計系統/一個列表很重的 App/一間理財 App 公司…）。
