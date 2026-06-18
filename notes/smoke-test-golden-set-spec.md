# 核心冒煙測試 Golden Set 實作規格

**建立日期**：2026-06-02  
**狀態**：🟡 Pilot 進行中（app_a 完成，app_b 進行中）→ **2026-06-17 更新：真實版已長到 7 個 APP / 4 種架構**（見 `AutoTesting/Author/smoke_script/README.md`）  
**來源**：[brand-value-and-smoke-test-proposal.md](brand-value-and-smoke-test-proposal.md) 第十節  
**技術環境**：Python + Pytest + Appium，獨立 `smoke_script/` 目錄，與現有回歸測試目錄分離

---

## ✍️ 寫作用途（2026-06-17 新增）：這份 spec 幾乎就是可發布的技術文骨架

**這份 spec 已經是去識別版（app_a/b/c、com.example.*）**——是「真實 README（7 個作者 APP、CMoney 統一登入、ChipK）」對外安全的雙胞胎。**直接拿這份的措辭當文章基底，不必再洗一次指紋。**

可發展成的文章（線三技術 + 線十二單兵 + 線二 AI×POM）：

| 角度 | 賣點 |
|---|---|
| **〈一套 POM 服務 N 個 APP：冒煙測試框架實戰〉** | 「框架是常數、adapter 是變數」；7 APP / 4 架構、`pages/` 一行未改——[pom-refactor](pom-refactor-from-runnable-to-maintainable-planning.md) 的真實案例 |
| **〈冒煙測試是 AI 規模化的地基〉** | 接 [facing-overwhelm 回歸 vs 冒煙](facing-overwhelm-via-steelmanning-regression-vs-smoke.md)：冒煙不取代回歸、是給 AI 跑回歸的高信賴度基準線。「給 AI 半小時調定位器、人工 review」 |
| **〈單兵 QA 怎麼用一套冒煙框架撐住 N 個產品〉** | [small-team / 新創第一位 QA](small-team-qa-content-and-startup-endgame.md) 的**真實單兵實證**——駁「我沒單兵經驗」（見 [writing-without-lived-experience](writing-without-lived-experience-honest-stance.md)） |
| **xfail ≠ skip：已知 bug 的誠實記錄** | 接 [proving-a-bug-is-gone](proving-a-bug-is-gone-verification-philosophy.md)：xfail 是「已知、有記錄、預期失敗」；XPASS = RD 修好了的訊號 |

→ **這份 spec + brand-value 提案（向上管理面）+ README（技術細節）= 一個主題的三個切面**，挑一個角度就能成文。

---

## 一、Pilot 範疇

### APP 覆蓋狀況

| 代號 | 狀態 | 完成案例 |
|---|---|---|
| app_a | ✅ 完成 | S01–S11 全過 |
| app_b | 🔄 進行中 | locators 建置中 |
| app_c | 待排 | — |

### 設計原則
- 新框架獨立於現有回歸測試目錄，兩者不互相汙染
- 跨平台預留：`locators/android/` 已完成，`locators/ios/` 後補
- 新增 App 只需補 1 份 locators + 1 份 app_config，不動 pages 和 tests

---

## 二、Golden Set：核心路徑清單（以 app_a 為基準）

### P0 — 生死線（任何版本都必須過）

| ID | 路徑名稱 | 驗證點 |
|---|---|---|
| S01 | App 啟動 | 底部 tab bar 首次出現 |
| S02 | 首頁渲染 | 主要內容容器 + 資料載入 |
| S03 | 登入狀態 | 已登入（鈴鐺 / 用戶識別元素可見）|
| S06 | 行情頁 Tab | 行情主頁面容器渲染 |
| S07 | 社群頁 Tab | 社群頁初始渲染 |
| S08 | 內容頁 Tab | 內容頁面容器渲染 |
| S09 | 更多頁 | 更多頁標題 + 個人資料卡片 |
| S11 | 行情 → 個股頁 | 點入個股，個股頁可達 |

### P1 — 核心功能入口

| ID | 路徑名稱 | 驗證點 |
|---|---|---|
| S04 | 搜尋頁可達 | 搜尋頁正確渲染 |
| S05 | 通知頁可達 | 通知頁正確渲染 |

### P2 — xfail（已知缺陷，等 RD 修復）

| ID | 路徑名稱 | 說明 |
|---|---|---|
| S99 系列 | 已知 bug 路徑 | 用 `@pytest.mark.xfail` 標記，不計入失敗；修復後移至 P0/P1 |

> **xfail ≠ SKIP**：xfail 代表「已知、有記錄、預期失敗」。若 xfail 意外通過（XPASS），代表 RD 已修復，需立即升為正式 case。

---

## 三、技術實作規格

### 3.1 目錄結構

