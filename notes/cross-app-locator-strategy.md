# 跨 APP 元素定位策略設計

**建立日期**：2026-05-28
**性質**：工程備忘（CMoney 作者 APP 系列的測試 framework 設計，**含公司專案路徑與 component 命名**——不直接發為 blog 文章）
**來源**：使用者 5/28 上傳的歸納，含 mojibake 已重建為正確中文（請對照原版確認）
**觸發脈絡**：同一個 `is_at_X` 方法跑不同作者 APP 時，因 XML 結構分歧導致 false-negative

---

## 問題場景

CMoney 作者 APP 系列（軟木花、肌肉書單、輸贏圈、阮姆河⋯⋯共 20+ 個），共用同一份測試 lib，但各 APP 的 Compose UI 細節有差異：

- 同一個 UI 元素：A APP 帶 `resource-id`、B APP 沒帶
- 同一個容器：A APP 用 `NavBarTitleComponent-Text`、B APP 用 `CustomNavBar-CenterComponent`
- 同一個按鈕：視覺一樣但 XML 結構（巢狀層級、tag name）不同

如果一個 page method 只 hardcode 一種寫法，遇到第二種 APP 就 fail。

## 已觀察到的兩種分歧（未至完整）

| 元素 / 判斷 | 寫法 A（標準）| 寫法 B（裸 TextView 包）|
|---|---|---|
| 搜尋頁標題 | `NavBarTitleComponent-Text` 自帶 text="搜尋" | `CustomNavBar-CenterComponent` 容器內 TextView text="搜尋" |
| 通知頁標題 | 同上 含 "通知" | 同上 含 "通知" |
| 大盤頁標題 | 同上 含 "大盤" | 同上 含 "大盤" |
| 貼文內容頁標題 | 同上 含 "貼文" / "內容" | 同上 含 "貼文" / "內容"（肌肉書單）|
| 鈴鐺 / 搜尋按鈕 | resource-id + xpath 位置可定位 | 視覺一致但 XML 位置不固定 → 各自定位邏輯 |

→ **「同樣兩種寫法」反覆出現**，到了該系統化抽象的程度。

---

## 設計取捨：抽 interface vs 不抽

### 直覺解法（per-APP class + 抽 interface）

```python
class NotificationPage(ABC):
    @abstractmethod
    def is_at_notification_page(self) -> bool: ...

class MuscleBookerNotificationPage(NotificationPage):
    def is_at_notification_page(self):
        # 肌肉書單的實作
        ...

class RuanMuHuaNotificationPage(NotificationPage):
    def is_at_notification_page(self):
        # 軟木花的實作
        ...

# ... × 20 個 APP
```

**為什麼這個方向選擇抽象（不建議一開始就做）**：

| 隱性成本 | 說明 |
|---|---|
| **class 爆炸** | NotificationPage × 20、StrategyPage × 20⋯⋯ 數百個 class |
| **DRY 違反** | 多數 APP 邏輯相同卻被迫複製 |
| **新增方法成本高** | 加一個 `mark_all_as_read` 要改 20 個檔 |
| **新人 onboarding 難** | 「我要找通知頁邏輯」要先決定「找哪個 APP 的」 |
| **同步落後** | APP 改版時要等到跑到才發現該 APP 的 impl 沒更新 |

**只在「業務流程完全不同」的 APP 才用 per-APP class** —— 例：某 APP 把通知做成 sub-app，整個導航流程不一樣。

---

## 推薦：漸進式三階段

### Phase 1（預設）：fallback chain + config override

單一 page object，方法內依序試多種定位策略：

```python
def is_at_article_content_page(self) -> bool:
    # a) 標準：NavBarTitleComponent-Text 自帶 text
    if getTarget.find_element_xpath(STANDARD_XPATH):
        return True
    # b) 裸 TextView 包：CustomNavBar-CenterComponent 容器內找
    if getTarget.find_element_xpath(WRAPPED_XPATH):
        return True
    # c) per-APP 客製：從 config.author 的 xpath override 撈
    custom = config.author.get('article_title_xpath')
    if custom and getTarget.find_element_xpath(custom):
        return True
    return False
```

