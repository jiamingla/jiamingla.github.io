---
urlname: page-source-vs-find-element
title: UI 自動化跑得慢？先別怪裝置——page_source 與 find_element 的成本完全不同
date: 2026-06-06 07:00:00
tags: [軟體測試, 自動化測試, Appium, Selenium, 效能優化, UI scraping, page_source, find_element, 測試架構, 品質工程]
---

## 前言：47 列資料，掃一次 80 秒

某個自動化測試在掃一份列表——47 列、每列 4 個欄位。看起來不算大。

但實際跑下來——**單次掃描 80 秒**。整個測試流程要捲動 5 次列表才能蓋齊全部，於是這個 case 光「讀資料」就花掉 6-7 分鐘。

第一反應通常是：「裝置慢吧？網路差吧？換台手機試試？」

**但這次跟裝置無關，跟網路也無關**。問題在程式碼結構本身——而且這個結構錯誤在 UI 自動化教學裡幾乎沒人講。

這篇文章想拆三件事：

1. 為什麼一個簡單的 list scrape 會慢成這樣？
2. `driver.page_source` 跟 `find_element` 是兩個 cost model（成本結構）完全相反的指令
3. 什麼時候該用哪一個？

讀完這篇你會發現，自己過去寫的某些 UI 自動化，**可能可以快 10 倍以上**——而且一行寫死的 xpath 都不用加。

---

## 一、診斷：時間究竟花在哪？

那段 80 秒的 scrape 程式碼長這樣（簡化過、概念性）：

```python
def get_row_data(self, row_element) -> dict:
    name = row_element.find_child_element(NAME_LOCATOR).get_attribute('text')
    title = row_element.find_child_element(TITLE_LOCATOR).get_attribute('text')

    # 兩種佈局之一，需要 fallback
    try:
        price = row_element.find_child_element(PRICE_LOCATOR, timeout=1).get_attribute('text')
    except:
        price = row_element.find_child_element(ALT_PRICE_LOCATOR, timeout=1).get_attribute('text')

    rate = row_element.find_child_elements(RATE_LOCATOR, timeout=1)[0].get_attribute('text')

    return {'name': name, 'title': title, 'price': price, 'rate': rate}

def scrape_all(self) -> list[dict]:
    rows = self.find_all_rows()
    return [self.get_row_data(row) for row in rows]
```

每一個 row 看起來只是讀 4 個欄位。乾乾淨淨。

**但仔細數一下這段 code 會發出多少次「請求」**：

| 動作 | 次數（每 row） |
|---|---|
| `find_child_element(NAME)` | 1 |
| `find_child_element(TITLE)` | 1 |
| `find_child_element(PRICE)` 或 fallback | 1-2 |
| `find_child_elements(RATE)` | 1 |
| `.get_attribute('text')` × 4 | 4 |
| **小計** | **8-9 次** |

47 row × 9 次 = **大約 400 次請求**。

加上「捲動之後重新掃整個列表」的迴圈邏輯——每次 scroll 都把整個列表重掃一輪——5 次 scroll × 80 秒 = 400 秒。

每一次「請求」對應一次 **roundtrip（往返通訊）**。理解 roundtrip 是這篇文章的核心。

---

## 二、什麼是 roundtrip？

`find_element` 看起來像直接「找元件」，但底下發生的事其實是這樣：

```
你的 Python script (client)
        │
        │  「請幫我找 resource-id = NAME 的元件」
        ▼
   Appium server / WebDriver
        │
        │  「請幫我找這個元件」
        ▼
   Android device / browser
        │
        │  「找到了，element id = abc123」
        ▼
   Appium server
        │
        │  「找到了」
        ▼
   你的 Python script
```

從你的 script 發出請求、到結果回來——這一整段旅程叫**一次 roundtrip**。

對 Android UiAutomator2 而言，**一次 roundtrip 通常是 50-200ms**。看起來不長，但問題是：每一個 `find_element` 都要一次、每一個 `get_attribute` 也都要一次。

這就是為什麼 47 row × 9 次 = 80 秒。**這 80 秒裡，99% 的時間在等網路往返，不是在做事**。

