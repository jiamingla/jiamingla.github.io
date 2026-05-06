---
urlname: pom-refactor-from-runnable-to-maintainable
title: POM 重構實戰：把「能跑」的自動化腳本，改寫成「能被別人接手」的形狀
date: 2026-05-06 22:00:00
tags: [軟體測試, 自動化測試, Page Object Pattern, POM, Selenium, Appium, Python, 測試架構, 程式碼重構, 品質工程]
---

## 前言：那份「再也沒有人敢動」的測試腳本

你接手了一份前人留下的自動化測試。它**會跑**。但你打開檔案的瞬間，呼吸停了半秒——

- 一個檔案 1500 行
- 同樣的 CSS selector 散在二十幾個地方
- `time.sleep(5)` 像撒鹽一樣到處都是
- 登入、瀏覽、結帳、登出全部塞在一個 function 裡
- assertion 混在 navigation 的步驟之間，讀的時候要倒著推

你站在三選一的岔路口：

1. **跟著爛** — 加新 case 就照原本的味道繼續寫，反正能跑
2. **全部重寫** — 把它整個丟掉，重來一份乾淨的
3. **有方法的重構** — 慢慢把它拉直，但中間每一刻都保持綠燈不破

第一種短期最舒服，但你的下下個 sprint 會付代價；第二種讓你想離職一個月；**這篇文章是寫給選第三種的你**。

POM（Page Object Model / Pattern）是這條重構路最常被推薦、但也最常被誤用的工具。我這篇想拆的不是 POM 的 wiki 定義（那種文章已經很多），而是——

> **POM 真正在解的問題是什麼？三層責任分離長什麼樣？什麼時候 POM 反而會傷你？**

如果你的目標是「**這份 code 一年後能被別人接手**」，POM 設計得好不好，幾乎就是分水嶺。

---

## 一、POM 不是「把 selector 抓出來」這麼簡單

很多人對 POM 的第一印象是：**「就是把 selector 集中放到一個檔案裡，避免 hardcode 散到處嘛」**。

這個理解只對了 20%。

如果 POM 只是「selector 集中管理」，那寫成一個 `selectors.py` 字典就夠了，不需要 class、不需要 method、不需要設計。實務上**很多 QA 寫的 POM 就停在這個層級**——把 selector 集中，但其他什麼都沒變。結果是：

- selector 集中了，但 wait 還是散在 test 裡
- 每個 test 還是直接呼叫 `driver.find_element(...).click()`
- 換頁邏輯混在斷言之間，讀起來還是天書

POM 真正的本質是這個——

> **把一個「頁面」當作一個物件。這個物件知道：自己有哪些元件（結構）、可以對它做哪些事（行為）。怎麼做到，是它自己的事，外面不該管。**

換句話說，POM 是一種**封裝**：把「**這一頁的 UI 細節**」跟「**用這一頁做事的人**」分開。test 不應該知道 username 欄位的 CSS selector 是什麼——test 只應該說「我要登入，帳號是 X，密碼是 Y」。

當你看清楚這個本質，你會發現 POM 真正要解的**從來不是 selector 重複**，是另一個更大的問題：

> **UI 會變，但測試意圖不變。POM 是一座在這兩者之間的橋。**

UI 改版的時候，selector 換、wait 條件變、結構重組——你不該因此重寫 test 的意圖。**你應該只動那座橋本身**，test 一個字都不用改。能不能做到這件事，就是 POM 寫得好不好的試金石。

---

## 二、三層責任分離：POM 的核心紀律

任何一段自動化測試，本質上都在做三件事：

1. **找東西**（Selector）— 這個按鈕在哪？這個輸入框在哪？
2. **等到對的時機**（Wait）— 元件出現了嗎？頁面 ready 了嗎？資料載入完了嗎？
3. **驗證結果**（Assertion）— 這個畫面長對嗎？這個值對嗎？

沒有設計的 code，這三件事**會混在每一個 step 裡**。每跑一個動作就 `find_element + sleep + assert` 一次，三件事像義大利麵一樣纏在一起。

POM 的核心紀律就是把這三層分開，讓每一層住在它該住的地方：

