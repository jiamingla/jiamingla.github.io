# uv + torch + PyQt5 踩坑紀錄

**建立日期**：2026-05-21
**性質**：工程備忘（cmqa-mcp 專案內部，**不直接發為 blog 文章**——含公司專案路徑與檔名）
**來源**：使用者 5/21 上傳，含 mojibake 已重建為正確中文（請對照原版確認）
**狀態**：cloud entry DLL 衝突暫不修；K096-K157（62 支）inline pattern 暫不收斂

---

## TL;DR

| 問題 | 狀態 | commit 範圍 |
|------|------|-------------|
| uv 裝不上 torchvision（PEP 440 local-version bug） | ✓ 修了 | 是 |
| torchaudio 跟 torch ABI 不匹配 | ✓ 修了 | 是 |
| K 系列共用 `get_chart_date_via_ocr` 每次重載 Reader（浪費 ~2 分鐘/輪） | ✓ 修了 | 是 |
| C 系列被 PyQt5/torch DLL 衝突搞死 | ✓ 修了 | 是 |
| K 系列 cloud (`Author_main_android_cloud.py`) 也踩 PyQt5/torch DLL 衝突 | ⏸️ **暫不修** | 否 |
| K 系列 standalone (`python K034.py`) 走 OCR 時可能撞同樣 DLL 衝突 | ⏸️ **暫不修** | 否 |

---

## Q1：為什麼 uv 裝 torchvision 失敗

**錯誤**：
```
error: Distribution `torchvision==0.24.0+e437e35 @ ...whl/cpu` can't be installed
hint: ... but `torchvision` (v0.24.0+e437e35) only has wheels for: `win_arm64`
```

**原因**：PyTorch 的 cpu index 同一版本 `0.24.0` 同時 host 了多個 local version：
- `+cpu` → win_amd64 ✓
- `+0429d73` / `+7a9db90` / `+b919bd0` / `+e437e35` → 只有 win_arm64

按 PEP 440 字串排序，`e437e35` > `cpu` → uv resolver 挑了它 → x86_64 機器無 wheel。

**修法**：`pyproject.toml` 三個都明確 pin：
```toml
"torch==2.9.0+cpu",
"torchvision==0.24.0+cpu",
"torchaudio==2.9.0+cpu",
```

---

## Q2：torchaudio 2.11.0 跟 torch 2.9.0 ABI 不匹配

**錯誤**：
```
OSError: Could not load this library: ...torchaudio\lib\_torchaudio.pyd
```

**原因**：原本只 pin `torch==2.9.0` 沒 pin torchaudio，uv 抓最新 2.11.0，但 torchaudio.X 必須對到 torch.X 的 C++ ABI。

**修法**：見 Q1，三個都對到 2.9.0/0.24.0。

---

## Q3：C 系列莫名踩 PyQt5/torch DLL 衝突

**錯誤**：
```
OSError: [WinError 1114] 動態連結程式庫 (DLL) 初始化例行程序失敗。
Error loading "...torch\lib\c10.dll" or one of its dependencies.
```

**重現條件**：
1. 任何路徑 import `Author.Android.lib.test_action`
2. test_action → `public.lib.google_sheets_lib.google_api_utility` → eagerly `from PyQt5...`
3. PyQt5 載入 → 把 `site-packages/PyQt5/Qt5/bin/` 加進 DLL 搜尋路徑
4. Qt5/bin 裡有 PyQt5 5.15 bundle 的老舊 `msvcp140.dll`、`vcruntime140.dll`
5. 之後任何 `import torch` → torch 載 c10.dll → c10.dll 找依賴 → 找到 PyQt5 的老 VC runtime → init 失敗

**為什麼 C 系列也撞**：`StrategyPage` 繼承 `BasePage`，`BasePage.__init__` 原本 eagerly `self.ocr_reader = easyocr.Reader(...)` → 觸發 easyocr → torch → 撞牆。

**修法**：`base_page.py` 把 `ocr_reader` 改成 lazy `@property`，C 系列從不 access OCR → 永遠不會載 torch → 永遠不會撞 DLL。

順帶清理：`stratagy_page.py` 死碼 `extract_text_from_image` 砍掉，連帶移除無用 import。

---

## Q4：K 系列每次重新載 Reader 浪費時間

**觀察**：
- ~66 支 K 腳本透過 `kline_page.get_chart_date_via_ocr()` 走共用路徑
- 62 支（K096-K157）自己 inline `reader = easyocr.Reader(['en'], verbose=False)`
- 每次 `easyocr.Reader()` 建構約 2 秒（重新載 ML 模型）

**修法（K030-K095 走的共用函式）**：`kline_page.py`、`kline_page_with_out_id.py` 加 module-level singleton `_get_ocr_reader()`。

