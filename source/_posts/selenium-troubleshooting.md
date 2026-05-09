---
urlname: selenium-troubleshooting
title: Selenium 踩坑筆記：別盲目相信 By.ID，解析重複 ID 下的定位排序邏輯
date: 2026-01-20 16:13:17
tags: selenium
---

# Selenium 踩坑筆記：別盲目相信 By.ID，解析重複 ID 下的定位排序邏輯

By.ID 和 By.XPATH 在底層掃描邏輯與規範約束力上的不同。
這次明白了如果同一個ID有出現在畫面上的好幾個地方，用XPath雖然比較慢，但比較穩定不會定位到錯誤的元素

1. By.ID 的實作：優化優先 (Fast Lookup)
在多數瀏覽器和 Android 系統中，ID（或 resource-id）被設計為一個「快速索引」。

實作方式：

系統通常會維護一個 Hash Map（雜湊表） 或索引表。當你調用 find_elements (By.ID, "...") 時，驅動程式並不一定會從根節點乖乖地開始遍歷，而是直接向系統底層詢問：「誰的 ID 是這個？」

排序特點：

由於底層索引表的目的是「快」，它有時會返回最先被系統註冊到索引中的元素。在 Android UIAutomator 中，如果一個佈局是異步渲染的，或者某些 View 被優化（如 merge 標籤），索引返回的順序並不絕對保證是物理 DOM 順序。

為什麼抓到子元素？

在 Android 的 Accessibility Node 樹中，有些父元素會被標記為「僅作為容器（Non-important for accessibility）」，而底層搜尋引擎可能會優先返回「有意義」的葉子節點（Leaf Nodes）。

2. By.XPATH 的實作：路徑規範 (Tree Walking)
XPath 的實作邏輯完全不同，它是一套嚴格的 W3C 標準演算法。

實作方式：

XPath 引擎會強迫進行一次完整的 DOM Tree Walker。它必須解析整個樹狀結構，以確保符合所有路徑約束（例如 // 代表任何深度，.. 代表父級）。

排序特點：

根據 XPath 規範，結果集（Node-set）必須按照 Document Order（文件順序） 排列。

文件順序定義： 節點的出現順序與它們在 XML / HTML 源碼中「起始標籤」出現的順序一致。

結果：

因為父標籤 <android.view.View> 絕對出現在子標籤之前，所以 XPath 返回的列表第一個元素 百分之百 會是父元素。

3. 實作方式與排序對照表  

| 特性 |	By.ID / By.ResourceID |	By.XPATH |
| :------ | :------: | ------: |
| 底層原理 |	索引查詢 (Lookup / Index) |	樹狀遍歷 (Tree Traversal) |
| 執行速度 |	極快（直接定位） |	較慢（需要解析整個 DOM） |
| 順序保證 |	弱（取決於底層 OS 註冊順序） |	強（嚴格遵循文件 DFS 順序） |
| 適用場景 |	元素 ID 唯一且明確時 |	需要處理複雜層級或重複 ID 時 |
