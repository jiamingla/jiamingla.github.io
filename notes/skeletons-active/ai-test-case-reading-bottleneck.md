# 備忘：AI 寫的測試案例越來越豐富，但 QA 讀不快——test case 缺少 scan affordance

**建立日期**：2026-05-28
**狀態**：💡 觀察記下，未來想寫時打開看
**起源**：5/28 對話——AI 產的測試案例越來越豐富，閱讀變成 bottleneck；對比程式碼有結構分塊可以快速 scan，test case（無論 AI 或手動寫的）都沒有這個性質

---

## 原始觀察（保留我的話）

> AI 給的測試案例的文字越來越豐富，我閱讀的慢，並且不像**程式碼**可以一個區一個區段看，手動測試案例看來不是如此。

---

## 我看到的結構：三種「閱讀單位」的對比

| 載體 | scan 單位 | 視覺 affordance | scanability |
|---|---|---|---|
| **程式碼** | function / class / file | 縮排、語法 highlight、IDE folding、minimap、outline | ⭐⭐⭐⭐ 高 |
| **AI 寫的 test case** | step（線性步驟） | 純 prose、無 fold、無 highlight、verbose | ⭐ 低 |
| **手動寫的 test case** | step（更短 prose） | 同上但 prose 更短 | ⭐⭐ 中 |

**關鍵觀察**：
1. **「scan 單位」決定閱讀速度的天花板**——程式碼可以 skip implementation 只讀 signature；test case 沒有 signature 可讀
2. **AI 寫的 case「字多」是表面問題**——更深的是 case 本身沒結構，verbose 在沒結構的載體上是雙倍痛
3. **手動 case 短不是因為「比較好」**——是因為作者預設了讀者有 context，能腦補 step 之間的銜接

---

## 5/28 第二層觀察：閱讀慢是表面、rationale 不可見是更深

整個 workflow 紀錄：

> 「我這次測試根本沒時間好好看整個產品的文件，就先把文件整份塞給 AI，結果產出的測試案例我看得很慢，**也不一定看的出來這個測試案例為什麼要存在**。」

這段話拆開來有**兩層問題**：

### 第一層：閱讀 scan 慢（前面那節已經處理）

純文字 + 缺結構 + AI verbose → 讀 1000 條 case 是 wall of text

### 第二層：rationale 不可見（這層更深）

不只「**讀得慢**」，是「**讀完也看不出為什麼這條 case 該存在**」：
- AI 是基於 spec 推導 case，但**「為什麼這條重要」的推理過程**沒寫進 case
- 重要性 / 風險判斷 / 業務脈絡 / 邊界判定——全在 AI 黑盒裡
- 讀 case 時看不到「**這條 case 在守什麼**」

→ 表面是 scan 工具問題，骨子裡是**理解問題**。

### Hidden cost：QA 對產品的內隱知識**沒長進**

這個 workflow 的隱形代價（**這是最該寫進文章的洞察**）：

```
QA 沒時間讀產品文件
  ↓
把文件全部 dump 給 AI
  ↓
AI 產出 case
  ↓
QA 也沒時間讀 case
  ↓
即使讀也看不出 rationale
  ↓
QA 在整個流程裡「沒有真正理解過這個產品」
```

**Workflow 看起來高效（case 產出、測試跑了），但 QA 的內隱知識完全沒累積**。

呼應 [yes-man-sequel-what-qa-still-owns](yes-man-sequel-what-qa-still-owns.md)「責任編輯」隱喻：
- **編輯不只是擋稿，是「對作品有深度理解」的人**
- 如果 QA 完全靠 AI 產 case，**責任編輯位置就空了**
- 不是 AI 取代了 QA，是 **QA 自己把責任編輯的座位讓出去了**

呼應 PDT：
- 測試案例的價值不在通過/失敗，在於**它揭露的不確定性**
- AI 產的 case **沒揭露不確定性**，只是給你一份 to-do list
- 沒 rationale = 沒揭露 = 沒 PDT

---

## 兩層問題對應到 affordance 設計

| 層次 | 缺的 affordance | 對應到既有方法論 |
|---|---|---|
| **第一層：scan 慢** | 分區、視覺加重、fold | Given/When/Then 結構 |
| **第二層：rationale 不可見** | **「為什麼這條存在」的顯式 metadata** | **PDT 提問** / 風險導向測試 |

