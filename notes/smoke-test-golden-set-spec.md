# 核心冒煙測試 Golden Set 實作規格

**建立日期**：2026-06-02  
**狀態**：🚀 實作中（Pilot 階段）  
**來源**：[brand-value-and-smoke-test-proposal.md](brand-value-and-smoke-test-proposal.md) 第十節  
**技術環境**：Python + Appium，沿用作者 APP 系列現有測試 lib

---

## 一、Pilot 範疇

### 選 APP 的原則（2–3 個先跑）
從作者 APP 系列中選出能代表兩種 XML pattern 的 APP：

| APP 角色 | 選定條件 | locator pattern |
|---|---|---|
| APP A（標準型）| NavBarTitleComponent-Text 自帶 text | Phase 1 fallback chain 主幹 |
| APP B（包裝型）| CustomNavBar-CenterComponent 容器 | Phase 1 fallback chain 備援 |
| APP C（選填）| 已知有個別怪癖（per_app_quirks.md 有記錄）| config override 驗證 |

> **填入欄位**（實作時補，此處以代號標示）：
> - APP A（app_a）= ___________
> - APP B（app_b）= ___________
> - APP C（app_c）= ___________ （可省略）

---

## 二、Golden Set：每個 APP 必測的核心路徑

優先順序由上往下，**先把 P0 跑通，再往下加**。

### P0 — 生死線（任何版本都必須過）

| ID | 路徑名稱 | 驗證點 | pass 條件 |
|---|---|---|---|
| S01 | App 啟動 | App 能被 Appium 啟動、不 crash | 首個畫面出現在 3 秒內 |
| S02 | 主頁可達 | 首頁 / 大廳 tab 可正常渲染 | 主要內容容器出現 |
| S03 | 登入 / 已登入狀態 | 使用者身份可被辨識 | 顯示用戶識別元素（頭像、名稱、bell icon 任一）|

### P1 — 核心功能線（商業價值最高的 1–2 條）

根據各 APP 的主要商業功能填入，例：

| ID | 路徑名稱 | 描述 |
|---|---|---|
| S04 | 搜尋功能可用 | 點搜尋進入搜尋頁、頁面可正確渲染（`is_at_search_page` pass）|
| S05 | 通知頁可達 | 點鈴鐺進入通知頁（`is_at_notification_page` pass）|
| S06 | ＿＿＿＿（各 APP 自定）| 各 APP 最核心的一條商業動線 |

> S06 是各 APP 的「靈魂路徑」，由你根據業務判斷填入（例：查看個股資訊、發文進入編輯頁等）。

### P2 — 進階守備（後期再加，不急）

| ID | 路徑名稱 | 備註 |
|---|---|---|
| S07 | 貼文內容頁可達 | 從主頁點入任意文章，確認頁面標題正確渲染 |
| S08 | 登出 → 重新登入 | 驗證 session 失效後能重取 |

---

## 三、技術實作規格

### 3.1 測試結構

```
smoke_tests/
├── conftest.py            # Appium session setup / teardown
├── run_smoke.py           # 主入口：選 APP → 跑 Golden Set → 輸出摘要
├── cases/
│   ├── s01_app_launch.py
│   ├── s02_home_reachable.py
│   ├── s03_login_state.py
│   ├── s04_search_page.py
│   ├── s05_notification_page.py
│   └── s06_core_flow.py   # 各 APP 自定，透過 config 注入
└── reporters/
    └── summary.py         # 輸出 pass/fail 摘要
```

### 3.2 執行方式

```bash
# 跑單一 APP（傳入 author name，對應 config.json 的 key）
python run_smoke.py --app app_a

# 跑 Pilot 全部 APP
python run_smoke.py --app app_a app_b app_c

# 只跑 P0（最快）
python run_smoke.py --app app_a --level P0
```

### 3.3 定位策略

- **直接複用既有 page object 和 fallback chain**（不另起爐灶）
- `is_at_X` 系列方法已支援兩種容器寫法，直接呼叫
- APP 特例透過 `config.json` 的 per-APP override 接住（同現有架構）
- 若某 APP 的某步驟 fallback chain 全部 miss → 記錄到 quirk log，先跳過、不 block 整跑

