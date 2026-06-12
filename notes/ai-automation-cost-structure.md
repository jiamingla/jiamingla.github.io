# AI 導入後，自動化測試的成本結構變成什麼樣子？（骨架）

**建立**：2026-06-12
**狀態**：🌱 骨架——核心三欄表已立、待填 AI 欄的具體 cost 拆解
**雙重定位**：
- **UI 自動化反思系列（五）候選**——[not-just-make-manual-script-automate](/post/not-just-make-manual-script-automate/) 結尾預告的「AI 時代的自動化測試：我們不再寫步驟，我們寫 Page API 與觀測指標」
- **[ai-era-tw-qa-needs](ai-era-tw-qa-needs.md) Gap 4（AI calibration 中道）的成本維度**
**起源**：6/12 寫 not-just 時 surface——「如果導入 AI，成本結構會變怎樣」值得獨立成篇、不塞進 not-just（避免提前爆雷系列五 + 稀釋 not-just 結尾 coda）

---

## 核心骨架：從二欄變三欄

not-just 第三節已立的二維模型 → AI 進來加第三欄：

| 維度 | 手動測試 | 傳統自動化 | **AI 輔助（待填）** |
|---|---|---|---|
| **稀缺資源** | 人的判斷時間 | 腳本維護成本 | ? **token 成本 / prompt 設計 / 結果判讀時間** |
| **擅長領域** | 探索、直覺、視覺、未知 bug | 重複、批次、結構驗證 | ? **生成草稿、跨語意翻譯、大量場景鋪陳** |
| **失敗模式** | 漏測、疲倦、不一致 | flaky、過期、維護債 | ? **幻覺、不可重現、過度自信的綠燈** |
| **失敗代價** | 一次性 | 複利累積 | ? **信任成本（一次幻覺毀掉對整批結果的信任）** |

→ **這張「二欄變三欄」的表本身就是文章骨架**。

---

## AI 欄的 cost 拆解（待想清楚、初步 brainstorm）

### 1. 新出現的成本（傳統自動化沒有的）

- **token 成本**：跑越多場景、API 費用越高（vs 腳本跑一次幾乎零邊際成本）
- **prompt 設計成本**：怎麼問 AI 才生出對的測試 = 新的 schema design 工作（連 [ai-era-tw-qa-needs](ai-era-tw-qa-needs.md) Gap 1 schema asset）
- **結果判讀成本**：AI 給的測試結果要人重審（連 [yes-man](/post/ai-as-yes-man-rd-pm-trust-calibration/)、6/3 Lead「AI 報告要先自己看再上報」）
- **不可重現成本**：同 prompt 不同次跑可能不同結果 → debug 難度上升
- **信任成本**：一次幻覺會毀掉對整批 AI 結果的信任（比 flaky 更難 recover——flaky 是已知不穩、幻覺是看起來很對的錯）

### 2. 被降低的成本（AI 真正省的）

- **初稿生成**：從零寫測試 → AI 生草稿、人改（草稿成本趨近零）
- **跨語意翻譯**：四角色語言混合 corpus（[5/12 insight](coach-sessions/2026-05-12-insights.md)）→ AI 跨角色中立
- **大量場景鋪陳**：邊界值組合、資料變體——AI 批次生成
- **維護的部分自癒**：UI 改版 AI 自我修復 locator（連 [POM AI 時代價值](pom-refactor-from-runnable-to-maintainable-planning.md)）

### 3. 成本「轉移」而非「消失」（最重要的論點）

> AI 不是讓成本歸零、是**把成本從「執行 / 維護」轉移到「設計 prompt + 判讀結果 + 校準信任」**。

→ 呼應 not-just 核心：**便宜資源 vs 稀缺資源**的配置原則沒變、只是稀缺資源的「位置」變了：
- 手動時代：稀缺 = 人的判斷時間（花在執行）
- 自動化時代：稀缺 = 腳本維護成本
- **AI 時代：稀缺 = 人的判讀 + 校準時間（花在「驗證 AI 對不對」）**

**這正是 [first-principle](software-testing-first-principle.md) 的延伸**——AI 是新一方 partial、需要 calibrate；測試員的稀缺資源從「執行」徹底轉到「顯影 AI 的 gap」。

---

## 候選標題

| # | 標題 | 風格 |
|---|---|---|
| 1 | 〈AI 導入後，自動化測試的成本結構變成什麼樣子？〉 | 問題開門、樸實 |
| 2 | 〈AI 不會讓測試成本歸零、只會把它搬到你沒注意的地方〉 | thesis 直放、有 punch |
| 3 | 〈從二欄變三欄：AI 時代測試資源模型的重新配置〉 | 接 not-just、系列感 |
| 4 | 〈我們不再寫步驟、我們寫 prompt 與判讀——AI 時代的測試成本〉 | not-just 預告的系列五原標題變體 |

---

## 候選結構

```
0. 開場：接 not-just——「便宜資源 vs 稀缺資源」原則沒變、但 AI 來了、稀缺資源換位置
1. 回顧二欄模型（not-just 第三節、快速帶過 + 連結）
2. 加第三欄：AI 輔助（核心三欄表）
3. AI 新出現的成本（token / prompt / 判讀 / 不可重現 / 信任）
4. AI 真正省的成本（初稿 / 跨語意 / 場景鋪陳 / 自癒）
5. 核心論點：成本「轉移」不是「消失」——稀缺資源從執行搬到判讀+校準
6. 結語：AI 時代最貴的不是算力、是「會判讀 AI 對不對」的人——收在 first-principle / PDT
```

---

## 揭露邊界 / 風險

- **低風險**：純方法論 + 資源模型論述、無公司指紋
- ⚠️ 唯一注意：token 成本 / 具體工具若舉例、用通用例子（不提公司實際用的 AI 方案、6/3 notes 提過「7 月起 Claude 改 MIS 團隊方案」這類內部資訊不寫）

---

## 對應主題線 / Gap / 既有檔

| 連動 | 關係 |
|---|---|
| **UI 自動化反思系列** | 系列（五）候選、收尾篇 |
| **Gap 4（AI calibration 中道）** | 成本維度——不恐慌不崇拜、看清成本搬去哪 |
| [first-principle](software-testing-first-principle.md) | AI 是新一方 partial、稀缺資源轉到「顯影 AI gap」 |
| [yes-man](/post/ai-as-yes-man-rd-pm-trust-calibration/) | 判讀成本 / 信任成本的源頭 |
| [ai-era-tw-qa-needs](ai-era-tw-qa-needs.md) Gap 1 | prompt 設計 = schema asset 的 AI 版 |
| [5/12 四角色 insight](coach-sessions/2026-05-12-insights.md) | AI 跨語意翻譯省的成本 |
| [successor-communication-and-ai-impatience](successor-communication-and-ai-impatience.md) | AI 即時回饋 vs 判讀需要的慢——成本的時間維度 |

---

## 待答（綠燈時段想）

- [ ] AI 欄四個維度的具體填法——token / prompt / 判讀 / 信任，哪個是主軸？
- [ ] 「成本轉移不消失」這個論點要不要當標題（選項 2）？
- [ ] 當系列（五）發、還是當獨立 Gap 4 文章發？（系列感 vs 獨立 SEO）
- [ ] 要不要放實際 token 數字 / 成本估算？（具體有說服力、但要用通用例子不洩內部）
- [ ] 跟 not-just 的互引怎麼設計（這篇開場回顧二欄、not-just 結尾已預告系列五）