| 層 | 職責 | 該住在哪 |
|---|---|---|
| Selector | 描述「東西在哪」 | **PageObject 的 class attribute** |
| Wait | 描述「什麼時候 ready」 | **PageObject 的 method 內部** |
| Assertion | 描述「對 / 不對」 | **Test 裡，不該進 PageObject** |

特別點出第三條——**assertion 不該寫進 PageObject**。這是初學者最常踩的雷：覺得「assert 寫在 page object 裡比較整齊」，結果整個物件變成「半 navigation 半 verification」的混合體。一旦這樣，你的 PageObject 就再也不能被另一個 test 重複使用——因為它身上綁著上一個 test 的 assertion。

PageObject 是工具，**assertion 是測試意圖**。工具該被重複使用，意圖則屬於每一個 test 自己。把它們分開，才能讓你的測試組合像樂高一樣自由拼接。

---

## 三、Before / After：一段虛構但典型的爛 code

下面這個例子是虛構的——一個 demo 電商網站的「登入＋加購物車」流程。但裡面每一個壞習慣，我都從真實 code 裡看過。

### Before：能跑、但沒人想動

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_and_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://shop.example.com/login")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "input#username").send_keys("test@example.com")
    driver.find_element(By.CSS_SELECTOR, "input#password").send_keys("password123")
    driver.find_element(By.CSS_SELECTOR, "button.login-btn").click()
    time.sleep(5)
    assert "Welcome" in driver.find_element(By.CSS_SELECTOR, ".user-greeting").text
    driver.find_element(By.CSS_SELECTOR, ".product-card:nth-child(1) button.add-to-cart").click()
    time.sleep(2)
    assert driver.find_element(By.CSS_SELECTOR, ".cart-count").text == "1"
    driver.quit()
```

**這段 code 能跑。但它有以下問題：**

1. **Selector 全部 hardcode 在 test 裡** — UI 一改，這個 test 跟未來十個 test 全部要改
2. **Sleep 處處** — 不是 explicit wait，是 `time.sleep`。網路慢一點就 flaky；網路快的時候是浪費時間
3. **登入 / 瀏覽 / 加購物車的邏輯全部塞在一個 test 裡** — 下一個 test 想複用「登入」？只能 copy-paste
4. **Assertion 跟 navigation 混在一起** — 讀的時候要在腦中切換「這行是動作 / 這行是檢查」
5. **沒有 setup / teardown 結構** — driver 直接在 test 裡開關，第二個 test 又要寫一遍

### After：把責任拆開後的版本

```python
# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "/login"

    USERNAME_INPUT = (By.CSS_SELECTOR, "input#username")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input#password")
    LOGIN_BUTTON   = (By.CSS_SELECTOR, "button.login-btn")

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> "LoginPage":
        self.driver.get(self.base_url + self.URL)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        return self

    def login(self, username: str, password: str) -> "HomePage":
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return HomePage(self.driver, self.base_url).wait_until_loaded()
```

```python
# pages/home_page.py
class HomePage:
    USER_GREETING = (By.CSS_SELECTOR, ".user-greeting")
    FIRST_PRODUCT_ADD_BUTTON = (By.CSS_SELECTOR, ".product-card:nth-child(1) button.add-to-cart")
    CART_COUNT = (By.CSS_SELECTOR, ".cart-count")

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def wait_until_loaded(self) -> "HomePage":
        self.wait.until(EC.visibility_of_element_located(self.USER_GREETING))
        return self

    @property
    def greeting_text(self) -> str:
        return self.driver.find_element(*self.USER_GREETING).text

    @property
    def cart_count(self) -> int:
        return int(self.driver.find_element(*self.CART_COUNT).text)

    def add_first_product_to_cart(self) -> "HomePage":
        before = self.cart_count
        self.driver.find_element(*self.FIRST_PRODUCT_ADD_BUTTON).click()
        self.wait.until(lambda d: self.cart_count > before)
        return self
```

```python
# tests/test_shopping.py
def test_login_and_add_to_cart(driver, base_url):
    home = (
        LoginPage(driver, base_url)
        .open()
        .login("test@example.com", "password123")
    )

    assert "Welcome" in home.greeting_text

    home.add_first_product_to_cart()

    assert home.cart_count == 1