當你看清楚這一層，第一個直覺是——

> **能不能一次抓完所有東西？**

答案是：能。叫 `driver.page_source`。

---

## 三、find_element：互動友善，批量災難

`find_element` 的設計是給你做「**互動**」用的：

- 點這個按鈕（找到 + click）
- 在這個輸入框打字（找到 + send_keys）
- 等這個元件出現（隱含等待 + 找到）

這些動作的特性都是——**你只要找一個元件，做一個動作**。一次 roundtrip 換一個操作，是合理的。

但當你要做的事是「**讀資料**」——而且要讀很多筆——這個工具瞬間變成災難：

- 找一個元件：1 次 roundtrip
- 拿那個元件的 text：又 1 次 roundtrip
- 拿它的 content-desc / class / bounds：再 N 次 roundtrip

讀 N 個元件的 M 個欄位 = **N × M 次 roundtrip**。

很多 QA 寫到這裡會走向另一個極端——**寫死 xpath，一次 bulk find（批量查找）**：

```python
prices = driver.find_elements(By.XPATH, '//*[@resource-id="Price-Text"]')
codes = driver.find_elements(By.XPATH, '//*[@resource-id="Code-Text"]')
# 然後用 index 對應 prices[i] 跟 codes[i] 是同一筆資料
```

這個版本確實快——從 400 次 roundtrip 降到 5 次（一個 field 一次 bulk find）。

但它的代價是：

1. **順序位移就壞掉** — 某幾筆資料剛好缺其中一個欄位，你的 index 對應就全錯
2. **沒有 row 邊界** — 表頭、分隔線、空 row 會混進來
3. **不通用** — 寫死 xpath，每個 APP / 頁面要重寫一份

如果你的 lib 是要跨多個產品共用的（這在實務上很常見），這條路根本不能走。

那有沒有「**bulk 讀，又不寫死 xpath**」的選項？有。

---

## 四、page_source：批量友善，但有它的代價

`driver.page_source` 是 Appium / WebDriver 提供的指令——**一次 roundtrip 回傳整個畫面當下的 XML 表示**：

```python
xml_text = driver.page_source   # ← 唯一 1 次 roundtrip
```

回傳的是一大段 XML（或 HTML，依框架而定）字串。例如 Appium 回傳的長這樣（簡化）：

```xml
<hierarchy>
  <android.widget.LinearLayout>
    <android.view.View resource-id="row_box">
      <android.widget.TextView resource-id="NAME-Text" text="..." />
      <android.widget.TextView resource-id="TITLE-Text" text="..." />
      ...
    </android.view.View>
    ...
  </android.widget.LinearLayout>
</hierarchy>
```

拿到這段 XML 之後，**所有解析都在記憶體裡進行，沒有任何 roundtrip**：

```python
import xml.etree.ElementTree as ET

def get_row_data_v2(self) -> list[dict]:
    xml = self.driver.page_source              # 1 次 roundtrip
    root = ET.fromstring(xml)

    rows = []
    for row in root.findall('.//*[@resource-id="row_box"]'):
        name_elem  = row.find('.//*[@resource-id="NAME-Text"]')
        title_elem = row.find('.//*[@resource-id="TITLE-Text"]')
        price_elem = row.find('.//*[@resource-id="PRICE-Text"]') or \
                     row.find('.//*[@resource-id="ALT-PRICE-Text"]')
        # fallback 邏輯一樣可以做，因為 XML 在記憶體裡查很快

        rows.append({
            'name':  name_elem.get('text', '') if name_elem is not None else '',
            'title': title_elem.get('text', '') if title_elem is not None else '',
            'price': price_elem.get('text', '') if price_elem is not None else '',
        })
    return rows
```

**估計效益：**

| 指標 | 原版（per-element） | 改版（page_source） |
|---|---|---|
| 單次 scrape | ~80s | ~1-3s |
| Roundtrip 數 | ~400 | 1 |

這就是 **10-50 倍的速度差距**——**而且不需要寫死 xpath，跨 APP 通用性也保留了**。