**未動（K096-K157 inline pattern）**：62 支沒改，這次 refactor 暫不動，diff 太雜不 review 划不來。

**效益**：K030-K095 整輪省 ~2 分鐘 + ~6GB 記憶體。

---

## Q5：K 系列 cloud entry 仍踩 DLL 衝突（**未修**）

**錯誤路徑**：
1. `Author_main_android_cloud.py` line 3 `from public.lib.google_sheets_lib import google_api_utility` → PyQt5 在這裡載入
2. 後續 `importlib.import_module('Author.Android.script.K034')` → K34.main() → `kline_page.get_chart_date_via_ocr()` → 第一次 lazy `import easyocr` → torch → DLL 衝突

**為什麼 standalone 跑起來 OK**：K34 也載 PyQt5，但因為 K34 還沒走到 OCR 那步就可能 early return（找不到 driver 之類），所以不一定 reproduce。實測 OCR 真的會撞。

**修法選項（討論後選 D：先不修）**：

| 方案 | 動作 | 評估 |
|------|------|------|
| A | 把 kline_page 的 lazy easyocr 改回 eager | 不夠：cloud 是 google_api_utility 先載 PyQt5 |
| B | `Author_main_android_cloud.py` line 1 加 `import torch` | 可行但很醜，ruff exclude 蓋掉 |
| C | `kline_page.py` 頂部加 `import torch`（已套用） | 只夠 standalone 場景，cloud 仍無效 |
| D | **先不修** | uv + torch 工作量不划算，等替換 easyocr 自然解決 |

---

## 為什麼只有 uv 環境會撞？

**核心：Python 發行版差異 → DLL loader 行為差異**

| 維度 | uv-managed Python | Windows Store Python |
|------|--------------------|---------------------|
| 來源 | `python-build-standalone`（portable build） | Microsoft 官方 |
| 安裝位置 | `~/AppData/Roaming/uv/python/cpython-...-windows-x86_64-none/` | `C:\Program Files\WindowsApps\...` |
| 執行容器 | 一般 Win32 process | **AppContainer**（App Sandbox） |
| DLL 搜尋規則 | 標準 Win32 順序（含 `os.add_dll_directory` 路徑） | AppContainer 額外規則 + SxS 偏好系統最新 |
| PyQt5 污染 DLL 路徑 | 直接影響後續 `import torch` | 被 AppContainer 隔離，不影響其他 wheel |

**簡單講**：uv 用的是「裸 Python」，沒有 MSIX 容器的 DLL 隔離；其他人用 Windows Store Python 跑在 AppContainer 裡，PyQt5 bundle 的老 VC runtime 干擾不了 torch。

### 個人替代方案

裝 [VC++ 2015-2022 Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe) 提供更新系統 VC runtime。但因為 Win32 DLL 搜尋順序裡 `os.add_dll_directory` 加進來的路徑優先**高於** System32，PyQt5 帶的老 DLL 仍會勝出。**對 uv 不一定有效**，但成本低可以試。

---

## 目前 commit 的東西

| 檔案 | 改動 |
|------|------|
| `pyproject.toml` | 三個 torch 套件 pin `+cpu`、分群整理 |
| `uv.lock` | 跟著 resolve |
| `base_page.py` | `ocr_reader` lazy property |
| `stratagy_page.py` | 砍死碼 + 無用 imports |
| `kline_page.py` | singleton `_get_ocr_reader()` + 頂部 `import torch`（standalone K 用 workaround） |
| `kline_page_with_out_id.py` | singleton `_get_ocr_reader()` |
| `K034.py` | docstring 修正 |

---

## 未修（已知 + 接受）

1. **`Author_main_android_cloud.py` 跟 K 系列撞 c10.dll** — workaround：cloud 場景用 Windows Store Python
2. **standalone `python K034.py` 走到 OCR 那步可能撞** — 同上
3. **K096-K157（62 支）inline `easyocr.Reader()` 沒收斂到 singleton** — 每輪浪費 ~2 分鐘

---

## 未來改進（治本）

### 中期：評估 OCR 替代方案

| 方案 | 每次處理 | init 成本 | 準確度（純數字） | 備註 |
|------|---------|----------|----------------|------|
| easyocr（現況） | ~200ms | ~2s | 高 | torch 整套累贅 |
| **pytesseract** | ~100-300ms | ~0 | 中-高 | 須系統裝 Tesseract |
| **模板匹配（OpenCV）** | ~10ms | 0 | 極高（字型固定） | 預存 0-9 + `/` + `:` 模板 |
| **後端 API 驗證** | ~50ms | 0 | 100% | 改測試策略，不看 UI |
| AI Vision（Claude/GPT-4V） | ~1-3s + $ | 0 | 高 | 慢 + 貴 + 不 deterministic |

