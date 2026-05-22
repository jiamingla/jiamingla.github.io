# MoT Reply (English) — rethinking-regression-test-value

**Target thread**: https://club.ministryoftesting.com/t/are-we-running-too-many-regressions-than-required/87169
**Original article**: [我們真的跑了太多「無意義」的回歸測試嗎？](/post/rethinking-regression-test-value/)
**Format**: Reply comment (NOT new thread)
**Length**: ~410 words — fits MoT reply norms
**Strategy**: Build on @kinofrost's "fear of large suites" critique, add Sieve Theory framing + 4 actionable questions + accountability angle, link back to Mandarin original for full version.

---

## ✂️ 直接複製下方這段貼到 MoT

I came across this thread after writing a piece in Mandarin on the same question, and @kinofrost's observation about "fear of large suites" really landed for me — it names something I've been trying to articulate.

What I've been calling it (translated from my own writing): **the Sieve Theory**.

Imagine bugs as gravel and sand falling through a funnel:

- **Unit tests** — finest mesh. Should catch ~80% of small logic errors. Cheap, fast, caught at dev time.
- **Integration tests** — medium mesh. Catches the cracks between modules.
- **UI / regression tests** — coarsest mesh. *Should* only catch the "fish that slipped past" on critical paths.

Most bloated regression suites I've seen are bloated because the earlier sieves had holes. We didn't trust our unit/integration coverage, so we built a steel-wire net at the most expensive, slowest, and most fragile layer to compensate. We end up paying for the failures of every prior stage at the UI layer.

A second cost worth naming directly: **a bloated suite erodes RD's trust in QA**. Flaky failures from over-tested UI scenarios get reported as bugs, can't be reproduced, and slowly QA's credibility drains. That 1% irreproducible UI failure you keep filing — it's costing more than the suite costs to maintain.

I now ask myself four questions before adding any regression script:

1. **Diagnosability** — If this fails, can I locate the broken layer within 1 minute?
2. **Redundancy** — Is this function point covered at API or unit level?
3. **Maintainability** — Am I confident I can fix it quickly when the UI changes, without it becoming flaky?
4. **Significance** — If this test disappeared tomorrow, would anyone feel the quality drop?

The hardest part isn't the analysis — it's the **accountability problem**. Deleting a test is technically easy, psychologically much harder. Whoever proposes the cleanup tends to inherit the cleanup work, and if anything goes wrong post-deletion, they own the consequence. Without explicit ownership of "this test exists because X", every test eventually becomes technical debt no one can responsibly remove.

I wrote a longer reflection on this in Mandarin: https://jiamingla.github.io/post/rethinking-regression-test-value/ — happy to dig into any of these threads further.

---

## 📋 翻譯/編輯決策說明（給未來的自己）

### 保留下來的核心

1. **Sieve Theory** 比喻——文章最強的記憶點
2. **四個自問**——actionable，MoT 讀者會直接回應
3. **Accountability problem** 收尾——跟你「無主之地」主張同源
4. **building on @kinofrost**——MoT 文化裡最受歡迎的姿態

### 刻意刪掉的（給未來的自己參考）

1. **約瑟在埃及的智慧** ❌——基督教引用，國際 QA 社群會覺得突兀。**保留在中文原文，不翻**
2. **退伍輔導長 / 教會預算會議** ❌——個人/文化敘事，reply 體裁放不下，會稀釋核心論述。**這部分是中文版的溫度，但英文 reply 不需要**
3. **「品質定心丸」「在團隊裡⋯」** ❌——中文式的個人志向宣言，英文讀起來會過度誠懇/preachy
4. **「你願不願意當那個站出來推動改變的人？」** ❌——中文修辭問句，英文裡會 read 成 inspirational quote，刪
5. **《單元測試的藝術》引用** ❌——書名引用在英文 reply 太繞，主張本身夠強不需要這個權威加持

### 語感調整

- 「我深刻體悟到」→ 直接陳述事實（"the hardest part isn't the analysis"）
- 「微小改變」→ "I now ask myself"（個人動作而非泛泛建議）
- 「論壇建議每個測試都應由專人負責」→ 改成自己的觀察（"Without explicit ownership⋯"）——不要 attribute 給 thread，因為 thread 裡沒人完全這樣講

---

## 🚪 貼之前的最後檢查

- [ ] 看一次連結是不是會跳到正確的中文文章
- [ ] 確認 @kinofrost 在原 thread 裡的 username spelling（小心 case sensitivity）
- [ ] **不要在貼出後立刻刪掉編輯**——MoT 小社群會被注意到
- [ ] 貼完關掉瀏覽器，不要追蹤前 6 小時（避免一直 refresh 焦慮）
- [ ] 兩週內不再看 → 設個行事曆 6/4 回來看反應就好

---

## 🔄 未來如果想做完整英文翻譯（給自己留條路）

如果這篇 reply 得到正向回應，可以考慮做**英文版完整 blog mirror**——當時要保留的東西：
- 約瑟引子（**保留**——blog mirror 可以有作者個性）
- 退伍輔導長 / 教會故事（**保留**——這是中文版的溫度，英文版完整篇也該有）
- 《單元測試的藝術》引用（**保留**——blog post 體裁夠長可以承載）

→ 這時候才動，現在不用先寫。一步一步來。
