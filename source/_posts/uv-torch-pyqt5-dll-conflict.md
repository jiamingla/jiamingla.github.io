---
urlname: uv-torch-pyqt5-dll-conflict
title: 【踩坑紀錄】uv + PyTorch + PyQt5 在 Windows 的 DLL 衝突：完整根因與解決方案
date: 2026-06-10 00:40:00
tags: [Python, uv, PyTorch, PyQt5, DLL, 疑難排解, 自動化測試]
---

## 前言：一個讓人措手不及的 WinError 1114

想像一個場景：你高高興興地把專案遷移到最近很紅、速度極快的 Python 套件管理工具 **uv**，本地端安裝一切順利。結果一執行專案，畫面沒出來，終端機直接噴出這一串冷酷的報錯：

```
OSError: [WinError 1114] 動態連結程式庫 (DLL) 初始化例行程序失敗。
Error loading "...torch\lib\c10.dll" or one of its dependencies.
```

更讓人納悶的是，旁邊用 Mac 的同事一臉無辜地說：「我跑起來完全沒問題啊？是不是你 Windows 系統壞了？」

這不是你的系統壞了，也不是你運氣不好。這是一個融合了 **套件版本命名潛規則**、**Windows 作業系統 DLL 載入順序**，以及 **uv 運行容器差異** 的綜合性大坑。這篇文章用白話文幫你拆解，這場「Windows 限定」的 DLL 衝突到底是怎麼發生的。

---

## 謎團一：為什麼 uv 裝 torchvision 會失敗？

當你剛把專案轉到 `uv` 時，通常在設定 `pyproject.toml` 階段就會遇到第一個下馬威。`uv` 在下載 `torchvision` 時會卡住並報錯：

```
error: Distribution `torchvision==0.24.0+e437e35 @ ...whl/cpu` can't be installed
hint: ... but `torchvision` (v0.24.0+e437e35) only has wheels for: `win_arm64`
```

### 根因：套件庫的版本號排序「比大小」Bug
PyTorch 官方的 CPU 版本套件庫裡，同一個版本（例如 `0.24.0`）同時放了兩種檔案：
1. `+cpu`（給一般 Intel/AMD 電腦用的）
2. `+e437e35`（專門給 ARM 晶片 Windows 電腦用的）

依照套件版本的英文字母排序規則，`e437e35` 排在 `cpu` 的後面，也就是被系統認為是「最新版本」。所以，求知慾很強且動作極快的 `uv` 在解析依賴時，會自動去抓它認為最新、但實際上是給 ARM 電腦用的 `+e437e35`，結果在你的一般 Windows 電腦上當然裝不起來。

### 怎麼解決？
在 `pyproject.toml` 裡，我們不能只寫 `torchvision` 讓它自己猜，必須把後綴的 `+cpu` 寫死，強迫 `uv` 抓正確的版本：

```toml
dependencies = [
    "torch==2.9.0+cpu",
    "torchvision==0.24.0+cpu",
    "torchaudio==2.9.0+cpu",
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true
```

---

## 謎團二：torchaudio 與 torch 的 ABI 不匹配

裝好套件後，一執行又噴出另一個錯誤：

```
OSError: Could not load this library: ...torchaudio\lib\_torchaudio.pyd
```

### 根因：核心零件的「嚴格對齊」
這很像買腳踏車，你只指定了車架（`torch`）要 2.9.0 版，卻讓鏈條（`torchaudio`）抓了最新版。因為這些深度學習套件底層都是 C++ 寫的，鏈條和齒輪的規格（C++ ABI）必須完全嚴格對齊。只要版本稍微對不上，動態檔案就卡不進去，直接當場罷工。

### 怎麼解決？
很簡單，在 `pyproject.toml` 裡，把 `torch`、`torchvision`、`torchaudio` 三個套件的版本後綴對齊成同一個系列（例如全部對齊 2.9.0 / 0.24.0 系列）。

---

## 謎團三：PyQt5 與 PyTorch 的 DLL 衝突

這是整個故事中最精采的部分。為什麼你的專案一 import PyQt5，接著載入 PyTorch（比如用 easyocr 做圖片辨識）時，`c10.dll` 就會初始化失敗？

### 用「餐廳的餐刀」來比喻這個衝突

想像你去一家餐廳（Python 進程）吃飯，你想用一把好切的專業牛排刀（現代 VC++ Runtime）來切牛排（載入 PyTorch 的 `c10.dll`）。

