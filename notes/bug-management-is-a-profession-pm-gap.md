# Bug 管理是一門專業、但我們把它當雜務塞給 PM（骨架）

**建立**：2026-06-11
**狀態**：🌱 骨架——核心 observation 已成形、待想清楚跟姊妹骨架的分工再動筆
**起源**：6/11 工作觀察——現組織選擇把 bug 交給 PM 追蹤、好處是減 QA 負擔、壞處是 PM 太忙 + **根本沒學過怎麼管理 bug**
**姊妹骨架**：[bug-triage-pm-turnover-cost](bug-triage-pm-turnover-cost.md)——那篇處理「**PM 流動率**」（人走了、routing knowledge 跟著走）；**這篇處理「PM 能力結構」**（人在、但不會 + 沒空 + 不是他的 KPI）。兩篇都是 [6/10 文章](/post/bug-triage-six-patterns-industry-survey/) Pattern A 的 hidden cost 深掘、未來可能合併成一篇或拆兩篇

---

## 核心 observation（user 原話意旨）

> 「這裡選擇把 bug 交給 PM 去追蹤。好處是減少 QA 的負擔；壞處是 PM 自己已經太忙了、**並且有些 PM 根本不擅長或沒學過如何管理 bug——他們只擅長追蹤那些要開發的功能**。這是 AI 時代下我覺得組織有點卡關的點。」

---

## 核心論點拆解

### 1. Feature tracking 和 bug tracking 是兩種不同的專業

| 維度 | Feature tracking（PM 受過訓的） | Bug tracking（沒人教過 PM 的） |
|---|---|---|
| 物件性質 | 計畫中的、有 roadmap 位置 | 突發的、沒人邀請它出現 |
| 需要的判斷 | 商業優先級、用戶價值 | **severity calibration、dedup、regression 關聯、技術判讀** |
| 數量曲線 | 可控（roadmap 排的） | 不可控（**AI 時代爆量**） |
| 完成定義 | shipped | 修了？關了？不修？——**連「完成」都沒共識** |
| 是誰的 KPI | ✅ PM 的核心 KPI | ❌ 沒人的 KPI（連 [6/10 後對話](bug-triage-pm-turnover-cost.md)「管好 bug 是誰的 KPI」） |

→ **把 bug 丟給 PM = 讓沒受訓的人、做沒人認領 KPI 的事、用錯的工具心智模型（拿 feature 思維管 defect）**。

### 2. 這不是 PM 的錯——是組織把「專業」當「雜務」

呼應 [6/10 文章](/post/bug-triage-six-patterns-industry-survey/) 已寫的「業界沒有單一最佳解」+ [PM-QA 介面](pm-qa-interface-structured-workflow.md)的「雙向 scope creep」reframe：

- PM 面試以為要當 APP PM、進來發現要管 bug——**bug 管理是他沒簽約的工作**
- QA 面試以為測 APP、進來發現要補 PM 不會管 bug 的洞
- **兩個 scope creep 受害者、中間掉著一門沒人認領的專業**

### 3. AI 時代為什麼這個缺口會放大（**文章的時代 differentiator**）

```
AI 提速 RD 產 code → bug 產量上升（5/31 觀察：新功能動輒夾帶幾十個 bug）
AI 提速 QA 報 bug → inbox 進量也上升
      ↓
PM 的 bug 管理 capacity 沒變、技能沒變、KPI 沒變
      ↓
瓶頸從「產 code」「找 bug」轉移到「治理 bug」
      ↓
組織卡關點：用 AI 加速了 bug 的「生產」、沒人用 AI 改善 bug 的「治理」
```

→ **最後一行是 punch**：直接接線十「AI 是無主之地的天然守門員」——AI 補位論的又一個結構性論證。

### 4.「減少 QA 負擔」這個好處的重新估價

組織的 trade-off 是真的（QA 人力有限），但搬走的是「追蹤的勞動」、搬不走「治理的專業」——專業沒跟著走、就掉在地上：

