# 軟體測試的第一性原理（探索檔）

**建立**：2026-06-01
**狀態**：🌱 骨架——只記元素跟 mapping，**不展開內容**，等想清楚再寫
**起源**：6/1 重新檢視部落格方向、把今天 surface 的所有 piece 拉到元層級時冒出的問題

---

## Candidate 第一性原理（待你校準 / 改寫）

> **軟體永遠 partial、人對它的期待永遠 partial、真實使用永遠 partial——測試 = 主動顯影三方 gap 的人類動作。**

「partial」這個詞中文化 candidate：**不完整 / 片面 / 局部 / 不可窮盡**。

---

## 三方 partial 的具體展開（待精緻化）

| Partial | 具體內容 |
|---|---|
| **軟體本身的 partial** | 程式有 unknown behavior、無法窮舉 state、edge case 永遠多於設想 |
| **人對軟體期待的 partial** | spec / 需求 incomplete、PM / RD 認知有限、設計階段假設不全 |
| **真實使用的 partial** | user 真實情境永遠 exceed 設想、極端使用者行為 unknowable in advance |

→ Tester = **calibrate 這三方 gap 的人類角色**。

---

## 既有文章 → derivative mapping（這篇寫好 = 整合 5 個月所有招牌）

| 方法論 | 是 first principle 的哪個面向 |
|---|---|
| [PDT](/post/problem-driven-testing-intro/) | 用問題**主動探**三方 gap |
| **QBT（責任編輯）** | 替**作者**看 gap（角色定位版） |
| **比較表 prototype** | expected vs actual = gap 顯影機制 |
| [spec-maintenance](/post/spec-maintenance-gray-zone/) | spec 是 partial → 需要 maintain（不是寫完就結束） |
| [yes-man](/post/ai-as-yes-man-rd-pm-trust-calibration/) | AI 是 partial 認知 → 不能 outsource judgment |
| [boredom-is-a-signal](/post/boredom-is-a-signal/) | 自動化判讀的 gap signal |
| **PM-QA 介面結構化** | gap 在 spec → test 中間 |
| [black-box-limitations](/post/black-box-limitations-and-strategy/) | 黑箱 = 從外部 partial 看 gap |
| [rethinking-regression](/post/rethinking-regression-test-value/) | 老 regression = 對 gap 結構認知過時 |
| [10-minute-test-plan](/post/ten-minute-test-plan-when-test-stage-down/) | ACC = gap 系統化 mapping 工具 |
| **AI test case 閱讀瓶頸** | gap 在「AI 預設讀者」vs「真實 QA reader」 |

→ **這篇寫好 = 把上面 10+ 篇 reduce 到一個元 framework**。

---

## 對照既有 thought leader

| 人 | 他的 first principle 主張 |
|---|---|
| **Cem Kaner** | "empirical investigation, 給 stakeholders 之前沒有的 quality info" |
| **James Bach** | "testing = questioning a product"（你 PDT 接近這派） |
| **Glenford Myers** | "executing with intent of finding errors"（過時 bug-finding 派） |
| **你的 candidate** | **Kaner + Bach 合流 + 加上「三方 partial」structure** |

→ 你的獨特 contribution 在「**三方 partial**」這個 structure（既有派多停在 information / questioning 層、沒明確切出 partial 對象）。

---

## 對未來文章的影響

如果這個 first principle 確立，未來寫作會有兩種可能：

| 方向 | 描述 | 影響 |
|---|---|---|
| **A. 元 framework 為主、其他文章變註腳** | 這篇成為 hub，其他 derivative 文章在文末 cite hub | 部落格 architecture 整合度大幅提升 |
| **B. 元 framework 是 background, 不主動 highlight** | 內化在所有文章背後、不顯性化 | derivative 各自獨立、framework 隱性傳達 |

→ A 對招牌建立更強、但 risk 是讀者覺得「太抽象、跟具體工作脫節」。B 更穩、但缺少元層級的可記憶 anchor。

---

## 對鐵人賽的可能延伸（與既有 A / 升級版 / I 並列當第四 option）

鐵人賽方向**第 4 個 option**: **「軟體測試第一性原理 30 天」**：
- W1: 排除錯誤候選（找 bug / 驗需求 / 品質保證 / 自動化）
- W2: 引入「三方 partial」frame
- W3-W4: 每個既有方法論作為 derivative 重講
- W5: 對 AI 時代 QA 的意義

→ 跟 A（PDT 純方法論）、升級版（PDT × PM-QA 結構化）、I（自審日記）並列，**但這個 option 主題抽象度最高、最考驗 30 天能否撐住**。

---

## 開場 rabbit hole（待擴展）

文章可能的開場 hook（5 個為什麼）：

```
為什麼測試？→ 找 bug
為什麼找 bug？→ 確保品質
品質是什麼？→ 符合期待
期待從哪來？→ spec / 使用者
spec 跟使用者期待一樣嗎？→ 不一樣，partial...
```

→ 5 個為什麼之後落到「**三方 partial 的 gap**」。

---

## Open questions（給未來自己想，不在這份檔展開）

- [ ] 「partial」中文怎麼翻最 punchy？不完整 / 片面 / 局部 / 不可窮盡？
- [ ] 「人對期待」vs「真實使用」這兩個 partial 是同一個還是兩個？要不要 collapse？
- [ ] 這篇要在鐵人賽前發、還是當鐵人賽 anchor 篇開場？
- [ ] 跟 PDT 主篇的關係：取代 / 升級 / 並列？
- [ ] AI 時代怎麼影響這 framework？AI 是新一方 partial、還是放在現有三方裡？
- [ ] 「主動」這個詞 vs「被動發現」——tester 的 active stance 要不要 framework 化進去？

---

## 跟其他線的關係

| 線 | 連動點 |
|---|---|
| 線一 PDT | **這篇是 PDT 招牌的元層級** |
| 線二 AI literacy | AI 進來是新一方 partial（或加深既有 partial） |
| 線四 測試紀律 | 所有方法論都 derivative |
| 線八 入門 SEO | 「軟體測試 first principle」「軟體測試 是什麼」長尾 |
| 線十三 書評 | 對話 Kaner / Bach / Myers 的天然題目 |

---

## 索引

- 對照 thought leader 引用待 verify：Kaner、Bach 出處（《Lessons Learned in Software Testing》/ Context-Driven 學派文獻）；Myers 出處（《The Art of Software Testing》）
- 跟既有文章的 mapping 上面表格已列
- 鐵人賽 endgame 連結：[ithome-ironman-2026-planning.md](ithome-ironman-2026-planning.md)
- 跟 PDT / QBT 戰略：[pdt-vs-qbt-positioning.md](pdt-vs-qbt-positioning.md)