```

**改了什麼？**

- **Selector 集中在 PageObject 的 class attribute**（第一層分離）
- **Wait 內建在 method 裡**——`open()` 自帶等元件、`wait_until_loaded()` 在轉頁後等 ready、`add_first_product_to_cart()` 等到 cart 真的變了才返回（第二層分離）
- **Assertion 完全留在 test 裡**——PageObject 只負責動作跟讀資料（第三層分離）
- **Method 回傳下一個 PageObject**——支援 method chaining，test 讀起來就是業務動作的順序
- **`time.sleep` 全部消失**——換成 explicit wait，flaky 大幅降低

test 從十幾行混亂剪成五行業務語義。**未來 UI 改版？只動 PageObject。Test 一個字都不用變。**

---

## 四、重構後最容易再走偏的四個 anti-pattern

寫完 POM 不代表結束。POM 寫到一半最常出現的「假乾淨」狀態，通常是這四種：

### 1. God PageObject（一個 class 包整個網站）

寫一寫覺得「都是同一個 app 嘛，幹嘛分這麼多檔」，然後出現一個 `MyAppPage` class 裡面有 80 個 method、覆蓋從登入到結帳到後台。

> **判斷標準**：一個 PageObject 該對應「一個畫面 / 一個功能區塊」。如果你的 PageObject 名字無法用一個畫面截圖描述，它就太大了。

### 2. 太瘦的 PageObject（每個 method 只是 wrap 一個 click）

```python
# 反例
def click_login_button(self):
    self.driver.find_element(*self.LOGIN_BUTTON).click()

def click_logout_button(self):
    self.driver.find_element(*self.LOGOUT_BUTTON).click()
```

這種 method 沒提供任何抽象——它只是把 `driver.find_element().click()` 改寫了一次。**好的 PageObject method 應該包業務語義**：`login(username, password)` 而不是 `click_login_button()`。

> **判斷標準**：你的 method 名稱是描述「使用者要做什麼」（login、checkout、search），還是描述「操作 UI 哪個元件」（click_X、type_in_Y）？前者是業務語義，後者是 UI 語義。**業務語義才是 POM 的目的**。

### 3. Wait 散落到處（sleep 與 explicit wait 混用）

最常見的爛狀態：PageObject 內部寫了 explicit wait，但因為「有時候會 flaky」，又在 test 外面塞了幾個 `time.sleep(2)` 「保險」。

> **判斷標準**：你的 test 檔案裡如果出現 `time.sleep`，**99% 是 PageObject 的 wait 沒寫好**。回去把責任放對位置，不要用 sleep 補。

### 4. Assertion 寫進 PageObject

```python
# 反例
def login(self, username, password):
    # ...
    assert "Welcome" in self.driver.find_element(*self.USER_GREETING).text  # ⚠️
    return HomePage(...)
```

PageObject 一旦帶了 assertion，它就**只能服務一種 test 情境**——只測「登入成功」的那種。如果你想寫一個「登入失敗該怎麼樣」的 test？這個 PageObject 直接報錯，因為它預期登入會成功。

> **判斷標準**：PageObject 只負責「能不能做這件事」，不負責「做完之後對不對」。對不對是 test 的責任。

---

## 五、網頁 vs. 手機：共通的設計原則

Selenium 跟 Appium 是不同的框架，但**POM 的設計原則是 1:1 對應**。差別只在 selector strategy：

| 平台 | Selector 策略範例 |
|---|---|
| Web (Selenium) | CSS selector、XPath、ID |
| Android (Appium) | accessibility id、resource-id、UiSelector |
| iOS (Appium) | accessibility id、predicate、class chain |

一個簡化的 mobile 對照：

```python
# pages/mobile_login_page.py
from appium.webdriver.common.appiumby import AppiumBy

class MobileLoginPage:
    USERNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "username_input")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "password_input")
    LOGIN_BUTTON   = (AppiumBy.ACCESSIBILITY_ID, "login_button")

    # __init__ / open / login 結構與 Web 版一樣
    # 唯一差別：找元件用的 By 不一樣
