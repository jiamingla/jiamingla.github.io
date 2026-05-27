---
urlname: frontend-ui-vocabulary-for-qa
title: QA 該認識的 31 個前端 UI 詞彙——從 AI 給我 skeleton loading 那天開始補的課
date: 2026-05-27 18:00:00
tags: [軟體測試, 前端測試, UI/UX, AI 測試, 跨領域學習, 品質工程]
---

> ✏️ 這是一篇種子稿。起源：2026-05-14 AI 給我的測試案例裡寫了 `skeleton loading`，我意識到對前端顯示效果 / 專有名詞的知識體系其實有缺口。
>
> **2026-05-25 framing 校準**：從「**後端 QA 補課**」改為「**QA 的前端 UI 視角**」——讓讀者群更廣（不只後端背景），也讓資深讀者讀得進去（focus 在「**每個詞彙背後的測試角度**」而非「定義」）。**對應 MoT 雙語發稿規劃**：中文版先發、1 週後做 adapted 英文版。

---

## 預設讀者（2026-05-25 校準）

**主要讀者**：任何 QA——不論測試經驗深淺、不論專精後端或前端。文章的價值不在「定義」，在「**每個詞彙背後的測試角度**」。

可能會特別有共鳴的讀者：
- 過去測後端居多、最近開始碰前端的人
- 開始用 AI 寫測試案例、發現 AI 用的詞彙自己不熟
- 工作環境慢慢往全端測試擴張
- 想升級「跟前端 / 設計溝通的詞彙」的人

**對資深讀者的訊息**（要寫進開場）：
> 「你可能已經知道這些詞彙——這篇的價值不是 definitions，是**第三欄『QA 該怎麼測』的 testing heuristics**。」

**SEO 角度**：「skeleton loading 測試」「toast notification QA」「frontend ui terms testing」這種搜尋是穩定長尾。

**MoT 英文版的差異化**（給未來自己）：
- Framing 改成 "**A tester's lens on frontend UI patterns**"——強調 testing heuristics 不是 vocabulary lookup
- 前提一句話 disarm senior readers：「You may already know some of these. The value isn't the definitions — it's the test heuristics in the third column.」
- 「最小生存集合」→ "starter kit" / "essentials"
- 「**PDT 的反向應用**」→ "**AI as a vocabulary mirror**" 或 "**reverse exploratory testing**"（不假設讀者懂 PDT 招牌）
- 「我都不知道」式自貶 → "I had to look this up too"（humble but not self-deprecating）

---

## 寫作風險備忘

低風險（技術知識型文章，沒個人觀察 / 同事 / 主管脈絡）：

- 不要寫成「**我都不知道**」的自我貶低調性——框架成「**業界詞彙比想像中多**」更專業
- 避免「前端比後端難」這種挑釁式比較——主軸是「**兩邊各有複雜度，我之前沒見過這層**」

---

## 緣起（可以直接當文章 hook）

2026-05-14，AI 給我一份自動生成的測試案例，裡面有這段：

> 「驗證列表載入過程中應顯示 **skeleton loading**，並在資料返回後平滑過渡到實際內容。」

我盯著「skeleton loading」這個詞看了三秒，**第一反應是「這是什麼」**。我做了好幾年 QA，跑過 API、debug 過 SQL、追過 race condition——但這個詞我沒有完整概念，只是隱約知道是「載入動畫的某一種」。

那一刻我意識到——**我從來沒問過自己這個專業詞彙缺口**。前端 UI 的整個詞彙體系（loading 狀態、用戶反饋、表單狀態、動畫術語...）我都是憑直覺看，沒有系統性學過，但是給AI的訓練資料有包含這些。我猜這不是只有我——**任何沒刻意盤點過前端 UI 詞彙的 QA，可能都有類似缺口**。

**AI 沒讓我學會 skeleton loading——AI 讓我看見我不知道有 skeleton loading 這個詞**。這正好是 [問題驅動測試（PDT）](/post/problem-driven-testing-intro/) 的反向應用：別人（AI）給的東西**暴露了你沒問過的問題**。

於是這篇文章想做的事——**把前端 UI 詞彙的最小生存集合整理出來，附上每個詞的測試角度**。

> ✏️ **給已經熟悉這些詞的讀者**：這篇的價值不是 definitions——是**每個詞彙底下「QA 該怎麼測」那欄的 testing heuristics**。如果你看到 skeleton loading 知道是什麼，可以直接跳到第三欄看「應該驗什麼」。

---

## 文章主結構（草擬）

### 一、開場：AI 給我一個我看不懂的測試案例

從「skeleton loading」這個具體詞彙切入。讓讀者立刻共鳴：「對，我也不確定自己懂這個詞」。

### 二、為什麼 QA 容易有這個缺口

- 後端測試的詞彙集中：API、status code、payload、idempotent、race condition、transaction、orchestration...
- 前端詞彙完全是另一套：loading states、user feedback、form states、animation timing、accessibility...
- **兩套詞彙幾乎不重疊**——背景偏一邊的 QA 自然很少接觸另一邊
- 過去 RD 分工清楚時，QA 也跟著只測自己熟的部分（**這不是後端 QA 獨有的問題——前端背景 QA 對後端詞彙也有同樣缺口**，只是這篇先從前端切入）