- QA 卸下了 inbox、但 bug 評級飄移（PM 用商業直覺給 severity）
- 重複單沒人 dedup（PM 不知道怎麼搜既有單——連 [bug 標題指南](ai-era-tw-qa-needs.md) 526 筆數據裡的 6 組重複標題）
- regression 關聯沒人建（PM 不知道這個 bug 跟上版哪個 bug 同源）
- → **這些活最後還是回頭找 QA**（「這單跟之前那個一樣嗎？」）——負擔沒消失、變成碎片化的諮詢

---

## 候選文章標題

| # | 標題 | 風格 |
|---|---|---|
| 1 | 〈Bug 管理是一門專業、但我們把它當雜務塞給 PM〉 | thesis 直放、最有 punch |
| 2 | 〈PM 擅長追功能、不擅長追 bug——AI 時代這個缺口正在放大〉 | 對比型 + 時代感 |
| 3 | 〈AI 加速了 bug 的生產、誰來治理 bug？〉 | 問題開門、接線十 AI 補位 |
| 4 | 〈「把 bug 交給 PM」之後：一個善意決定的隱形成本〉 | 敘事型、對組織最溫和 |

---

## 揭露邊界（⚠️ 比姊妹篇更敏感）

- 「我們組織把 bug 交給 PM」是**現公司在跑的制度**——6/10 文章已決定「現公司不寫」
- 處理方式：寫成「**Pattern A（PM 預設）組織的通病**」、用 6/10 文章的業界框架當底、**不說這是我們公司**
- 「PM 不擅長管 bug」這句直接發會傷現職 PM 關係（PM-Ca 等人可能讀到）——**framing 必須是「組織沒給 PM 這個訓練 / 這不是 PM 的 KPI」**、矛頭對結構不對人
- 對照：你 5/30 觀察過 PM-Ca 是「重視文件的異類 PM」——證明這是訓練 / 結構問題、不是個人能力問題、**這個證據本身可以寫進文章**（去識別後）

---

## 對應主題線 / Gap / 既有檔

| 連動 | 關係 |
|---|---|
| [6/10 bug-triage 文章](/post/bug-triage-six-patterns-industry-survey/) | Pattern A hidden cost 深掘、天然續篇 |
| [bug-triage-pm-turnover-cost](bug-triage-pm-turnover-cost.md) | 姊妹骨架：turnover（人走）vs competency（人在但不會）——**動筆前先決定合併 or 拆開** |
| [ai-era-tw-qa-needs](ai-era-tw-qa-needs.md) Gap 3 | 「資產 vs 負債」——PM 把 bug list 當負債、因為他的 KPI 是 feature delivery |
| 線十（無主之地） | 「AI 加速 bug 生產、沒人治理」= AI 補位論的結構性論證 |
| [pm-qa-interface-structured-workflow](pm-qa-interface-structured-workflow.md) | PM 不會寫 spec 給 QA + PM 不會管 bug = **PM-QA 介面兩個方向都沒 schema** 的同一結構問題 |
| [5/12 insights](coach-sessions/2026-05-12-insights.md) | 四角色語言 corpus——PM 只讀得懂客服 + 自己的語言 |

---

## 待答（綠燈時段想）

- [ ] **跟 turnover 骨架的分工**：合併成一篇〈Pattern A 的三個 hidden cost〉（turnover + competency + KPI 真空）？還是拆兩篇？傾向先想清楚再動、避免兩篇互相蠶食
- [ ] 「組織卡關」這個判斷要不要先跟 Head 聊過再寫？（順著「管好 bug 是誰的 KPI」那題一起問）
- [ ] PM 視角的平衡段怎麼寫？（找 PM-Ca 類型的 PM 聊過會更紮實——但會暴露寫作意圖、再想）
- [ ] 發稿時機：6/10 文章 cluster 還熱、但這篇揭露邊界要想清楚——**不急、寧慢勿險**