```

**整段 PageObject 的結構、職責切分、method 命名邏輯——完全一樣**。Wait 策略也是同樣的（Appium 也有 WebDriverWait）。

換句話說——**POM 是設計模式，不是框架特性**。框架是工具，工具會換、會升級、會被取代（比如 Appium v2 → v3）；但**設計思維會跨工具沿用**。投資在設計思維上，比投資在某個框架的特定 API 上更值得。

如果你同時測網頁跟手機，可以考慮做一個 `BasePage` 抽出共用的 wait / find 邏輯，再讓 Web / Mobile 各自繼承。但這是進階話題，先把單一平台的 POM 寫好再說。

---

## 六、給接手爛 code 的人：重構的進場順序

如果你正在面對前人留下的 1500 行義大利麵，請忍住想全部重寫的衝動。重寫看起來最快，但**它通常會讓你卡在 50% 完成度的地獄**——舊 code 還沒淘汰、新 code 沒蓋完、兩邊都不能信。

我推薦的順序：

### 1. 先讓它能持續綠燈（不重構，先穩定）

把 `time.sleep` 改成 explicit wait、把最 flaky 的 case 加 retry——這些動作幾乎不動結構，但能立刻提高你接下來重構的安全感。**你不能在地震的房子裡裝潢**。

### 2. 從「最常壞的那個流程」下手

不要從「最簡單的」開始（那是 ego trap：你會選最容易的 case 來秀重構成果）。從**最常出問題、最痛的流程**先做——它的重構 ROI 最高，也最能幫團隊立刻減痛。

### 3. 拆三層的順序：Selector → Wait → Method 結構

這個順序是有意義的：

- 先把 selector 抽出來（最機械、最不會破事）
- 再把 wait 整理進 PageObject method（這時候你會看清楚每個動作該等什麼）
- 最後才動 method 結構與 method chaining（這個動到 test 介面，最容易破）

### 4. 全程綠燈不破

每一步重構結束都要跑一輪測試。**綠燈一旦破了不要繼續往下重構**——回頭把它修綠再走。這個紀律比任何技術細節都重要。

### 5. 不一次重構完全部 case

只重構你接下來會動到的部分。其他部分等到下次再碰它時再說。**重構是個持續的 90/10——90% 的 case 永遠不會被改寫，10% 在改寫的當下順手做就好**。

---

## 七、結語：POM 真正解的是「未來的你跟你同事」這個問題

寫到最後，我想退一步講一件事。

很多人覺得 POM 是為了「讓 code 更乾淨」。這個說法不算錯，但太抽象了。POM 真正在解的問題是這個：

> **這份 code 一年後，當原作者已經換工作了、UI 已經改版三輪了、團隊裡只剩沒看過這段 code 的新人——它還能不能被理解、被修改、被信任？**

POM 不是寫給此刻的你看的——它是寫給**未來的某一個人看的**，那個人可能是你自己（六個月後忘了一切的你），也可能是接手你這份遺產的同事。

寫到這一步，你會發現一件事——**POM 設計得好不好，會直接影響你能不能做有風險假設的探索式測試**。當你想驗證「在這個邊界條件下使用者會踩到什麼」，能不能快速用既有 PageObject 拼出一個新 case？這是 [〈問題驅動測試〉](/post/problem-driven-testing-intro/) 能不能落地的基礎建設。**POM 寫得爛，PDT 跑不起來**。

所以下次你打開那份 1500 行的爛 code，請記得：

> **寫到「能跑」，只是自動化測試的第一步。寫到「能被別人接手」，才是 QA 工程的紀律。**

這份紀律沒有人會在 sprint review 上鼓掌，但它會在某一個你已經離開團隊的早上，讓某個沒見過你的同事，順利把測試跑起來。

那個早上你不會在現場——但你寫過的 PageObject 會替你在現場。

---

## 延伸閱讀

- [Selenium 踩坑筆記：別盲目相信 By.ID](/post/selenium-troubleshooting/)
- [Appium v2 → v3 遷移指南](/post/appium-v2-to-v3-migration/)
- [問題驅動測試（PDT）：致命 Bug 藏在你沒問過的問題裡](/post/problem-driven-testing-intro/)