```
smoke_script/
├── locators/
│   ├── android/{app}_locators.py   # Android XPath，每個 App 一份
│   └── ios/{app}_locators.py       # iOS locators（後補）
├── pages/                          # 跨平台 POM，平台無關
│   ├── base_page.py                # 共用操作（find, tap, ensure_at_home）
│   ├── home_page.py
│   ├── stock_page.py               # 含「行情頁 → 個股頁」邏輯
│   └── ...
├── app_config/{app}.json           # App package name 等設定
├── page_factory.py                 # 依 --app 參數注入對應 locators
├── driver_factory.py               # Appium driver 建立
├── conftest.py                     # Pytest session fixture + App 狀態恢復
├── pytest.ini
└── tests/
    ├── test_s01_app_launch.py      # S01–S11 每個 case 一支檔
    ├── ...
    └── test_s99_*_xfail.py        # S99 系列，xfail 標記
```

**核心設計**：`page_factory.py` 根據 `--app` 參數注入對應 locators；`pages/` 不感知具體 App。新增 App 只需補 `locators/` + `app_config/`，不改框架。

### 3.2 新增 App 步驟

這段流程可交由 AI（如 Claude）輔助——提供 App 的 XML dump，AI 協助找出所有 locators，省去人工逐一比對的時間。

**Step 1：建 app_config（5 分鐘）**
```json
// app_config/app_b.json
{
    "app_b": {
        "chinese": "（App 中文名）",
        "app_package": "com.example.app_b",
        "app_activity": "com.example.app_b.LaunchActivity",
        "category": "stock"
    }
}
```

**Step 2：建 Android locators（30–60 分鐘，可交給 AI）**
```python
# locators/android/app_b_locators.py
class AppBAndroidLocators:
    tab_home = Locator(By.XPATH, '...')
    # NavBar、底部 Tab、首頁內容...
```

命名規則：`locators/{platform}/{app}_locators.py` → class `{PascalApp}{Platform}Locators`

**Step 3：執行確認**
```bash
pytest smoke_script/tests/ -v -s --app app_b -m P0
```

### 3.3 Pass / Fail / xfail 判斷

| 狀態 | 定義 |
|---|---|
| PASS | 驗證元素在 timeout 內出現 |
| FAIL | timeout 超時或 App crash |
| xfail | 已知 bug，預期失敗（不計入 FAIL 數）|
| XPASS | xfail 意外通過，代表 RD 已修復 → 升為正式 case |
| ERROR | 非預期例外（Appium 斷線、環境問題）|

### 3.4 Timeout 設定

| 步驟類型 | Timeout |
|---|---|
| App 啟動 | 10s |
| 頁面切換 | 5s |
| 元素出現 | 5s（沿用 `find_element_until_visible` 預設）|

---

## 四、執行方式

```bash
# 跑預設 App（app_a）
pytest smoke_script/tests/ -v -s

# 跑其他 App
pytest smoke_script/tests/ -v -s --app app_b

# 只跑 P0（生死線，最快）
pytest smoke_script/tests/ -v -s -m P0

# 未來 iOS
pytest smoke_script/tests/ -v -s --platform ios --device <UDID>
```

---

## 五、群組回報範本（人工貼，不自動發送）

```
【冒煙測試 🟢🔴】2026-06-02 v1.x
✅ app_a  P0+P1 全過（S01–S11）
🔴 app_b  S06 行情頁 FAIL（等 RD 確認）
⚪ app_c  尚未加入

核心功能目前狀態已回報，邊界風險決策交 PM。
```

---

## 六、維護規則

| 情境 | 動作 |
|---|---|
| 新 App 加入 | 補 `app_config/` + `locators/android/`，跑 P0 確認 |
| UI 改版 locator 失效 | 改 `locators/android/{app}_locators.py`，pages 和 tests 不動 |
| 出現新的已知 bug | 加 S99 系列 test + `@pytest.mark.xfail`，不要 skip |
| XPASS（xfail 意外通過）| 把該 case 移出 S99，升為正式 P0/P1 |
| 全套跑超過 5 分鐘 | 拆為 P0 獨跑（`-m P0`），CI 跑 P0、手動跑 P1 |

**維護底線**：Golden Set 失效比沒有 Golden Set 更危險。已知問題用 xfail 記錄，不要靜默略過。

---

## 七、Pilot 完成定義（DoD）

- [x] app_a S01–S11 全部通過，無 ERROR
- [x] xfail 機制驗收：S99 正確標記為已知 bug
- [x] `--app` 參數與 `page_factory.py` 注入機制運作正常
- [ ] app_b S01–S03（P0）通過
- [ ] app_b locators 完成後跑完 S01–S11
- [ ] 至少一次「真實 FAIL」情境驗收輸出格式

---

## 八、相關連結

- [brand-value-and-smoke-test-proposal.md](brand-value-and-smoke-test-proposal.md) — 提案背景與攻防腳本
- [cross-app-locator-strategy.md](cross-app-locator-strategy.md) — 元素定位三階段策略
- [sole-qa-bottom-up-automation.md](sole-qa-bottom-up-automation.md) — 影子自動化生存策略
