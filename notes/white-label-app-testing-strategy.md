# White-Label App 自動化測試策略與漸進式設計

## 一、 什麼是 White-Label App（白牌 / 貼牌 App）？

**White-Label App（白牌 App）** 是一種常見的軟體開發與商業模式。其核心概念是：
> **「一套核心程式碼（Core Codebase），多個品牌包裝（Multi-branding）。」**

開發團隊維護一個主要的系統產品，並透過配置、編譯參數或資源替換，為不同的企業客戶、子品牌或個別合作對象打包出多個獨立發佈的 App。這些 App 分佈在 App Store 與 Google Play 上，擁有不同的 App 名稱、Icon、軟體包名（Bundle ID），但其底層的業務流程有 90% 以上是共用的。

### 業界常見案例
1. **SaaS 與平台系統商**：例如點餐外送平台（幫 50 家不同的連鎖餐飲店各自出獨立的 App）、智慧家居平台（幫不同的家電品牌客製化控制 App）。
2. **金融與保險業**：同一個行動銀行架構，包裝成 20 家不同信用合作社或地方分行的 App。
3. **品牌/作者群體平台**：同一個內容訂閱、論壇或工具系統，為 20+ 位不同的意見領袖（KOL）或專家客製化專屬的個人品牌 App。

---

## 二、 White-Label App 測試的四大痛點

當測試腳本從「服務 1 個 App」變成「用同一套腳本跑 20 個 App」時，會面臨以下核心挑戰：

1. **案例爆炸（Case Explosion）**：
   如果為每個 App 複製一份測試案例，當加一個新功能時需要修改 20 份檔案，維護成本將呈線性膨脹，專案很快會進入無法維護的死局。
2. **元素定位脆弱（Locator Fragility）**：
   即便功能一樣，因為各 App 的 UI 主題色、元件庫版本、客製化外觀不同，編譯出來的 XML/HTML 樹狀結構可能不同。有的 App 帶 `resource-id`，有的沒帶；有的被多包了一層佈局容器，導致 XPath 直接失效。
3. **測試環境與測試資料的隔離性**：
   每個 App 可能連向不同的網域、使用不同的第三方登入通道，且需要不同的測試測試帳號。
4. **功能開關（Feature Flags）的分歧**：
   A App 有開「討論區」功能，B App 沒開。測試腳本在跑 B App 時必須能聰明地跳過該段測試，而不是直接報錯。

---

## 三、 漸進式定位抽象策略（三階段心法）

為了解決定位點與 UI 結構的分歧，不建議一開始就引入複雜的設計模式（例如為 20 個 App 抽 20 個類別），而應採用**漸進式抽象**：

### 📌 Phase 1：Fallback Chain + Config Override（小幅差異）
在 Page Object 的方法內，直接嘗試多種常見的 XPath 策略（Fallback），或者透過設定檔進行少數特例的覆蓋。

```python
def is_at_search_page(self) -> bool:
    # 策略 A：標準容器定位
    if self.driver.find_elements(By.XPATH, "//div[@id='standard-search-title']"):
        return True
    # 策略 B：裸文字定位（適用於某些被簡化包裝的 App）
    if self.driver.find_elements(By.XPATH, "//h1[contains(text(), '搜尋')]"):
        return True
    # 策略 C：外部 Config 注入的客製定位點
    custom_xpath = self.config.get("search_title_xpath")
    if custom_xpath and self.driver.find_elements(By.XPATH, custom_xpath):
        return True
    return False
```

### 📌 Phase 2：Locator Strategy Pattern（中度結構差異）
當 Fallback Chain 超過 4 個，或者多個頁面都需要 Config 客製化時，將「**定位策略**」抽離成獨立的 Strategy 類別，但 **Page Object 的業務邏輯（如 login, search）保持不變**。

```python
# locator_strategies.py
from typing import Protocol

class SearchLocator(Protocol):
    def get_search_input(self, driver) -> WebElement: ...

class StandardSearchLocator:
    def get_search_input(self, driver):
        return driver.find_element(By.ID, "search-input")

class WrappedSearchLocator:
    def get_search_input(self, driver):
        return driver.find_element(By.XPATH, "//div[@class='nav-wrapper']//input")
```
在 Page Object 初始化時，根據當前運行的 App 類型注入對應的 `SearchLocator`。**這能讓 Page Object 依然維持 1 個，而不會膨脹成 20 個。**

### 📌 Phase 3：Page Class 繼承與重寫（業務流程分歧）
只有當某個 App 的「業務流程/工作流」（而不僅僅是 UI 定位點）與其他 App 截然不同時，才為該 App 建立專屬的 Sub-class。

```python
class SpecialAppLoginPage(LoginPage):
    def login(self, username, password):
        # 該 App 登入時需額外處理一次性的驗證碼（OTP）流程
        ...
```

---

## 四、 未來寫作去識別化（De-identification）指南

如果您未來打算將這個珍貴的架構實戰經驗分享到部落格，為了徹底防範任何企業機密洩漏，請遵守以下去識別化規則：

| 原本專案的敏感資訊（指紋） | 建議替換的去識別化方案 |
| :--- | :--- |
| **公司與產品名稱** (如 CMoney、作者 App 系列) | 替換成常見的商業場景，如**「白牌電商平台（White-label E-commerce Platform）」**、**「連鎖品牌餐飲系統」**。 |
| **特定的 App 名字** (如 肌肉書單、軟木花等) | 替換為 **「Red Shop App」**、**「Blue Shop App」**。 |
| **真實專案的元件 ID** (如 `NavBarTitleComponent-Text`) | 替換成通用 HTML/XML 定位，如 `id="nav-title"`、`class="custom-header"`。 |
| **真實專案架構名稱與目錄** | 程式碼範例簡化為純 Python + Selenium/Appium 的最小可行性 Demo。 |

### 💡 虛擬範例包裝構想：
在文章中，您可以假設自己正在為一家幫連鎖超市開發 App 的軟體商服務：
> *「我們需要為『紅太陽超市』與『藍海洋超市』打包各自的 App。紅太陽超市在標題元件自帶了完整的 `id='store-title'`，但藍海洋超市因為是由第三方外包設計，UI 樹狀圖中只有一個裸的 `TextView`。如果我們寫死定位，測試就會在藍海洋 App 崩潰。以下是我們如何用三階段抽象來設計這個共用測試框架...」*

這樣不僅保留了最精華的**架構思考價值**，也讓內容完全合規且普適，非常適合軟體測試社群閱讀。
