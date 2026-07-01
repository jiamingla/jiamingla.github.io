# 〈可維護性 = AI 要修改的最小單位有多小——三種測試架構的 AI ROI〉骨架

> 📂 **定位**：線三 + 線二。AI 時代的測試架構觀。
> 🪙 **核心金句**：「一個測試架構對 AI 友不友善，取決於『AI 要改它時，最小定位有多小、牽連有多大』。」
> 📦 **素材來源**：smoke docs `three-architectures-vs-ai.md`。三架構實比。

---

## 核心論點

比較三種真實架構：
- **兩個巨石 lib**（單檔 5503 / 6182 行、inline xpath + 全域 id table）：UI 一改，AI 要讀進很大的 context、牽連高、改一處怕動全身。
- **乾淨 POM 冒煙框架**（per-app locator ~130 行、關注點分離）：改一個 App 只動一個檔、零牽連。

→ **「AI 能不能維護」不是看你用了多少 AI，是看 locator 能不能被單獨修。** self-healing（AI 自動修）幾乎**只在乾淨架構可行**；巨石 lib 等於把 AI 卡進一台難維護的引擎。

**給 QA Head 的判準**：評估一個架構的「AI 友善度」，不要問「用了多少 AI」，要問「**AI 要修改它，最小定位多小、牽連多大**」。

---

## 結構草

1. 三架構硬事實表（行數 / 關注點分離 / id 管理）
2. AI 的介入點差在哪（巨石：卡在 runtime 相依裡；乾淨：locator 可獨立餵/改）
3. 為什麼 self-healing 只在乾淨架構成立
4. 判準：問「最小修改單位」，不是「用多少 AI」
5. **誠實**：新框架目前只有「廣度」，深度（視覺 diff / K 線 / 策略）還沒接——乾淨是「刪掉冗餘」換來的，不是功能更多

## ⚠️ 去識別
- 架構討論相對安全；lib 名、公司、app 名去識別。誠實標明深度資產仍在舊 lib。

## 🔗 關聯
- 接 [pom-refactor](../skeletons-done/pom-refactor-from-runnable-to-maintainable-planning.md)、[ai-finds-locator-human-defines-oracle](ai-finds-locator-human-defines-oracle.md)。
- 是「100% 開發 100% 測試」衍生篇的架構面（見 pass-fail 規劃檔）。