但現在三件事在改變：
1. **AI 給的測試 prompt 跨越前後端詞彙**——AI 不知道你 specialize 在哪邊
2. **全端開發越來越普遍**——QA 自然 scope 擴張
3. **用戶反饋越來越多是「畫面這裡怪怪的」**——需要前端詞彙才能精準回報、跟 RD 溝通

### 三、最小生存集合：四類詞彙 × 各 3-5 個關鍵詞

#### 3.1 載入狀態（Loading states）

| 詞彙 | 意義 | QA 該怎麼測 |
|---|---|---|
| **Skeleton loading** | 灰色塊預先展示內容輪廓 | 載入時是否有 skeleton、實際資料返回後是否**平滑替換**（不閃爍） |
| **Spinner** | 旋轉圓圈，最傳統的 loading | 阻塞操作時是否顯示、**超時時是否消失**、不要永遠轉 |
| **Progress bar** | 顯示具體進度（0%-100%） | 進度是否真實反映、**停滯時是否處理**、不要假進度 |
| **Shimmer** | 帶光澤動畫的 skeleton 變體 | 動畫流暢度、**不會卡 CPU** |
 infinite scroll

#### 3.2 用戶反饋（User feedback）

| 詞彙 | 意義 | QA 該怎麼測 |
|---|---|---|
| **Toast** | 短暫飄出、自動消失的訊息 | 顯示時間、可否手動關閉、**多個同時顯示時的堆疊行為** |
| **Snackbar** | Material Design 的 toast，常帶 action 按鈕 | 同 toast + **action 點擊行為** |
| **Banner** | 持續顯示的全寬訊息，需用戶 dismiss | 是否真的持續、**dismiss 後是否記住**（下次不要再跳） |
| **Modal / Dialog** | 阻擋背景操作的彈窗 | **ESC 鍵關閉、外部點擊行為、focus trap**（鍵盤 tab 不會跑出 modal） |
| **Drawer** | 從邊滑出的側邊面板 | 滑動方向、關閉手勢、**內容過長時的滾動** |
| **Optimistic UI** | UI 先假設操作成功立刻更新、失敗時 rollback（按愛心立刻變紅、留言立刻出現再悄悄送出） | **rollback 行為是否正確**、網路慢/失敗時是否有清楚提示、**不要假成功永不回退**（會掩蓋真實 bug） |

#### 3.3 表單狀態（Form states）

| 詞彙 | 意義 | QA 該怎麼測 |
|---|---|---|
| **Floating label** | 輸入時 label 浮到欄位上方 | 動畫流暢、**defocus 後如果空是否回到原位** |
| **Helper text** | 欄位下方的小字說明 | 是否顯示、**變 error 時是否被 error message 替換** |
| **Validation states** | error / success / warning 等視覺狀態 | **顏色 / icon / 文字三件套是否一致**、color-blind 友善 |
| **Inline validation** | 邊填邊驗證（vs. submit 才驗） | 觸發時機（onBlur vs onChange）、**錯誤太早出現會煩人** |

#### 3.4 導航結構（Navigation）

| 詞彙 | 意義 | QA 該怎麼測 |
|---|---|---|
| **Breadcrumb（麵包屑）** | 頁面層級路徑，例：首頁 > 分類 > 子分類 > 商品 | **層級正確、每層可點、目前頁不可點**、深層路徑不被截斷 |
| **Tab** | 同畫面內切換內容區塊 | **目前選中視覺明顯、切換時不會丟失輸入**、URL 是否同步（deep link 支援） |
| **Pagination（分頁）** | 上一頁 / 下一頁 / 頁碼 | 頁碼正確、最後一頁邊界、**首末頁按鈕的 disabled 狀態** |
| **Stepper** | 多步驟流程的進度顯示（註冊、結帳） | **不能跳步、上一步資料保留**、完成步驟視覺差異 |
| **Hamburger menu** | 漢堡選單（三條線圖示），手機版常見 | 展開動畫、**外部點擊關閉**、選後是否自動關閉 |

#### 3.5 訊息密度（Information density）

| 詞彙 | 意義 | QA 該怎麼測 |
|---|---|---|
| **Tooltip** | hover 顯示的小說明 | **手機沒 hover 該怎麼處理**、顯示位置不超出邊界 |
| **Popover** | 點擊觸發、比 tooltip 大的浮層 | **外部點擊關閉**、不會擋住重要內容 |
| **Badge** | 通知數字（紅點 / 數字） | **0 時是否消失**、`99+` 等截斷邏輯 |
| **Tag / Chip** | 標籤元件（可刪除、可選） | 刪除互動、**選中視覺**、長字截斷 |
| **CTA（Call to Action）** | 「呼籲行動」是一個相對模糊的概念，可能是按鈕——畫面上希望使用者點的主要動作（「立即註冊」「升級」「開始試用」） | **視覺優先級明確**（主 CTA / 次 CTA 對比清楚）、**文字具體**（「立即註冊」優於「OK」）、loading / disabled 狀態完整 ，並且整個路徑有達到邀請使用者做某件事情的目的(通常是掏錢)|
| **Empty state** | 沒資料時的畫面 | **不只是空白**——要有引導文字 + CTA 按鈕 |

