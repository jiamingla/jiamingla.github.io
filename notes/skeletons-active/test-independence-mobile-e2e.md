# 〈單獨跑都過，合在一起跑就垮——手機 E2E 的測試獨立性〉骨架

> 📂 **定位**：線三/五（技術實戰/自動化設計）。**有真實踩坑故事的 how-to**，SEO 長尾強。鐵人賽 Day-2x 診斷實戰群。
> 🪙 **核心金句**：「進場先問『我可能被丟在任何地方』，而不是『我應該在某頁』。」／「手機 E2E 不是單元測試——一條 driver、一次登入、一台裝置、一份帳號狀態從頭用到尾。」
> 📦 **素材來源**：smoke docs `pytest-test-independence.md`（2026-07-17 兩 app 合併回歸首跑的真實踩坑）。

---

## 核心論點

單元測試每個 case 起於乾淨記憶體；**手機 E2E 不是**——共用一條 driver、一次登入、一台裝置、一份持久的後端帳號狀態。前一個測試把 App 留在某畫面/留下資料，會污染後一個。

→ 獨立性 ≠ 不共用 driver（太貴）。獨立性 = **每個測試進場時主動把環境喬回自己要的已知狀態；離場時把自己造成的副作用清乾淨。**

**最好的鉤子**：「單獨跑都過、合在一起跑就垮」——這現象超多人踩過。單獨跑是單元、合併跑才是整合，合併跑正是戳破「每個檔單獨綠」假象的價值。

---

## 結構草（blog 版要比原 doc 精簡——挑 3-4 個最有感的手法）

1. **鉤子 + 現象**：一堆案子單獨跑全綠、合併跑一片 skip/fail（真實故事，抽象化）。
2. **為什麼手機 E2E 特別容易互相污染**：App 是個大狀態機，case N 留在哪、case N+1 就從哪開始。
3. **核心手法（挑最 CP 值的講，別七個全展開）**：
   - ①**進場先 reset 再導航、絕不假設起點**（最重要）：先退回已知狀態（逐層 BACK 回底部 tab）再導航。口訣在金句。
   - ②**teardown 即使測試中途爆掉也要收得乾淨**：清理放 fixture yield 之後（不放 body 尾）、用可辨識的拋棄式命名、帳號級 reset 當最後保險。
   - ③**不依賴執行順序**：任何順序/單獨/合併都要過；可用隨機順序（pytest-randomly）逼出隱藏依賴。
   -（其餘：真陽性 is_at_X、冪等清殘留 loop 到不剩、fixture scope 分對、副作用只在拋棄式資料——可壓成一段帶過或做延伸清單）
4. **收尾清單**：新增一個測試 class 的獨立性檢查清單（原 doc §3 很好、直接改寫）。

---

## ⚠️ 去識別（這篇指紋重）
- app 名（hermit / ruanmuhua）、case id（M001/wl003/cm006/r003…）、測試群組名（QA回歸暫存…）、`cmqa-mcp` / `reset_stock_watchlist` 工具名——**全去掉或抽象**（「一個自選股 CRUD 的測試」「帳號級重置工具」）。
- 現象講「兩個 App 合併回歸」即可，不點名。

## 🔗 關聯
- 診斷家族：[app-broken-is-misattribution](app-broken-is-misattribution-diagnosis-layers.md)（是誰的錯）、[flaky-is-information](flaky-is-information-not-randomness.md)（flaky=資訊）——本篇是「狀態污染/順序依賴」那一種，跟前兩者互補不重疊。
- [pom-refactor](../skeletons-done/pom-refactor-from-runnable-to-maintainable-planning.md)（測試架構/POM）。