### 實戰延伸：雙向驗證的實作基礎

這種批量讀取的效能優勢，不只是讓測試跑得快，它還直接決定了**某些測試設計是否可行**。

以我們在[〈篩選後沒結果，是資料真的沒符合條件，還是篩選功能壞掉了？——自動化測試的五種解法〉](/post/empty-result-ambiguity-in-filter-testing/)中提到的「雙向驗證」為例：在該方案中，為了驗證篩選後的「空集合」是不是 bug，我們需要用 APP 自己的「無篩選狀態全量資料」作為基準（ground truth），跟當前篩選結果進行比對。

這意味著同一個測試流程中，我們需要抓取兩次完整的列表資料。

如果使用傳統的 `find_element` 逐筆讀取，每掃描一次列表都需要幾十秒甚至上百秒，做一次「雙向驗證」的成本會高到令人無法接受。然而，當我們利用 `page_source` 將每輪抓取降到常數級別的 1-2 秒時，原本昂貴的雙向驗證就變成了一個極其廉價且可靠的日常操作。

**沒有 page_source 帶來的效能釋放，很多高階的測試邏輯（如雙向驗證）在實務上根本不具備操作性。**

---

## 五、兩個工具的分工：互補不替代

說「page_source 比較快」是對的，但**這不代表它能取代 find_element**。它們是兩個 cost model 不同的工具，各有最佳場景：

| 場景 | find_element | page_source |
|---|---|---|
| 點按鈕、滑動、輸入 | ✅ 必用 | ❌ 沒辦法（它只讀，不操作） |
| 等元件出現（wait） | ✅ 必用 | ❌ 沒辦法 |
| 讀單一元件的單一屬性 | ✅ 直觀 | 🟡 也行但小題大作 |
| 讀大量元件的大量屬性 | ❌ 災難 | ✅ 必用 |
| 結構性檢視（樹狀關係、scope） | 🟡 痛苦 | ✅ 直觀 |
| 動態變化中的 UI | ✅ 隱含 wait | ❌ 只是當下 snapshot（快照） |

換句話說——

> **`find_element` 是給「跟 UI 互動」用的工具。`page_source` 是給「從 UI 讀資料」用的工具。**

它們不是替代品，是互補品。一個健康的自動化測試會**同時用兩者**：用 `find_element` 操作（點、滑、等），用 `page_source` 讀（一次抓多筆資料）。

---

## 六、page_source 的真實限制（5 個雷區）

吹完它的優點，講幾個會踩到的雷：

### 1. Lazy render（延遲渲染）：只看得到當下螢幕內的元件

Android 列表通常是 lazy render——**螢幕外的 row 根本不在 view tree（視圖樹）裡**。`page_source` 抓回來的 XML 就只有當下可視範圍。

意思是：**你還是要 scroll**。`page_source` 取代的是「scroll 後的 per-element scrape」，不是取代「scroll」這個動作本身。

### 2. 大型 view tree 會讓 page_source 自己變慢

UiAutomator2 在深層巢狀的 view tree 上，`page_source` 本身就可能 1-3 秒甚至 timeout。

**這是真實風險**——80 秒掉到 3 秒是常見，但偶爾會遇到「view tree 太肥，光 page_source 就要 5 秒」的情況。**所以實作前要先量一次**，不要假設它一定快。

### 3. 屬性名稱跟 find_element 不一致

`page_source` 的 XML 用的屬性名是 raw 的——例如 `resource-id`、`text`、`content-desc`。但 `WebElement.get_attribute('text')` 在某些版本可能對應不同名字。

**第一次切換時要 assert 兩邊抓到的內容一致**，再開始信任新版。

### 4. Encoding / 特殊字元

如果你抓的文字包含 `&`、`<`、`>`、emoji，XML parse 通常會自動處理 escape——但偶爾會有版本差異。**用真實資料 sample 測試一次**。

### 5. 動態 UI 的時間點問題

`page_source` 是「當下這一刻」的 snapshot。如果 UI 還在 loading、動畫中、有 spinner——你抓到的可能是中間狀態。