→ 真正的 affordance 設計**兩層都要解**。只解第一層（讓 case 變短）會錯失更大的價值。

第二層的解法可能長這樣（每條 case 顯式包含）：
- **守的是什麼**（business rule / regression boundary / edge case）
- **如果這條失敗，可能漏掉什麼**（最壞情境）
- **為什麼這條跟其他類似 case 不重複**（differentiation）

→ 這正好是 [rethinking-regression-test-value](/post/rethinking-regression-test-value/) 那 4 個自問問題的另一面——前者問「該不該存在」，本篇問「**讀的人看不看得出來為什麼存在**」。

---

## 5/28 第三層觀察：真正的解方不在 AI prompt，在 QA 的前置工序

當下浮現的：

> 「下次遇到下一個全新的產品，我認為再給 AI 產測試的時候，**QA 自己也該用 PDT 往前走挖出內隱知識**。」

這句話把整篇文章從「**分析問題**」拉到「**給 actionable 解方**」。

### 兩個 workflow 對比

**Workflow A（現狀，有隱形代價）**：
```
QA 沒時間 → dump 整份文件給 AI
  → AI 產 case
  → QA 讀 case 慢、看不出 rationale
  → QA 沒長對產品的理解
  → QA 變成搬運工（責任編輯位置空了）
```

**Workflow B（PDT 前置，挖內隱知識）**：
```
QA 拿到文件 → 用 PDT 提問挖內隱知識
  (這個功能在守什麼？什麼情境下會壞？邊界在哪？)
  → QA 先長對產品的理解
  → 帶著問題去看 AI 產的 case
  → 知道哪條 case 守哪個提問、哪條缺、哪條多餘
  → QA 還是責任編輯，AI 是延伸提問的工具
```

### 為什麼 Workflow B 不只是解 rationale 問題，也救了 hidden cost

- Workflow A 的問題不只是「**讀得慢**」——是「**QA 沒成長**」
- Workflow B 的解法不只是「**多花一道工序**」——是「**保住 QA 對產品的內隱知識**」這條長期資產
- AI 加速 case 產出，**但 QA 自己的 PDT 不能省**——這道工序是 QA 不可被取代的核心

### 三個核心轉換

| 維度 | Workflow A | Workflow B |
|---|---|---|
| AI 的角色 | 黑盒輸出機 | **延伸提問的工具** |
| QA 的位置 | 搬運工 | **責任編輯（仍有 ground truth）** |
| 對產品的理解 | 沒長進 | **透過 PDT 持續累積** |
| 讀 case 時 | 看不出 rationale | **看得出每條 case 守哪個提問** |

### 一個重要金句

> **「想被 AI 幫忙，自己得先『值得被幫』。**
> **不挖內隱知識 → AI 給的 case 就是黑盒輸出，QA 變成搬運工。**
> **挖了內隱知識 → AI 給的 case 變成『替我延伸的提問』，QA 還是責任編輯。」**

這段話可能會是整篇文章最重要的核心——它**把 PDT 招牌主張、yes-man 責任編輯、AI literacy 三條線一次串起來**。

---

## 5/28 第四層觀察：DevOps 類比——AI 加速暴露短板

### 活體證據（必須寫進文章前言）

> 「今天請 AI 產 100 個 case，**真的是看 30 個就想把腦袋關機**。」

這個畫面是整篇文章最有溫度的入口。不是抽象「閱讀慢」，是**腦袋直接關機**——身體層次的回應。

100 / 30 這個比例本身就是 hook：**消化跟產出的比例是 0.3**。

### 借自 DevOps 的 framing（來源：David Ko 或類似業界文章，**寫文時須 verify 來源**）

業界已有的觀察：
> 「AI 讓 Deploy 速度從一週幾次變成一天幾次，**卻也同時讓大家看見 DevOps 的短板**——監控、事故反應、容量規劃、安全審查，每一塊都被加速暴露出原本能勉強撐住的瓶頸。」

