# 〈「App 壞了」常常是誣賴——一套從後端到 GPU 的診斷分層〉骨架

> 📂 **定位**：線一 PDT（診斷）+ 線三。把「問題驅動」用在「這到底是誰的錯」。
> 🪙 **核心金句**：「後端 200 + 無例外 + 非 OOM + 有 EGL 錯誤 = 環境問題，不是 APK。」「最快的證偽法：換一台（尤其實體機/真 GPU）跑跑看。」
> 📦 **素材來源**：smoke docs `gpu-blank-and-physical-device.md`、`mike-customer-service-overlay.md`、`ci-troubleshooting.md`。三個真實案例。

---

## 核心論點

「App 壞了/測試壞了」是最容易被誤判的結論。真相常在別層——**先分層診斷是誰的錯，再動手。**

**三個真實案例（各自對應一層）：**

1. **GPU 空白屏 ≠ APK 壞**：某 App 在模擬器整片黑，但 logcat 顯示後端回 200、無 FATAL exception、記憶體充足（非 OOM）、只有 `EGL_BAD_MATCH` GL 繪製錯 → 是**內顯模擬器的 GPU 繪製撐不住**，換實體機（真 GPU）完全正常。判準：GPU-heavy（列表/Compose）在內顯特別容易踩。
2. **假失敗 ≠ crash**：某案例連跑時偶爾失敗、報「頁面元素找不到」，但 process 還活著 → 其實是被**行銷推播的客服頁覆蓋**。診斷法：logcat 找那個 Activity 的 intent 來源 uid，證明是 App 自己發的、不是測試誤點。
3. **本地能跑、CI 不能 ≠ 腳本錯**：環境差異（見另一篇 CCT vs WebView）。

---

## 結構草

1. 開場：一句「app 壞了」背後可能藏著幾層完全不同的真相
2. 診斷分層：App 邏輯層 / 環境層（GPU、瀏覽器）/ 覆蓋層（別的東西蓋上來）
3. 三個案例各拆一段（怎麼一步步排除到真因）
4. 給讀者的**判準清單**：後端狀態？有無 exception？是否 OOM？有無 GL 錯？換台重現嗎？
5. 收：QA 的價值不在「回報壞了」，在「準確歸因是哪一層壞」

## ⚠️ 去識別
- app 名、公司、行銷 SDK 名（AIQUA/Appier）、客服網域（firstline）、同事名**全去掉**。
- 案例抽象成「一個列表很重的 App」「一個會跳推播的 App」。

## 🔗 關聯
- 線一 PDT（診斷即提問）；呼應 [boredom-is-a-signal](/post/boredom-is-a-signal/)（煩是診斷工具）。
- 技術細節接 [local-runs-ci-fails-environment-diff](local-runs-ci-fails-environment-diff.md)（案例 3 展開）。