#### 3.6 動畫術語

| 詞彙 | 意義 | QA 該怎麼測 |
|---|---|---|
| **Transition** | 兩狀態之間的過渡 | 流暢度、**沒有閃爍** |
| **Easing** | 動畫的速度曲線（linear / ease-in / ease-out / spring） | 主要看「不彆扭」 |
| **Micro-interaction** | 小動畫回饋（按鈕按下、checkbox 勾選） | **響應性**、不會延遲 100ms 以上 |

#### 3.7 存取控制 / 商業化（Access control & monetization）

| 詞彙 | 意義 | QA 該怎麼測 |
|---|---|---|
| **Paywall / Premium Gate** | 限制免費用戶存取的閘門（「升級才能看 / 用」） | **觸發條件正確**（不該擋的不要擋）、**升級流程順**、**取消訂閱後是否退回 gate**、cache / 帳號切換邊界 |
| **Feature gate** | 比 paywall 更細——擋特定功能（例：免費版有基礎匯出、premium 才能匯出 PDF） | 功能可見性、**用戶 tier 升級後是否立刻解鎖**（不該需要重啟 app） |
| **Login wall** | 強制登入才能看完整內容（看部分後跳） | **觸發時機**（看了多少才擋）、登入後是否回到原本位置不丟失上下文 |

（先抓最常見的，第一版不求完整）

### 四、進階：accessibility 一節（可選，看篇幅）

如果篇幅允許再加——這些是後端 QA 最容易忽略、但對企業客戶 / 政府客戶最常被查的：

- **aria labels**（給螢幕閱讀器看的標籤）
- **focus management**（鍵盤焦點該往哪去）
- **keyboard navigation**（不用滑鼠能不能完成所有操作）
- **color contrast**（WCAG AA / AAA）

如果第一版砍掉，可以當下一篇的引子（「**accessibility 是後端 QA 完全沒見過的世界**」）。

### 五、後端 QA 的學習資源建議

不講設計理論，只給能查的：

- **Material Design Guidelines**（Google 出的，最系統化、免費、有範例）
- **Apple Human Interface Guidelines**（iOS 必看，跟 Material 對照很有趣）
- **公司自己的 design system 文件**（如果有，這是最直接的）
- **Storybook of any 開源 UI library**（直接看 component 名 + 行為，例如 MUI / Chakra / Ant Design）

### 六、結語：AI 把這個缺口照出來

> 我做 QA 那麼多年，從沒主動問過自己「**我前端詞彙夠用嗎**」——直到 AI 給我一個我看不懂的測試案例。
>
> 這是 AI 對 QA 工作的另一種貢獻——**它用的詞彙跨越了你的舒適區，逼你補你不知道自己沒補的東西**。
>
> 跟著 AI 的測試 prompt 學詞彙，可能比看書還快。**讀不懂的詞，就是你下次該學的詞**。

---

## 跟其他線的關係

| 主題線 | 關係 |
|---|---|
| **線八（入門 / 長尾 SEO）** | 本篇主場——詞彙型文章 SEO 流量好 |
| **線二（AI 取代 / 當責）** | 結尾連到「**AI 暴露 QA 的知識缺口**」這個正向視角——AI 不取代 QA，AI 是 QA 的擴張鏡 |
| **線一（PDT）** | 緣起段是 PDT 的**反向應用**：別人（AI）給的東西暴露你沒問過的問題 |
| **線九（突發應變 / 自我審視）** | 「我從沒問過自己」這個自審視角度有 overlap |

---

## 寫作前還沒解決的

- [ ] **範圍**：寫一篇全覆蓋（四類詞彙都帶到）的 primer，還是只寫一類（loading states）做深？
  - 全覆蓋：SEO 廣、入門讀者收益高、深度淺
  - 單類深：論述更紮實、可以做一個系列、深度高
  - 傾向**全覆蓋淺**——這篇是 SEO 入門，目標是讓讀者「**至少不會卡在詞彙**」
- [ ] **截圖 / 圖示要不要做**：詞彙型文章配圖會大幅加分。可以用 CodePen 或現有 UI library 截圖
- [ ] **「QA 該怎麼測」這欄要不要展開**：簡單列 1 句 vs 每個詞彙寫 1 段
- [ ] **accessibility 一節要不要砍**：第一版可以砍以控制長度，當下一篇引子
- [ ] **觸發條件**：不急，但 SEO 入門線有需要。**可以較早動筆**（沒有同事/主管指紋顧慮）
- [ ] **可能的姊妹篇**：「**後端 QA 該認識的 accessibility**」「**後端 QA 該認識的 responsive design**」——如果這篇反應好，可以做系列

---

## 一句話定位

> 後端 QA 看到 AI 給的 `skeleton loading` 卡住三秒——那一刻不是 AI 不對，是**自己從沒問過自己這個詞彙缺口**。這篇幫你補上最小生存集合。
