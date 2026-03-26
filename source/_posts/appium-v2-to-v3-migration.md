---
urlname: appium-v2-to-v3-migration
title: 【技術升級】Appium 3.0 來了！從 v2 遷移至 v3 的核心重點與避坑指南
date: 2026-03-26 14:00:00
tags: [Appium, 自動化測試, 測試開發, Test Automation, 升級筆記]
---

就在我們還在習慣 Appium 2.0 的獨立 Driver 安裝架構時，**Appium 3.0** 已經正式進入大家的視野。

這次的升級並不像從 v1 到 v2 那樣有翻天覆地的架構改變，但卻有幾個針對「現代化」與「安全性」的關鍵修正。如果你正在考慮將團隊的自動化框架升級，這篇筆記能幫你快速掌握遷移重點。
> 參考資料：[Appium 官方遷移指南 (v2 to v3)](https://appium.io/docs/en/latest/guides/migrating-2-to-3/)

### 1. 為什麼要升級？Appium 3 的核心哲學
Appium 3 延續了 v2 的「插拔式」精神，但更進一步地移除了許多過時的依賴，並強化了對最新行動作業系統（iOS 18+, Android 15+）的支援穩定性。

**最主要的變化在於：**
* **Node.js 版本要求：** Appium 3 建議（甚至在某些環境下要求）使用更高的 Node.js LTS 版本。
* **安全性增強：** 針對內部 API 進行了重構，減少了潛在的安全漏洞。

---

### 2. 遷移四大重點 (Migration Checklist)

根據官方文件，以下是我們在遷移時必須檢查的項目：

#### A. 驅動程式 (Drivers) 與外掛 (Plugins) 的更新
Appium 3 需要對應版本的 Driver。升級後，請記得執行以下指令來更新你的核心驅動：
```bash
appium driver update uiautomator2
appium driver update xcuitest
```

#### B. 移除過時的 Capabilities
一些在 v2 已經標註為過時（Deprecated）的參數，在 v3 可能會直接失效。建議全面檢查並改用 appium:options 的巢狀結構來定義 Capabilities。

#### C. 腳本相容性：WebDriver 協議
Appium 3 完全擁抱 W3C WebDriver Protocol。如果你的腳本中還殘留舊式的 JSON Wire Protocol 寫法，升級後可能會遇到定位失效或連線中斷的問題。

#### D. Plugin 的重大變更
有些在 v2 廣泛使用的 Plugin 可能需要升級到 v3 相容版本，否則在啟動伺服器時會報錯。

### 3. 實戰避坑：關於 Images Plugin 的血淚經驗
這是這次升級中最具體的一個坑。如果你的專案有用到 Images Plugin（影像比對定位），請特別注意版本號：

版本陷阱： 實測發現 appium-images-plugin 3.x 版本在環境適配上有些問題。

目前的解決方案： 建議將版本鎖定在 4.1.1，在目前的測試環境中相對穩定。

隱憂： 雖然 4.1.1 解決了安裝問題，但在 Appium v3 環境下，似乎存在「長時間運行會突然掛掉」的穩定性疑慮。這部分我還在持續觀察中，建議若非必要，先在 Dev 環境跑一段時間的壓力測試。

### 4. 其他建議
備份 Node Modules： 在執行 npm install -g appium@next 前，確保知道如何降級。

Client 端同步： 伺服器升級後，Appium-Python-Client 等客戶端也需同步更新，避免通訊協定不匹配。

善用 Appium Inspector： 定位不到元素時，先開 Inspector 檢查 DOM 結構是否因 Driver 更新而變動。

### 結語
Appium 3 象徵行動自動化進入更精簡的時代。雖然為了穩定性（如上述的 Images Plugin 問題）可能需要花時間調整，但長遠來看是值得的投資。

你已經開始嘗試 Appium 3 了嗎？或是升級過程中遇到了什麼卡關的地方？歡迎在下方留言，我們一起拆解問題！