→ **同樣的 pattern 正在 QA 發生**：
- AI 讓「產 case」從一週幾百條變成一天上千條
- 但這個加速**不是讓 QA 輕鬆**——是讓**原本能勉強撐住的短板全部暴露出來**

### QA 流程被暴露的「短板」清單

當「產 case」變得便宜，下面這些原本被掩蓋的瓶頸全部浮上來：

| 短板 | 為什麼以前看不到 | 為什麼現在暴露 |
|---|---|---|
| **Rationale 累積機制** | 以前 case 量少、QA 自己寫、邊寫邊知道為什麼 | 現在 AI 產的 case 沒帶 rationale，QA 沒參與推導 |
| **產品內隱知識** | 以前 QA 邊測邊長知識 | 現在 dump 文件給 AI、QA 跳過理解步驟 |
| **Case 分類 / 重複偵測** | 以前 case 數量在大腦 cache 內 | 現在 1000 條 case，腦袋根本撐不住 |
| **Case 維護策略**（哪條該砍）| 以前不抽不寫就不長、長慢 | 現在每週長 10x，舊的還沒處理新的又來 |
| **新人 onboarding** | 以前 case 寫法可以邊讀邊學 | 現在 verbose AI prose，新人讀更慢 |

### 為什麼 DevOps 類比是文章的最強 hook

1. **業界已驗證的 pattern**——讀者不用被說服「加速會暴露短板」這個結構性論點，已經是共識
2. **跨領域類比 = 文章高度上一級**——讓本文不只是 QA 圈題目，是 software development 普遍議題
3. **賦予 framing 重量**——「**AI 加速暴露短板**」這六個字可能比「scan affordance」這種技術詞彙更容易被傳播
4. **連到 actionable**：DevOps 應對短板的方式（observability、SRE、incident response）QA 也可以套用同樣的「先看見、再投資」邏輯

### 對文章框架的影響

前言應該改用這個 hook：

```
前言：100 條 case，我看 30 個就把腦袋關機

  → AI 替我產了 100 條 case，我看 30 個就把腦袋關機。
  → 這不是 AI 寫得爛——case 寫得清楚、結構完整、step 詳細。
  → 是我自己撐不住「看的速度」。
  →
  → 這讓我想起 DevOps 圈早就在說的事：
  →   AI 讓 Deploy 速度從一週幾次變成一天幾次，
  →   卻也同時讓大家看見 DevOps 的短板。
  →
  → QA 也是如此——當 AI 讓「產 case」變便宜，
  → 原本能勉強撐住的瓶頸，全部會被加速暴露。
```

這個前言比原本「沒時間讀文件」更強，因為它**自帶結構性洞察**，不只是個人困擾。

---

## 5/28 第五層觀察：神經科學層次——閱讀程式碼跟讀 prose 用的是不同的大腦網絡

### 已驗證的 neuroscience 研究（**寫文時須引用 verify**）

- **Ivanova et al. (2020)**, MIT — "Comprehension of computer code relies primarily on domain-general executive brain regions"
- **Siegmund et al. (2014)** — 用 fMRI 觀察 source code 閱讀的腦區激活

**核心發現**：閱讀程式碼主要動用 **multiple demand (MD) network**（一般執行功能、問題解決），**不是**像讀自然語言那樣主要靠 **language network**。

### 三種測試載體的神經科學投射

| 載體 | 主要動用的腦網絡 | 閱讀代價 |
|---|---|---|
| **程式碼** | MD network（執行 / 問題解決） | 並行可解、速度快 |
| **自動化測試腳本**（Selenium / pytest / cypress）| 推測同 MD network（code-like 結構） | 推測速度快 |
| **手動測試案例 prose** | **Language network**（語言處理） | **序列、不可並行、必然慢** |
| **AI 產的 verbose case** | Language network × verbose 加成 | **最痛** |

### 為什麼這層觀察是文章最深的錨點

前四層分析（scan affordance / rationale / hidden cost / DevOps 短板）都隱含一個假設——「這個問題可以靠工具或流程改善」。

**神經科學層次直接拒絕這個假設**：
- 大腦讀 prose 的速度有**生物學上限**
- 工具可以把「序列 prose」轉成「結構化 code-like」表示——但**不能讓語言處理本身變快**
- → 結論不是「等更好的工具」，是「**把 case 表示形式從 prose 切換到 structured / code-like**」