1. 你的程式一啟動，因為要連接 Google Sheets 或是畫面上某些元件，先載入了 **PyQt5**。
2. PyQt5 很高調，一進餐廳就把自己隨身攜帶的一把**舊款折疊塑膠刀**（PyQt5 5.15 內建的老舊 runtime DLL）直接拍在餐桌上（將自己的目錄加進 Windows 的系統 DLL 搜尋路徑）。
3. 隨後，程式準備載入 PyTorch（easyocr）。PyTorch 進場後想找牛排刀，但因為 PyQt5 已經把那把舊塑膠刀放在桌上最顯眼的位置了（Windows 搜尋 DLL 的高優先級路徑），PyTorch 沒多想，拿起來就切。
4. 結果塑膠刀當場折斷，牛排切不下去——這就是 `c10.dll` 載入失敗（WinError 1114）。

### 怎麼解決？
*   **方法一：惰性載入（Lazy Import）**
    如果你的自動化測試流程中，只有特定步驟才需要用 OCR 影像辨識，就把 `import easyocr` 或 `import torch` 移到函式內部。這樣平常不需要影像辨識時，程式就永遠不會去拿那把牛排刀，自然相安無事。
*   **方法二：搶先佔位（Workaround）**
    在程式最頂端、PyQt5 還沒有進餐廳之前，**搶先 `import torch`**。這等於是在 PyQt5 把塑膠刀拍在桌上之前，我們先把專業牛排刀拿在手上鎖定。等 PyQt5 進場後，我們已經拿好正確的工具了，就不會被它的舊 DLL 干擾。

---

## 核心解析：為什麼這個 Bug 只有在 `uv` 環境下會發生？

這時你可能會問：「不對啊，我之前沒有用 `uv`，是用微軟商店（Windows Store）裝的 Python，為什麼就不會遇到這把『塑膠刀』的干擾？」

這涉及到 **`uv` 運作環境** 與 **Windows OS 安全防護** 的底層差異：

*   **Windows Store 版 Python**：運行在微軟的 **AppContainer（應用程式沙盒）** 裡面。在這個沙盒裡，每個套件都被隔離在自己的包廂，PyQt5 的塑膠刀根本拿不出包廂，污染不到 PyTorch。
*   **`uv` 的 Python**：`uv` 為了追求極致速度與乾淨的獨立虛擬環境，拉下來的是「綠色免安裝（Standalone）」的 Python。它在 Windows 上就是個毫無防護的普通 Win32 進程，沒有沙盒包廂。因此，PyQt5 的 DLL 一旦註冊，就會毫無阻礙地直接污染整個大廳。

---

## Mac 同事為什麼在一旁笑而不語？

回到文章開頭那個無辜的 Mac 同事。為什麼他們用 `uv` 卻完全不會踩到這個大坑？

答案很簡單：**這是一個作業系統底層動態庫機制的 Windows 限定 Bug**。

1. **Mac 根本沒有 DLL**：macOS 使用的是 `.dylib`，其動態連結機制與鏈結器規則和 Windows 截然不同。
2. **沒有微軟 runtime 的包袱**：Windows 上的衝突起因於 PyQt5 包裹了舊版微軟 runtime DLL。而 Mac 上的 PyQt5 與 PyTorch 都是鏈結 macOS 原生的 `libc++`，大家用的是同一套系統底層鋼骨，沒有新舊規格不合的問題。
3. **結論**：所以 Mac 同事不論用什麼工具管理 Python，都天然免疫這個問題。

---

## 未來改進：徹底替換 OCR 核心（去 PyTorch 化）

如果想一勞永逸地解決這個 Windows 上的 DLL 惡夢，最治本的方法是「去 PyTorch 化」。

在自動化測試專案中，我們往往只是需要辨識截圖上的「日期」或「數字」等簡單文字，並不需要用到 PyTorch 這樣動輒幾百 MB、依賴重度的龐大深度學習框架。我們可以考慮：

1.  **Pytesseract (Tesseract OCR)**：輕量、初始化快，不依賴 C++ ABI 與 PyTorch，能徹底避開 DLL 衝突。
2.  **OpenCV 模板匹配 (Template Matching)**：如果辨識的字體（例如網頁時間、固定按鈕數字）大小與字型固定，直接用 OpenCV 做影像特徵比對，速度極快（<10ms）且精準度 100%，完全不需要載入機器學習模型。
3.  **改進測試策略 (API 驗證)**：最穩健的自動化測試是直接向後端 API 驗證資料是否正確，而非透過 UI 截圖用 OCR 去猜。

## 結語

`uv` 帶來了極速的套件建置體驗，但當我們把專案部署到不同的作業系統與環境時，底層的機制差異就會悄悄浮現。

下一次在 Windows 上遇到神祕的加載錯誤時，不妨想想那把「被搶佔的餐廳餐刀」，或許解答就藏在那些隱形的載入路徑之中。