### 3.4 Pass / Fail 判斷

| 狀態 | 定義 |
|---|---|
| PASS | 驗證點在 timeout 內被找到 |
| FAIL | 驗證點 timeout 後仍不存在，或 App crash |
| SKIP | 該 APP 已知 quirk 尚未支援（須在 per_app_quirks.md 有記錄）|
| ERROR | 非預期例外（Appium 連線中斷、環境問題）|

SKIP ≠ FAIL，SKIP 代表「已知、有記錄、刻意放行」。

### 3.5 Timeout 設定

| 步驟類型 | Timeout |
|---|---|
| App 啟動 | 10s |
| 頁面切換 | 5s |
| 元素出現 | 5s（沿用 `find_element_until_visible` 預設）|

**全套 P0 目標在 2 分鐘內跑完；P0+P1 在 5 分鐘內**。

---

## 四、輸出規格

### 4.1 Console 摘要（每次執行結束輸出）

```
===== Smoke Test Summary — 2026-06-02 14:23 =====
APP: app_a
  S01 App 啟動          PASS  (1.2s)
  S02 主頁可達          PASS  (2.1s)
  S03 登入狀態確認      PASS  (0.8s)
  S04 搜尋頁可達        PASS  (1.5s)
  S05 通知頁可達        FAIL  ← 建議退件或告知 PM 風險

APP: app_b
  S01 App 啟動          PASS  (1.1s)
  S02 主頁可達          PASS  (1.9s)
  S03 登入狀態確認      SKIP  (quirk: login_check_xpath_not_defined)
  ...

Overall: 7 PASS / 1 FAIL / 1 SKIP / 0 ERROR
```

### 4.2 群組回報範本（人工貼上，不自動發送）

```
【冒煙測試 🟢🔴】2026-06-02 v1.x
✅ app_a  P0+P1 全過
🔴 app_b  S05 通知頁 FAIL（等 RD 確認是否已知）
⚪ app_c  SKIP（S03 尚未支援）

核心功能目前狀態已回報，邊界風險決策交 PM。
```

> 「核心功能我保證，邊界風險由 PM 決策」——責任邊界透明化。

---

## 五、維護規則

| 情境 | 動作 |
|---|---|
| 新 APP 加入系列 | 在 `config.json` 加 entry；先跑 P0，S06 稍後補 |
| APP UI 改版導致 locator 失效 | 先更新 `per_app_quirks.md`，再改 config override 或 page method |
| 某 APP 長期 SKIP 超過 3 項 | 升 Phase 2（抽 per-APP LocatorStrategy，見 cross-app-locator-strategy.md）|
| 整套跑超過 5 分鐘 | 刪 P2、只留 P0+P1；或改為 APP 分批執行 |

**維護底線**：Golden Set 失效比沒有 Golden Set 更危險。寧可先 SKIP 有記錄，不要靜默 FAIL。

---

## 六、Pilot 完成定義（DoD）

本週 Pilot 結束的驗收條件：

- [ ] APP A 的 S01–S05 能在 CI 本地跑完，無 ERROR
- [ ] APP B 的 S01–S03 能跑完（允許 S04/S05 SKIP if locator 未對齊）
- [ ] `run_smoke.py` 能接受 `--app` 參數並輸出 Summary
- [ ] 至少跑過 1 次「真正失敗」的情境（手動讓 S02 fail 驗收 FAIL 輸出）
- [ ] per_app_quirks.md 已記錄本次發現的所有 SKIP 原因

---

## 七、相關連結

- [brand-value-and-smoke-test-proposal.md](brand-value-and-smoke-test-proposal.md) — 提案背景與攻防腳本
- [cross-app-locator-strategy.md](cross-app-locator-strategy.md) — 元素定位三階段策略
- [sole-qa-bottom-up-automation.md](sole-qa-bottom-up-automation.md) — 影子自動化生存策略
- `per_app_quirks.md` — 各 APP 已知 locator 差異 catalog（內部，不對外）