「**這不是工具問題，是大腦問題**」這句話一旦立起來，整篇文章的論述重量升一級——它從「QA 圈的觀察文」變成「**有生物學基礎的結構性主張**」。

### 對 QA 角色的暗示（值得寫進文章）

- **自動化測試腳本「讀起來像 code」這件事不是巧合**——讀法本來就跟 code 一樣（MD network）
- **手動 case 維持 prose 是因為「容易寫」**（語言區寫起來自然）——但讀起來在另一個維度
- → 「**寫的人輕鬆 = 讀的人累**」這個落差有 **neurological 原因**
- QA 一直在「替別人讀 case 把答案抽出來」這個位置——這個位置的辛苦是有 neural basis 的

### 對 Workflow B（PDT 前置）的補強

這層觀察其實也**解釋了為什麼 Workflow B 真的會快**：

- 用 PDT 提問挖內隱知識時，**QA 在做 problem-solving**（MD network）——大腦最擅長的網絡
- 用 AI 產 case 後，case 是「**替我延伸的提問**」——讀時 QA 在做「**對照模式判斷**」（MD network），不是「逐句讀 prose」（language network）
- → 不是因為「Workflow B 比較有條理」，是因為它**把 QA 的大腦放回擅長的網絡**

### 這層對第二層問題（rationale 不可見）的深層解釋

為什麼讀不出 rationale？**神經科學給了答案**：

- 讀 prose 時，meta judgement（「為什麼 X 重要」）會被 language processing **suppress** 掉
- 大腦不能同時做「serial language parsing」 + 「parallel meta judgement」
- → 讀 verbose prose 時，rationale judgement **物理上**沒空間發生

**這個解釋比「AI 沒寫 rationale」更深**——就算 AI 寫了 rationale，讀者在 prose 模式下也很難 process。
**解方不只是「讓 AI 寫 rationale」，是「讓 rationale 用結構化方式呈現」（tag / 欄位 / 分區），讓 MD network 可以處理。**

---

## 5/28 神經科學的通俗版本：齒輪 vs 敘事性文學（**這可能才是文章真正的 hook**）

直覺版的同一個發現——不需要懂 neuroscience，QA 自己用比喻就摸得到：

> **程式碼**：「腦袋裡只跑一個問題——**這有沒有照我預期的齒輪一樣好好運轉**？」
>
> **測試案例**：「會一直想**這要測什麼、為什麼要這麼測**——跟讀**敘事性文學**差不多。」

這個比喻**直接對應神經科學的發現**：
- **齒輪檢查** = 執行 / 預測模型 / problem-solving → **MD network**
- **讀敘事性文學** = 持續詮釋作者意圖 / theory of mind → **language network + 敘事理解**

→ **比「multiple demand network」這種術語好用一百倍**。

### 三個跟同事閒聊用的版本

1. **完整比喻**：「程式碼像在檢查齒輪有沒有照我預期運轉；測試案例像讀小說，要一直猜作者為什麼這樣安排情節。」
2. **更日常**：「程式碼有編譯器替你抓錯；prose 沒有——你讀完才知道作者意圖跟你想的不一樣。」
3. **直接挑戰**：「讀 100 行 code 跟讀 100 行測試案例 prose，哪個累？為什麼？」（**先讓對方自己感受到，再揭曉**）

### 一個自然引出 AI 議題的追問

> 「現在 AI 寫 case 都寫得像**敘事文學**——詳細、verbose、有上下文。你覺得這對 QA 是幫忙，還是增加閱讀負擔？」

對方答什麼都可以接到 Workflow B：
- 說「幫忙」→「**所以你能讀完 100 條？**」
- 說「負擔」→「**對啊我也是、所以我在想⋯⋯**」

### 對文章 hook 的提示

備忘檔的「文章框架草擬」前言目前用「**100 條 case 看 30 個關機 + DevOps 類比**」當 hook。**這個齒輪 vs 敘事性文學的比喻可能更強**——更直覺、更容易記住、不需要 verify reference。