**對策**：page_source 之前要做 explicit wait（顯式等待，等到關鍵元件 visible），再 page_source。**用 find_element 等到穩定，再用 page_source 批量讀**——這就是兩個工具互補的最佳示範。

---

## 七、實務混合策略：一個健康的列表 scrape 流程

把上面所有原則串起來，一個典型的列表 scrape 應該長這樣：

```python
def scrape_full_list(self) -> list[dict]:
    all_data = []
    seen_ids = set()

    while True:
        # ① 用 find_element 等列表 ready
        self.wait_for_list_visible()

        # ② 用 page_source 一次讀整個可視範圍
        rows = self.parse_visible_rows_from_page_source()

        # ③ dedup（因為 scroll 之間可能重複）
        new_rows = [r for r in rows if r['id'] not in seen_ids]
        all_data.extend(new_rows)
        seen_ids.update(r['id'] for r in new_rows)

        # ④ 用 find_element 操作 scroll
        if not self.scroll_down_if_more():
            break

    return all_data
```

注意三個工具的角色：

- **`wait_for_list_visible`**：用 `find_element` 確保 UI ready
- **`parse_visible_rows_from_page_source`**：用 `page_source` 批量讀
- **`scroll_down_if_more`**：用 `find_element` 操作

每個工具都用在它最擅長的地方。

---

## 八、給仍在 per-element scrape 的你

如果你正在維護一份「掃資料慢得不合理」的自動化 code，這是診斷三步驟：

### 1. 加 timing log，先知道時間花在哪

```python
import time

def get_row_data(self, row):
    t0 = time.time()
    # ...原本邏輯
    print(f"single row scrape took {time.time() - t0:.2f}s")
```

如果單一 row 抓資料要 1-2 秒，那就是 per-element roundtrip 累加。如果單筆 0.1 秒以下、但累積很多，本質上也是同樣問題。

### 2. 量一次 page_source 本身的速度

```python
t = time.time()
xml = self.driver.page_source
print(f"page_source 耗時 {time.time() - t:.2f}s, XML 長度 {len(xml)}")
```

如果 page_source 本身就要 5 秒以上，這條路可能不適合你的 view tree。先想 mitigation（緩解措施，例如 reduce nesting、分段抓），再決定要不要走。

### 3. 寫一個並存版本，A/B 對比

不要一次重寫。**寫一個 `_v2` 方法，跟舊版並存幾天**，跑同樣的流程比對：

```python
old_data = self.get_rows_v1()  # 舊版 per-element
new_data = self.get_rows_v2()  # 新版 page_source
assert old_data == new_data, f"Mismatch: {old_data} vs {new_data}"
```

確認資料一致、新版穩定之後，舊版改成 `_legacy` 留作 fallback、新版扶正。

---

## 九、結語：知道工具的 cost model，比知道工具本身重要

寫到最後，我想退一步講一件事。

`find_element` 跟 `page_source` 在 Appium / Selenium 的文件裡都有——它們不是什麼隱藏指令、不是什麼進階技巧。**任何讀過官方文件的人都知道有這兩個東西**。

但很少人**真的理解這兩個東西的成本是不同階級**。`find_element` 是 per-call 一次 roundtrip，`page_source` 是一次 roundtrip 加上本地 parse。當你要掃 N 筆資料的 M 個欄位時——前者是 O(N×M) 次 roundtrip，後者是 O(1)。**這是線性 vs 常數時間，差距會隨資料量無限擴大**。

> **把 UI 自動化寫得「能跑」很容易。把它寫得「能 scale」需要一件事——你心裡要有 cost model**。

cost model 不是高深的東西。它就是這個問題：

> **我這行 code 觸發了多少次 client-device 通訊？**

問自己這個問題，再對照你的工具該用哪個——這份判斷，就是把自動化從「會跑」推到「會跑得好」的分水嶺。

下次你打開一個跑得慢的測試，先別急著怪裝置或網路。**先看看自己的 code 是不是在做 N×M 次 roundtrip**——如果是，page_source 在等你。
