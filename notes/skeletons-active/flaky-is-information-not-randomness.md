# 〈flaky 不是隨機，是資訊：一個「社群頁閃退」的偵探故事〉骨架

> 📂 **定位**：線一 PDT。flaky 當成待解讀的訊號，不是噪音。
> 🪙 **核心金句**：「flaky 不是噪音，是還沒被解讀的訊號。retry 是最後手段，不是第一反應。」
> 📦 **素材來源**：smoke docs `mike-customer-service-overlay.md`（+ 近期 commit：Compose recompose 的 StaleElement 重抓）。

---

## 核心論點

遇到 flaky 的兩種反應：
- **蓋過去**：加 retry，讓它變綠。→ 資訊被丟掉。
- **解讀**：問「它在什麼條件下才發生」。→ 常挖到真問題。

**偵探故事（真實）**：某案例只在「連續跑一整輪」時偶爾失敗、單獨跑不重現。不是隨機——是**自動化連跑太快、累積觸發了行銷推播的條件**，推播在特定頁 fire 出一個客服頁覆蓋。用 logcat 找 intent 來源 uid，證明是 App 自己發的、不是測試誤點。

→ 「單跑不重現、連跑才壞」本身就是線索：指向「**累積狀態**」而非隨機。

（次要案例：Compose 畫面 recompose 造成的 StaleElement flaky——正解是「重抓一次」而非 sleep，也是「理解成因再對症」而非蓋過去。）

---

## 結構草

1. flaky 的兩種處理（蓋 vs 解讀），先講立場
2. 偵探過程：單跑不重現 → 連跑才發 → logcat 追來源 → 累積觸發
3. 根因：不是隨機，是「連跑」這個條件本身
4. 次案例：Compose recompose 的 stale（重抓 vs sleep）
5. 收：flaky 是資訊；retry 只在「已理解成因、確認可容忍」後才用

## ⚠️ 去識別
- 行銷 SDK（AIQUA/Appier）、app 名、客服網域、同事名去掉；框成「一個會跳推播的 App」。

## 🔗 關聯
- 線一 PDT；呼應 [boredom-is-a-signal](/post/boredom-is-a-signal/)、[app-broken-is-misattribution](app-broken-is-misattribution-diagnosis-layers.md)（同屬「準確歸因」家族）。