未來動筆時可以考慮**重排前言順序**：
1. **比喻先**（齒輪 vs 敘事性文學）——讀者立刻有畫面
2. **個人 anecdote**（100 條看 30 個關機）——把比喻拉到具體場景
3. **DevOps 類比**——把個人困擾升級到結構性論述
4. **神經科學作為背書**——「對，這不是錯覺，研究證實了」

→ **比喻 → 故事 → 結構 → 學理**。這個順序比學理 → 故事流暢得多。

---

## 為什麼這個瓶頸現在浮現？

三個結構性原因：

1. **AI 加速「產 case」，沒加速「讀 case」**——產出速度跟消化速度之間的不對稱第一次拉這麼開
2. **AI 寫的 case 預設讀者不是你**（呼應 [ai-test-output-default-reader-is-ai](../source/_drafts/ai-test-output-default-reader-is-ai.md)）——它寫得像一篇 spec 文件給機器讀，不是給 QA 工作時 scan
3. **Case 數量爆炸**：以前 100 條 case 是上限，現在 AI 可以產 1000 條——個別 case 寫得再好，**1000 條讀過去就是 1000 條 wall of text**

---

## QA 需要什麼？—— Test case 的 IDE 等級工具想像

程式碼有了 IDE 之後，閱讀速度被工具救起來。**Test case 還在「純文字編輯器」時代**。

### 5/28 補：IDE 給程式碼的真正禮物，是「**進出閱讀**」的能力

> 「在閱讀程式碼裡，我們有**強大的 IDE 幫助我們快速進出閱讀**，但測試案例沒有這類工具。」

這句話點破了問題的核心——IDE 不只是 syntax highlighting，它給的是**進出閱讀的自由**：

- **Jump to definition** → 順著一條線追下去
- **Go back** → 隨時回到原點
- **Fold / unfold** → 只看 outline，需要才展開
- **Minimap** → 全域空間感
- **Hover tooltip** → 不離開當前位置就拿到資訊
- **Search project-wide** → 跨檔案 query

**這些全是「進出」動作**——可以下沉到細節、可以浮回大局、可以橫向跳。**程式碼的閱讀本來就不是線性的**。

而 test case prose？
- 沒有 jump to
- 沒有 fold
- 沒有 minimap
- **只能從頭讀到尾，線性、一次性、不可進出**

→ 不是「test case 比較難讀」——是「**test case 的載體拒絕你進出**」。

這個 framing 跟第五層神經科學完美互補：
- 神經科學說：**讀 prose 用 language network，序列、不可並行**
- IDE asymmetry 說：**就算大腦想並行，工具也沒給你並行的入口**

→ **兩個層次同時鎖死 QA 的閱讀效率**。文章寫這段時可以連著講——讀者讀完會有強烈的「**這不是我笨，是條件被剝奪了**」的釋然感。



可能的 affordance 改造方向：

| 改造 | 對應程式碼的什麼 |
|---|---|
| **每條 case 顯式分區（前置 / 步驟 / 驗證 / 邊界）** | 像 docstring vs implementation |
| **驗證點視覺加重**（bold / 顏色）、setup 步驟弱化 | Like syntax highlighting |
| **可折疊的 outline mode**（只看標題、需要才展開）| IDE folding |
| **Tag 系統**（「結構性驗證」/「UX 判斷」/「業務流程」）| File type / namespace |
| **長 case 拆成具名子段** | Refactor into helper functions |

**重要洞察**：Given / When / Then 這個結構**就是 test case 的「function signature」嘗試**——但很多人寫成自由 prose，把這個 affordance 丟掉了。AI 寫的 case 更慘——它把 Given/When/Then 都寫成了 verbose narrative。

---

## 三條線的交會點

| 既有線 / 草稿 | 跟本篇的關係 |
|---|---|
| [ai-test-output-default-reader-is-ai](../source/_drafts/ai-test-output-default-reader-is-ai.md) | **同源**——那篇講「AI output 預設讀者是 AI 不是你」，本篇是它的**具體場景**：test case 是這個現象最痛的活體 |
| [yes-man-rd-pm-trust-calibration](/post/ai-as-yes-man-rd-pm-trust-calibration/) | yes-man 講「AI 不替你篩」，本篇講「**AI 不替你結構化**」——AI 生產力 vs QA 消化力的不對稱 |
| [ai-bug-fix-faster-than-ticket](ai-bug-fix-faster-than-ticket.md) | **同一個 pattern 第三個案例**——AI 加速某個動作（修 bug / 產 case / 給結果）但不加速人類消化它的能力 |
| 線一 PDT | 「結構化提問」是 PDT 的核心；test case 沒結構 = 沒被 PDT 過 |
| 線四 測試紀律 | Given/When/Then 是測試方法論的經典，本篇可以重新解釋它的「**affordance 設計**」價值 |