**何時夠用**：
- 多數 APP 落在 2-3 個共通 pattern
- 個別 APP 的特例可以靠 `config.json` 的 per-APP override 接住
- 已有專案內既有先例（`config.author['search']`、`config.author['bell']`）

**何時該升 Phase 2**：
- 單一方法 fallback chain 超過 4 個 xpath（讀起來像大義麵）
- 同一個 APP 多個方法都要 config override（暗示該 APP 整體行為差異大）
- 加新 APP 要改超過 3 個檔（單純加 config 撐不了）

---

### Phase 2（中期）：抽 LocatorStrategy（不抽整個 Page）

當 Phase 1 fallback chain 變太長時，把「**定位策略**」抽出來，但 page logic 不動：

```python
# locator_strategies.py
from typing import Protocol

class TitleLocator(Protocol):
    """Per-APP 的標題定位策略"""
    def find_article_title(self) -> WebElement | None: ...

class StandardTitleLocator:
    """resource-id="NavBarTitleComponent-Text" 自帶 text 的標準寫法"""
    def find_article_title(self) -> WebElement | None:
        return getTarget.find_element_xpath(
            f'//*[@resource-id="{id_.NavBarTitleComponent_Text}" '
            f'and contains(@text, "貼文")]'
        )

class ContainerWrappedTitleLocator:
    """容器 resource-id + 內部裸 TextView 的寫法（肌肉書單等）"""
    def find_article_title(self) -> WebElement | None:
        return getTarget.find_element_xpath(
            f'//*[@resource-id="{id_.CustomNavBar_CenterComponent}"]'
            f'//android.widget.TextView[contains(@text, "貼文")]'
        )

# strategy registry
TITLE_LOCATOR_BY_APP = {
    'musclebooker': ContainerWrappedTitleLocator(),
    'ruanmuhua': StandardTitleLocator(),
    # 未列出 → 用 default = 串連兩個 locator 形成 fallback chain
}
```

`NotificationPage` 只對映 strategy：

```python
class NotificationPage(BasePage):
    def __init__(self):
        super().__init__()
        self.title_locator = TITLE_LOCATOR_BY_APP.get(
            config.author_name, DefaultTitleLocator()
        )

    def is_at_article_content_page(self) -> bool:
        return self.title_locator.find_article_title() is not None
```

**關鍵收穫：page object 仍只有 1 個（NotificationPage），不變 20 個。**

---

### Phase 3（特例）：完整 per-APP page class

**只有當某 APP 的「業務流程」（不只 UI 結構）跟其他 APP 完全不同時** 才為它建專屬 page class：

```python
class WeirdAppNotificationPage(NotificationPage):
    """這個 APP 的通知頁是個完全獨立的 sub-app，整個導航流程不同。"""
    def click_first_article(self):
        # 完全不同邏輯
        ...
```

但 **不要對每個 APP 都做這個**。Phase 3 應該是 1-2 個案例，不是常態。

---

## 給「20 APP」場景的當前決策表

| 觀察到的差異程度 | 建議做法 |
|---|---|
| 多數 APP 視覺一致，XML 微異（resource-id 有無、容器層級差異）| Phase 1：fallback chain + config override |
| 3-4 個方法的 fallback chain 都長到難讀 | 抽 helper function（**抽通用 pattern，不抽 APP**）|
| 有幾個 APP 連 fallback 都接不住，要用不同 UI lib | Phase 2：per-APP `LocatorStrategy` |
| 某 APP 業務流程跟其他完全不同 | Phase 3：per-APP `Page` class（少數案例）|

---

## 抽 helper function 是「中間的智慧」

當你發現第 4 次寫同樣 pattern 的 `is_at_X`，重複到痛、該抽、還沒死。

**不要直接跳到 Phase 2**（per-APP strategy）。先抽 helper function：

