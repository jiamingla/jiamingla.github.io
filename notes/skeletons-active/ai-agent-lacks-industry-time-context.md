# 〈AI Agent 最缺的不是能力，是「業界時間」累積的 context〉骨架

> 📂 **定位**：線二（AI 測試 / AI literacy）+「難量化能力」moat 主題。**你的招牌角度**（AI 時代 QA 不可取代的那塊）。
> 🪙 **核心金句**：「Agent 有的是知識，缺的是業界時間——時間換來的校準：哪個知識該在什麼時候用、哪些是 cargo-cult、真實組織裡實際會怎樣。」
> 📦 **素材來源**：2026-07-17 做冒煙測試提案時的發現 +（2026-07-02）API 監控找不到書籍良好實踐。

---

## 核心論點

**知識 ≠ 業界時間。** Agent 讀過所有 best practice（知識滿分），但缺「時間換來的校準」：
- 哪條知識**在什麼時候**該用（而非全部背出）
- 哪些「最佳實踐」其實是 cargo-cult
- 真實組織裡**實際會怎樣**（而非書上說該怎樣）

→ 這正是 7/03 挖到的「**難量化能力**」的另一個名字，也正是 AI 最難補的 moat。
→ 接「AI 找 locator、人定 oracle」：**人定的 oracle 背後，就是業界時間。**

---

## 結構草（短，5 拍）

1. **觸發**：我用 Agent 做冒煙測試提案，結構、草稿生得飛快——但我發現它少了一塊。
2. **那塊是什麼**：不是「知識」（它什麼 best practice 都讀過），是「業界時間」——時間換來的校準（which / when / 在這組織這群人行不行）。
3. **兩個具體**：
   - (a) 提案要**落地**，靠的是「這個組織、這群人、這個時機」的 context——那是 Agent 沒有的（呼應〈對的工具用錯時機〉/ 看懂局）。
   - (b) API 監控我找書找不到好實踐、Agent 大概也給不出——**有些領域連整個業界的 aggregate 都還沒累積夠 context，你得自己從做中長出來**（先行者位置）。
4. **為什麼是好消息（moat）**：業界時間 = AI 最難補的、= 難量化能力、= 你的主場（組織/判斷/看懂局）。「AI 取代」焦慮的反面。
5. **深一層**：對前沿/niche 的東西，沒有人（書、Agent）有 context——你就是那個在累積 context 的人。那不是劣勢，是機會。

---

## ⚠️ 去識別
- 冒煙提案 / API 監控講抽象（「一個我在做的監控/提案」），**無公司/部門/產品名**。

## 🔗 關聯
- [ai-finds-locator-human-defines-oracle](ai-finds-locator-human-defines-oracle.md)：人定的 oracle 背後就是業界時間（這篇是那篇的「為什麼人不可取代」上位版）。
- 7/03 coach「難量化能力 / 量錯的尺」（[coach-sessions/2026-07-03](../coach-sessions/2026-07-03-insights.md)）：同一個東西的另一個名字。
- 已發：[ai-as-yes-man](/post/ai-as-yes-man-rd-pm-trust-calibration/)、[如果被 AI 取代我會去讀神學院](/post/ai-replacement-seminary-calling/)（moat / 取代焦慮的反面）。
- 已發：[對的工具用錯時機](/post/right-tool-wrong-time/)（提案落地靠看懂局的 context）。
