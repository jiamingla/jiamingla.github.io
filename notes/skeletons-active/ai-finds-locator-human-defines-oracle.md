# 〈AI 找 locator、人定 oracle：一個單兵 QA 的 AI 分工中場報告〉骨架

> 📂 **定位**：線二（AI 測試）+ 線三。**有真框架撐的誠實中場報告**（非成功案例）。
> 🪙 **核心金句**：「『找 locator』可以越來越自動；但『告訴 AI 產品真相』和『驗證 AI 沒錯』，是人的責任主場。」
> 📦 **素材來源**：smoke docs `ai-role-and-human-steps.md`、`three-architectures-vs-ai.md`。真實在跑。

---

## 核心論點

在一套真的在跑的冒煙框架上，AI 與人的分工實際長這樣：

| AI 實際接手（機械 / 可窮舉） | 人不可取代（判斷 / oracle） |
|---|---|
| 在 XML 裡找/校正 locator、harness 小改、部分診斷 | 提供 ground truth（這頁該長怎樣、該不該有此功能）、下決策、**驗證 AI 沒幻覺**、跨人協調、環境/帳號一次性設定 |

- 直覺以為「AI 幫的是找 locator」，其實那塊最機械、最該給 AI；**AI 真正的能力邊界在「產品真相」與「判斷對錯」**——那才是人寫進 runbook 的部分。
- **誠實框架**：這是「進行中的實驗中場報告」，不是「導入成功」。有些 case AI 就是做不到（見 oracle 缺失）。
- **reframe**：AI 不是取代 QA，是把 QA 從「靠手工資本」升格為「餵真相 + 驗結果 + 扛責」的工具箱——人沒被替換，是被從勞力升到判斷。

---

## 結構草

1. 場景：把一個新 App 從零弄到冒煙全綠，AI 到底幫了哪幾步
2. AI 接手了什麼（機械層）+ 為什麼該給它
3. 人留下什麼（oracle 層）+ 為什麼不可交
4. **縮短迴圈的做法**：第一次校正時把「這頁的真相」寫進測項註解 → AI 下次自己判（把 ground truth 資本化）
5. 誠實中場報告：還沒接的、AI 仍做不到的

## ⚠️ 去識別
- app 名去掉；用「一套服務多個 App 的單兵冒煙框架」。

## 🔗 關聯
- 接 [pom-refactor](../skeletons-done/pom-refactor-from-runnable-to-maintainable-planning.md)（分工金句）、[pass-fail](../skeletons-done/ai-test-result-schema-planning.md)（oracle/信心維度）。
- 是「100% 開發 100% 測試」衍生篇的實證版（見 pass-fail 規劃檔衍生篇）。
- **也是未來 Test Corner talk 的核心素材**（見 test_corner「先導入一塊再講」決定）。