走向：**pytesseract**（最小改動）或 **後端 API**（最徹底）。

### 長期：徹底替換 easyocr / torch

完成 OCR 替換後：
- 砍 `pyproject.toml` 的 torch / torchvision / torchaudio
- 砍 `[[tool.uv.index]] pytorch-cpu`
- 砍 `kline_page.py` 頂部 `import torch` workaround
- DLL 衝突從此根除

---

## 給未來自己的提醒

1. 如果哪天 `kline_page.py` 頂部那段 `import torch` 註解被誤觸，那是 workaround，等替換 easyocr 一起砍
2. 如果 uv lock 又抓了奇怪的 torchvision local version，去 https://download.pytorch.org/whl/cpu/torchvision/ 看多了什麼新變體，pin 死 `+cpu`
3. 如果要徹底替換 OCR，盤點所有用 `easyocr` 的腳本，估算 ~95 支 K 系列 + 部分 lib

---

# 🎯 Blog 文章潛力評估（**這份內容如何抽象化成可發文章**）

## 長尾關鍵字潛力：⭐⭐⭐⭐

這份內容剛好命中昨天 SEO 策略段討論的最佳長尾類型——**極具體的技術踩坑**，搜尋量小、競爭極小、容易排第一頁：

- "uv torchvision PEP 440 local version bug"
- "torch torchaudio ABI mismatch Windows"
- "PyQt5 torch c10.dll WinError 1114"
- "easyocr DLL conflict Windows uv Python"
- "AppContainer vs uv Python DLL loading difference"

特別有價值的是 **「為什麼只有 uv 環境會撞」** 那段——**這個分析非常稀缺**，搜尋這個 keyword 的人幾乎沒有資源，誰寫出來誰收。

## 必須洗掉的指紋（**發前要動的東西**）

| 內部指紋 | 替換成 |
|---|---|
| `K 系列`、`K030-K157`、`K034.py` | 「自動化測試專案」「某系列腳本」 |
| `Author/Android/lib/...` | 「自動化框架的 lib」「測試共用模組」 |
| `StrategyPage`、`BasePage` 繼承關係 | 「頁面物件繼承鏈」「Page Object 父類別」 |
| `Author_main_android_cloud.py` | 「雲端入口腳本」 |
| `google_sheets_lib`、`google_api_utility` | 「Google Sheets 整合模組」 |
| `kline_page`、`kline_page_with_out_id` | 「K 線圖頁面物件」 |
| `get_chart_date_via_ocr` | 「OCR 日期擷取函式」 |
| ~66 支、62 支、95 支這類具體數字 | 「數十支」「大多數」 |
| 「給未來自己的提醒」這節 | **整節刪除**（公司內部備忘） |

## 建議拆分

這份內容**太密、太長**，做成一篇會勸退讀者。建議拆 2-3 篇：

### 主文（必發）：〈uv + torch + PyQt5 在 Windows 的 DLL 衝突：完整根因解析〉
- Q1 + Q2（uv resolver 行為 + PEP 440 bug）
- Q3（PyQt5/torch DLL 衝突重現條件）
- **「為什麼只有 uv 環境會撞」**（這段是文章核心）
- 修法（lazy import + pin versions）
- 預估 2500-3500 字

### 副文 1（選發）：〈Python 自動化測試的 OCR 取捨：easyocr vs pytesseract vs 模板匹配 vs 後端 API〉
- 把 OCR 替代方案表單獨拉出來成獨立文
- 純技術評估、零專案指紋
- 1500-2000 字
- 長尾力同等 ⭐⭐⭐⭐

### 副文 2（選發）：〈uv 對個人開發者很好、對團隊不一定——一個 6 人團隊的相容性 cost 觀察〉
- 把「未來改進 - 短期」那節（uv 對團隊 vs 個人）拉出來
- 比較大人學文章，配合 SEO 長尾「uv vs venv team adoption」
- 線六（職涯）+ 線八（SEO 長尾）

## 建議下一步

如果你想動筆——**先動主文**（DLL 衝突全紀錄）。理由：
1. 長尾力最強（「PyQt5 torch c10.dll」這組關鍵字真的沒人寫過深度分析）
2. 容易洗指紋（核心是技術原理，公司路徑只是輔證）
3. 跟你 [page-source-vs-find-element](../source/_drafts/page-source-vs-find-element.md)（已排 6/20）形成「Python 自動化測試 + Windows 底層技術」雙篇——線三辨識度大增

我可以幫你建 `_drafts/uv-torch-pyqt5-dll-conflict.md` 骨架——洗指紋過、結構保留——等你想動筆時填內容。要嗎？