---

## 可能的文章角度（4 個，按優先排）

| 角度 | 主題線 | 核心 | 可發性 |
|---|---|---|---|
| **A. 〈AI 寫的測試案例越來越豐富，但 QA 讀不快——test case 沒有「scan 單位」〉** ⭐⭐ | 線二 + 線四 | 三載體（程式碼 / AI case / 手動 case）的 affordance 比較 | **極高**（題目稀缺、SEO ⭐⭐⭐⭐） |
| **B. 〈Given/When/Then 不只是寫作格式——它是 test case 的「function signature」〉** ⭐⭐ | 線四 PDT 方法論 | 把 GWT 重新詮釋成 affordance 設計 | 高（純方法論、零指紋） |
| **C. 〈AI 加速「產」，但沒加速「消化」——一個結構性的不對稱〉** | 線二 AI literacy | 把這個 pattern 升級到通用 framework，用 test case + bug fix + report 三個案例 | 高（跨多案例論述） |
| **D. 〈Test case 還在純文字編輯器時代——我們需要 test case 的 IDE〉** | 線四 + 工具想像 | 比較投機，但稀缺到極點 | 中（偏前瞻、可能變成 conceptual essay 而非 actionable） |

**A 文最該先寫**——它包含 B 跟 C 的核心、SEO 力最強、有具體對照（三載體比較表）。

---

## 跟 [ai-test-output-default-reader-is-ai](../source/_drafts/ai-test-output-default-reader-is-ai.md) 的關係——重要決定

那篇草稿的核心：「AI output 預設讀者不是你」。本篇的核心：「test case 沒有 scan affordance」。

**兩種處理方式**：

1. **本篇單獨成文**——具體場景 + 三載體對比，跟 ai-test-output 互引
2. **本篇變成 ai-test-output 的「**最強案例段**」**——把 ai-test-output 從泛論升級成有具體錨點的文章

→ **建議路徑**：等 ai-test-output 動筆時，**先把本篇觀察寫進去看 fit 不 fit**。如果 ai-test-output 整篇結構撐得起這個案例，就合併；如果發現本篇值得獨立深寫，再分篇。**不要現在就決定**。

---

## 不能丟掉的金句

> ⭐ **「AI 加速『產 case』，但沒加速『讀 case』——產出跟消化的不對稱第一次拉這麼開。」**

> ⭐ **「程式碼可以 skip implementation 讀 signature；test case 沒有 signature 可讀。」**

> ⭐ **「Given/When/Then 是 test case 的『function signature』嘗試——但很多人寫成自由 prose，把這個 affordance 丟掉了。」**

> **「AI 寫的 case verbose，是因為它把 Given/When/Then 都展開成了 narrative。」**

> **「Test case 還在純文字編輯器時代——我們需要 test case 的 IDE。」**

---

## 文章框架草擬（5/28 升級為三層架構 + 解方層）

