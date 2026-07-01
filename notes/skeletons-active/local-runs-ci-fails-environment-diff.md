# 〈本地能跑、CI 不能跑：多半是環境差異，不是你的腳本錯〉骨架

> 📂 **定位**：線三（技術實戰）。
> 🪙 **核心金句**：「CI 出問題，先問『這台跟我本機哪裡不一樣』，再問『我腳本哪裡錯』。」
> 📦 **素材來源**：smoke docs `ci-troubleshooting.md`（+ `ci-jenkins-reference.md`）。

---

## 核心論點

CI 壞掉的通例是**環境差異**，不是腳本錯。最深的案例：

**本地能登入、共用機不能**——同一份腳本、同一個 App。根因是**登入頁跑在不同的瀏覽器容器**：
- 本地沒有 Chrome Custom Tab 提供者 → App 走 in-app WebView（同進程、Appium 可注入、能登）。
- 共用機有完整 Chrome → App 走 Custom Tab（別的進程、注入被擋、locator 也對不上）。
- 解法：用 root **只停用 Chrome 的 CCT 元件**（`CustomTabsConnectionService`），保留 WebView 引擎——不是停整個 Chrome（會連 WebView 一起殺）。

**其他環境差異**：adb 高 index 實例連不到（埠＝5555+index×2，要手動 connect）；共用機沒有 `uv`（改用 `sys.executable`）；`schtasks` 起模擬器（Jenkins 服務跑在無桌面的 session 0，GUI 模擬器起不來）。

→ 共同教訓：**無人介面的 CI，可觀測性（串流 log、失敗自動 dump 畫面+activity）是必需**，否則每次除錯都在瞎子摸象。

---

## 結構草

1. 一句總心得：本地能跑 CI 不能，先列「環境差異清單」
2. 深案例：CCT vs WebView（為什麼同腳本一台能登一台不能）
3. 其他環境差異快列（adb 埠 / uv / session 0）
4. 可觀測性：CI 無人看畫面，log 串流 + 失敗 dump 是保命
5. 給讀者：CI 排查 checklist（先環境、後腳本）

## ⚠️ 去識別
- 公司、機器名、帳號、內部 IP 去掉；技術細節（CCT 元件名、adb 埠公式）可留（通用知識）。

## 🔗 關聯
- 線三；接 [app-broken-is-misattribution](app-broken-is-misattribution-diagnosis-layers.md)（環境層是誤判來源之一）。