```python
# base_page.py
def _is_at_titled_page(self, keywords: list[str], timeout: int = 5) -> bool:
    """
    通用：標題含某字串任一 keyword 時回傳（自動容兩種容器寫法）。

    兩種寫法：
    a) NavBarTitleComponent-Text 自帶 text
    b) CustomNavBar-CenterComponent 容器內裸 TextView
    """
    keyword_or = ' or '.join(f'contains(@text, "{k}")' for k in keywords)
    # a)
    a_xpath = f'//*[@resource-id="{id_.NavBarTitleComponent_Text}" and ({keyword_or})]'
    if getTarget.find_element_until_visible(a_xpath, timeout=timeout):
        return True
    # b)
    b_xpath = (
        f'//*[@resource-id="{id_.CustomNavBar_CenterComponent}"]'
        f'//android.widget.TextView[{keyword_or}]'
    )
    return getTarget.find_element_xpath(b_xpath) is not None
```

子類方法變一行：

```python
def is_at_notification_page(self):
    return self._is_at_titled_page(['通知'])

def is_at_search_page(self):
    return self._is_at_titled_page(['搜尋'])

def is_at_article_content_page(self):
    return self._is_at_titled_page(['貼文', '內容'])
```

**好處**：
- 維護成本最低
- cover 已知的多數場景
- 新加類似 `is_at_X` case 變成 1 行
- 不引入 per-APP 概念，不破壞既有架構

---

## 經驗法則總結

1. **「重複 3 次以上才抽象」**—— 別過度抽象
2. **「抽通用 pattern，不抽 APP」**—— helper function 比 per-APP class 維護成本低 10 倍
3. **「config.json override 是逃生口」**—— 個別 APP 的特例不該污染主邏輯
4. **「Phase 3 是例外不是常態」**—— per-APP class 只給「業務流程完全不同」的 APP

當下次新增 `is_at_X` 第 5 次同樣 pattern 時，就是抽 `_is_at_titled_page` helper 的時機。

---

## 妥協代價：POM 抽象讓 case 變簡潔

老實講，fallback chain pattern 會讓 page object 的讀起來很冗 —— 每個方法 5-15 行才搞定一件事（「判斷在不在某頁」），相比寫死單一 xpath 的 1-2 行版本，閱讀成本明顯較高。

**但這是有意識的妥協**，理由：

| 替代方案 | 為什麼更差 |
|---|---|
| 寫死單一 xpath | 遇到第 N 個 APP 不一致就要全部 case 進去改 |
| Per-APP class × 20 | 加新方法要改 20 處，新人不知道去哪改 |
| Switch by appname inline | 邏輯散落變亂，遺漏一處變靜默 fail |

**選 fallback chain 是承認「APP 結構分歧是 ground truth，不會消失」**—— 與其讓 case 端寫一堆條件判斷，不如把分歧封裝在 page method 內，case 端保持乾淨。

POM 讓 case 簡潔，這個交易在 80+ case × 20 APP 的乘法效應下值得。但記住這個代價存在 —— 當哪個 method fallback chain 超過 4-5 段時，那是訊號該往 Phase 2（抽 LocatorStrategy）走，而不是繼續加 chain。

---

## 個別作者已知差異 catalog

具體「哪個 APP 在哪個 page method 做了什麼不同」的清單記在這份檔案：