```
前言：那個沒時間讀文件的早上
  → 我這次測試根本沒時間好好看整個產品的文件
  → 就先把文件整份塞給 AI
  → AI 產出 test case 清單
  → 我讀得慢、而且看不出每條 case 為什麼要存在
  → 兩層問題同時打中（scan 慢 + rationale 不可見）
  → 而且還有第三層代價：「我整個過程沒真正理解過這個產品」

一、第一層問題：為什麼讀得慢？scan affordance 的缺失
  → 程式碼可以快讀的三個 affordance（signature / 縮排 / IDE folding）
  → Test case 沒有「scan 單位」——一條 case 就是一段 prose
  → AI 寫的 case 把 Given/When/Then 寫成 narrative
  → Verbose 在沒結構的載體上是雙倍痛

二、第二層問題：為什麼看不出 case 為什麼存在？rationale 不可見
  → AI 基於 spec 推導 case，但「為什麼這條重要」沒寫進 case
  → 重要性 / 風險判斷 / 業務脈絡——全在 AI 黑盒裡
  → 讀者看不到「這條 case 在守什麼」
  → 呼應 rethinking-regression 的 4 個自問——前者問「該不該存在」，本篇問「讀的人看不看得出來為什麼存在」

三、Hidden cost：QA 對產品的內隱知識沒長進
  → Workflow 看起來高效（case 產出、測試跑了）
  → 但 QA 在整個流程裡「沒有真正理解過這個產品」
  → 不是 AI 取代了責任編輯，是 QA 自己讓出了座位
  → 呼應 yes-man-sequel 的「責任編輯」隱喻

四、Given/When/Then 解第一層，但解不了第二、三層
  → GWT 是 test case 的 function signature——解 scan 問題
  → 但 GWT 不揭露 rationale——還缺第二層 affordance
  → 而且 GWT 解的是「讀 case 的工具」，沒解「QA 自己對產品的理解」

五、真正的解方不在 AI prompt，在 QA 的前置工序：用 PDT 挖內隱知識
  → Workflow A（現狀）：dump 文件 → AI 產 case → QA 讀不出 rationale → 變搬運工
  → Workflow B（推薦）：QA 先用 PDT 提問挖內隱知識 → 自己長理解 → 再給 AI 產 case → 知道哪條守哪個提問
  → 三個轉換：
    - AI 的角色：黑盒輸出機 → 延伸提問的工具
    - QA 的位置：搬運工 → 責任編輯（仍有 ground truth）
    - 對產品的理解：沒長進 → 持續累積
  → AI 加速 case 產出，但 QA 自己的 PDT 不能省

結語：想被 AI 幫忙，自己得先「值得被幫」
  → 不挖內隱知識 → AI 給的 case 就是黑盒輸出，QA 變成搬運工
  → 挖了內隱知識 → AI 給的 case 變成「替我延伸的提問」，QA 還是責任編輯
  → AI 沒取代 QA，QA 自己決定要不要把責任編輯的位置讓出去
```

**vs 5/28 原版的升級重點**：

| 維度 | 原版 | 升級版 |
|---|---|---|
| 問題層次 | 只有「scan 慢」單層 | 三層：scan / rationale / hidden cost |
| 解方層 | 「未來的 test case IDE」（speculative）| **PDT 前置工序**（actionable） |
| Hook | 1000 條 case 的早上 | **沒時間讀文件、dump 給 AI** 的早上（更真實的 workflow 描述） |
| 跨線連結 | 線二 + 線四 | **線一（PDT）+ 線二 + 線四 + 線六（yes-man 責任編輯）** 四線匯流 |
| 結語強度 | 「QA 守閱讀速度」 | **「QA 自己決定要不要把責任編輯位置讓出去」** |

→ 升級後的版本**從 SEO 入門文升級成招牌系列的核心文**——它把 PDT、yes-man、AI literacy 三條線正式合流。可能是這條主題系列的最強錨點文章之一。

---

## 觸發條件（什麼時候從 notes/ 進 _drafts/）

任一成立：

- [ ] 等 ai-test-output-default-reader 動筆時，看本篇能不能 fit 進去
- [ ] 實際遇到 1-2 次 AI 給的 1000+ case 場景，有真實閱讀痛苦的具體 anecdote
- [ ] 跟同事或主管聊過「AI 給的 case 讀得慢」——他們的反應會是文章內容
- [ ] 試過在 AI prompt 裡強制要求 GWT 格式，觀察前後閱讀速度差別——這個 A/B 對比會是文章最強骨幹

---

## 紅線

- ❌ 不要寫成「AI 寫的 case 沒用」——主張是「**AI 沒給對 affordance**」，不是 AI 本身爛
- ❌ 不要點名具體 AI 工具的爛——Claude / GPT / Cursor 都會這樣，這是 LLM 共通問題
- ❌ 不要寫成「我們要造 test case IDE」這種 build it yourself 的承諾——這是 conceptual essay，不是 product roadmap
- ❌ 不要過度 idealize Given/When/Then——它有它的代價（reads 機械、不適合探索式 case），主張是「**有結構 > 沒結構**」，不是「**GWT 是 silver bullet**」

