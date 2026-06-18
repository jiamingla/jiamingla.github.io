# 醫院電子化的歷史，是 AI 導入的一面鏡子（骨架）

> 📂 **定位**：跨領域類比文骨架。借「醫院電子病歷/HIS 導入」的歷史，照出「AI 導入軟體測試/職場」此刻的陣痛。
> 🎯 **主軸（2026-06-18 user 拍板）**：**導入的陣痛是常態**——初期效率反而下降、人員抗拒，是所有大型工具導入的必經之路，**別用初期的痛去否定方向**。
> 🪧 **素材深度（user 拍板）**：**課堂理論為主**（大學資管系主修修過醫院電子化歷史）。**這是它的優點也是邊界**——當「跨領域類比」夠用，但**不深挖醫療細節、不假裝第一手**。寫作時老實標明「這是我課堂上學到的歷史」。

---

## ⚓ 誠實錨（這篇的寫作姿態）

- 我不是醫療資訊專家，這段歷史來自大學課堂。
- **但類比的價值不在細節精準，在結構同構**——我要主張的是「導入大型工具的痛，跨產業長得一樣」。
- 接 [writing-without-lived-experience](writing-without-lived-experience-honest-stance.md)：**寫思考、不冒充經驗**。把「課堂學到的」當引子，不當權威背書。

---

## 🔑 核心論點：陣痛是常態，不是失敗訊號

> 醫生第一次被要求用電腦打病歷時，效率是**下降**的。打字比手寫慢、流程被改、老醫生抗拒。
> 但沒有人會因此說「電子病歷是錯的方向」——**那只是導入曲線的谷底，不是終點。**

→ 此刻 QA / RD 面對 AI，正站在同一個谷底：prompt 要調、結果要校對、不信任、流程被改。
→ **這篇要替「正在陣痛的人」說話**：你感覺到的慢與亂，是導入曲線的常態，不是 AI 沒用、也不是你不行。

---

## 🪞 同構對照表（主結構）

| 醫院電子化 | AI 導入（軟體測試/職場） |
|---|---|
| 紙本病歷 → 電子病歷，醫生抗拒（打字慢、流程被改） | 手動 → AI，QA/RD 抗拒（不信任、流程被改） |
| 導入初期**效率反而下降**（學習曲線、新舊雙軌並行） | AI 初期也常**先變慢**（prompt 工、校對成本、雙軌驗證） |
| 抗拒的不是「笨」，是**既有流程已經很順、改變有切換成本** | 資深者抗拒不是守舊，是**現行流程確實能跑**（接「別當佈道者」） |
| 熬過谷底後，價值才浮現（可搜尋、可統計、可跨科室） | 熬過谷底後，規模化價值才浮現（跨 N 個 APP、可累積） |

→ ⚠️ 對照表保持**淺而準**——每格都是「結構同構」，不深入醫療技術細節（守住素材邊界）。

---

## 🧩 可延伸、但不一定全寫（看篇幅）

> 以下是醫院電子化還能照出的東西，但**主軸是「陣痛是常態」**，這些當配菜、別喧賓奪主：

- **garbage in garbage out**：電子化≠醫療品質自動提升；爛資料數位化還是爛資料 → AI≠品質自動提升、爛 spec 餵 AI 出爛 case。（這條若展開可獨立成另一篇，別在這篇搶戲）
- **價值在二次利用**：電子病歷真正的價值不在無紙化、在資料可被研究/健保/決策再用 → AI 價值不在自動跑、在規模化+資料累積。（接 [small-team-qa](small-team-qa-content-and-startup-endgame.md) 規模化線）
- **系統給數據、人下判斷**：電子化後醫生仍要判讀，系統不取代醫生 → AI 找 where、人定 oracle。（接 [pom-refactor](pom-refactor-from-runnable-to-maintainable-planning.md) 分工金句 + [pass-fail-not-enough](../source/_drafts/pass-fail-not-enough-for-ai-testing.md)）

---

## ✍️ 結語方向（候選，擇一）

- **A（對正在陣痛的人喊話）**：你現在覺得 AI 又慢又亂，那不是 AI 的失敗、也不是你的失敗，是每一次大型導入都會經過的谷底。醫生熬過了電子病歷，我們也會熬過 AI。
- **B（對推動者的提醒）**：如果你是要推 AI 的人，記得醫院電子化的教訓——**強推會招致抗拒，谷底期的效率下降會被當成失敗的證據**。要的是陪人走過曲線，不是站在山頂喊話。（接「別當佈道者」）

---

## 🔗 關聯

- [writing-without-lived-experience](writing-without-lived-experience-honest-stance.md)：誠實錨、寫思考不冒充經驗。
- [small-team-qa-content-and-startup-endgame](small-team-qa-content-and-startup-endgame.md)：規模化價值線（價值在二次利用那條）。
- [pom-refactor-from-runnable-to-maintainable-planning](pom-refactor-from-runnable-to-maintainable-planning.md)：系統給數據、人下判斷（AI 找 where、人定 oracle）。
- [pass-fail-not-enough-for-ai-testing](../source/_drafts/pass-fail-not-enough-for-ai-testing.md)：AI 結果仍需人判讀。
- 「別當佈道者」線（SDET 篇 / facing-overwhelm）：抗拒是流程已順、不是守舊。