- **Markdown 版**（給工程查找 / git 追蹤）：[per_app_quirks.md](per_app_quirks.md)
- **簡報版**（給 PM / 跨團隊 status review）：[Google Slides](https://docs.google.com/presentation/d/1cNnV6hCgAEP9UNZ57S-RSpbzz5EqFdcUQc_wiGq_51s/)

當 fallback chain 無法 cover 新 APP 時，先去 `per_app_quirks.md` 查該 APP 是否已被觀察到差異，再決定 Phase 1 / 2 / 3 哪條路。

---

## 相關連結

- 目前 fallback chain 範例：`StrategyPage.is_at_notification_page`
- per-APP config override 範例：`config.json` 內各 APP 的 `search`、`bell` 欄位
- 跨置物櫃的 fallback 範例：`StrategyPage.get_stock_info_list_v2` 的 `Content_StockNameCandleStickTag` 分支

---

# 🎯 Blog 文章潛力評估

## 長尾力：⭐⭐⭐⭐

這個題目在中文 QA 圈**幾乎沒人寫過**，極具差異化價值：

- "跨 APP 測試框架 Page Object"
- "Appium fallback chain locator"
- "Compose UI 元素定位策略"
- "一份測試 lib 多 APP 共用"
- "Page Object 漸進式抽象"

特別有價值的是 **「漸進式三階段」這個思考框架**——多數 POM 教學只講「該抽 interface」或「不該抽」，**沒人說「該分三階段、何時升階」**。這個 mental model 稀缺。

## 必須洗掉的指紋

| 內部指紋 | 替換成 |
|---|---|
| CMoney 作者 APP 系列 | 「某個內容型 APP 集團」「某產品線」 |
| 軟木花 / 肌肉書單 / 輸贏圈 / 阮姆河 | 「APP A / B / C / D」 |
| musclebooker / ruanmuhua | 抽象代號 |
| NavBarTitleComponent-Text / CustomNavBar-CenterComponent | 「容器 A / 容器 B」 |
| Author/Android/lib/ | 「測試 lib」 |
| StrategyPage / get_stock_info_list_v2 / Content_StockNameCandleStickTag | 抽象命名 |
| per_app_quirks.md / Google Slides 連結 | **整段刪除** |
| 「20+ APP」「80+ case」具體數字 | 「20+ 個 APP」「上百個 case」 |

## 該歸的主題線

**主要落線三（技術實戰 / 自動化）**——這是本篇的天然定位。

**次要呼應線四（測試紀律 / 方法論）**——「重複 3 次才抽象」「抽通用 pattern 不抽 APP」是普世方法論。

## 跟既有草稿的關係

| 既有 | 跟本篇的差異 |
|---|---|
| [pom-refactor-from-runnable-to-maintainable](../source/_drafts/pom-refactor-from-runnable-to-maintainable.md) | 那篇處理「**能跑 → 可維護**」（single APP） |
| 本篇（cross-app-locator）| 處理「**single APP → multi APP**」（規模化） |

→ **可形成「POM 雙篇」或「POM 系列」**——pom-refactor 是入門、本篇是進階。如果未來兩篇都寫，可以互引、形成線三的子系列。

## 跟 [not-just-make-manual-script-automate](../source/_drafts/not-just-make-manual-script-automate.md) 的關係

那篇講「**自動化是另一物種**」（why），本篇講「**多 APP 自動化怎麼設計**」（how at scale）。同屬線三 + 線五，但角度完全不同——不衝突，可互引。

## 建議拆分

這份內容超長（~2000 字 + code blocks），做成一篇可能 4500-5500 字。建議：

### 主文：〈一份測試 lib 服務 20 個 APP——元素定位的漸進式抽象策略〉
- Phase 1 / 2 / 3 + helper function 中間智慧
- 決策表 + 經驗法則
- POM 抽象的妥協代價
- 預估 4000-5000 字

### 副文（選發）：〈為什麼我不一開始就抽 interface？——抽象的「三次法則」〉
- 把「重複 3 次以上才抽象」獨立成方法論文
- 不限於 Page Object，可應用到任何 codebase
- 1500-2000 字
- 線四（方法論）

## 標題候選

1. ⭐ **〈一份測試 lib 服務 20 個 APP——元素定位的漸進式抽象策略〉**——精準、SEO 友善
2. **〈為什麼我不一開始就抽 interface？跨 APP locator 設計的三階段〉**——挑戰性開頭
3. **〈Fallback chain vs Per-APP class——20 個 APP 共用測試框架的設計取捨〉**——比較型
4. **〈POM 規模化：當你的 Page Object 要服務 20 個 APP〉**——POM 系列定位

## 建議下一步

如果未來想動筆——**先寫主文**（漸進式三階段）。理由：
1. 長尾力最強（「跨 APP 測試框架設計」這組關鍵字稀缺）
2. 跟 pom-refactor 形成 POM 雙篇，**線三辨識度大增**
3. 容易洗指紋（核心是技術思考框架，公司命名只是輔證）

我可以幫你建 `_drafts/cross-app-locator-progressive-abstraction.md` 骨架——洗指紋過、結構保留——等你想動筆時填內容。

## 紅線

- ❌ 不要點名任何具體 APP / component / 同事
- ❌ 不要寫成「我們公司怎麼做」——主張該是「**一個普世可參考的設計策略**」，公司是案例不是主角
- ❌ 不要過度否定 per-APP class——它在 Phase 3 還是有位置
- ❌ 不要把 80+ case × 20 APP 寫死——可能洩漏規模