---

## 5/28 第六層：寫這篇的個人動機（給未來自己，**不寫進文章正文**）

### 為什麼我會這麼想

> 「這篇文章其他人可能沒這麼想，**我會這麼想是因為我沒有辦法為一個我不夠了解的產品扛起當責的責任**。我想要當顧問，但責任編輯驅使著我不該全部都交給 AI，即便這是大勢所趨。」

這段話揭露了文章的 personal driver——

- **當責的紅線**：「無法為不夠了解的產品簽名」是這篇五層論述的真正起點
- **顧問 vs 責任編輯的張力**：北極星往顧問走（5/27 揭曉），但**責任編輯的本能阻止全部假手 AI**——這個張力本身是文章的 hidden engine
- **承認業界趨勢、但有個人閘門**：不否認 AI 會接管更多，但有 personal 紅線

### 跟 5/27 Coach session 的呼應

5/27：「**北極星 = Manager；C 堆才是 QA 主場；先攻 B 堆，因為 AI 進不來**」
5/28：「**我想當顧問**；但**責任編輯驅使我不該全部交 AI**」

→ **本篇是 5/27 職涯方向的活體實踐**。文章外顯內容（test case reading）跟內在動機（顧問 + 責任編輯）是同一件事的兩面。

### 對文章定位的影響

這篇**不是寫給所有 QA 的**：
- 對「**同型 QA**」（想當顧問 + 有責任編輯本能）會深度共鳴
- 對「**執行型 QA**」（滿足完成任務、樂見 AI 接手）可能只是「有道理但 so what」

→ niche audience 的深度共鳴 > broad audience 的淺度認同。**這沒問題，就讓它是 niche 文。**

### 這段個人動機不要直接寫進文章

讀者不需要知道作者的內在動機。**但可以在結語暗藏**——拋一個邀請讀者自己定位的問題（見下方 sequel idea）。

---

## 潛在 sequel：〈QA 該主動放手 AI 到什麼程度？〉

### 起源

> 「看來 QA 也需要討論該放手交給 AI 的程度高還是低。」

### 為什麼這個 reframing 強

業界目前的 AI in QA 論述全在「**AI 能不能取代 QA**」（被動 framing）。**沒人在問「QA 該主動放手多少」**（主動 framing）。

這個 reframing 跟 yes-man 系列的「主動姿態」完全一致——不是「等 AI 來」，是「**QA 主動決定 AI 進多少**」。

### 可能的 spectrum 框架

| 放手程度 | 工作流程 | 守的是什麼 |
|---|---|---|
| 0% | QA 自己寫所有 case | 完全的對產品理解 |
| 30% | AI 寫 boilerplate、QA 寫核心 | 關鍵 path 的判斷權 |
| **50%（本篇推薦的 Workflow B）** | **QA 用 PDT 挖內隱知識 + AI 產 case** | **責任編輯位置 + 顧問能力累積** |
| 80% | QA 只審查 AI 產出 | 終端把關權 |
| 100% | QA 完全不參與 | 什麼都不守 → 變搬運工 |

重點不是哪個 % 對，是 **QA 該意識到「自己現在在哪個 %」、為什麼**。

### 可能的本篇結語邀請（暗藏 sequel 鉤子）

```
「你現在的『放手程度』是幾 %？為什麼是這個數字？
 你的選擇背後，守的是什麼？」
```

→ 這三句問題既邀請讀者自我定位，也預告 sequel。

### 觸發條件

- [ ] 本篇（reading bottleneck）寫完 + 上稿
- [ ] 累積 1-2 個跟同事討論「放手程度」的真實對話
- [ ] 業界出現更多「主動 framing」的文章可以對話

---

## 給未來自己的提醒

寫的時候**保留「1000 條 case 的早上」這個畫面**——它是這篇文章唯一有溫度的入口。其他都是結構分析，沒有那個畫面文章會變成乾乾的 technical essay。

> **「字寫得清楚、結構完整、step 詳細——但我讀到第 30 條就累了。」**

這句是整篇的情緒錨點。
