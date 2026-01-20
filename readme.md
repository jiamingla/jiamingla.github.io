在一個典型的 Hexo 專案中，main 分支與 gh-pages 分支扮演的角色完全不同：main 儲存原始碼與設定檔（你的生財工具），而 gh-pages 儲存生成的靜態網頁檔案（實際給瀏覽器看的內容）。 
以下是兩者分別會有的主要檔案與資料夾：
1. main 分支 (原始碼分支)
這是你進行寫作、修改主題、調整設定的地方。
source/：最重要的資料夾，包含你的 Markdown 文章 (_posts/)、圖片或其他資源。
_config.yml：網站的全域設定檔（如網站標題、網址、部署路徑等）。
themes/：存放你下載或自定義的主題檔案。
scaffolds/：存放建立新文章時的模板。
package.json：列出專案所需的 Node.js 套件及其版本。
.gitignore：設定不需上傳的檔案，通常會包含 public/、node_modules/ 與 .deploy_git/。 
2. gh-pages 分支 (部署分支)
這是執行 hexo d 或透過 GitHub Actions 自動生成後的結果，內容對應本機的 public/ 資料夾。 
index.html：網站的首頁。
css/、js/、fonts/：由主題生成的樣式與腳本資源。
2024/01/20/post-name/：根據你的 permalink 設定生成的文章 HTML 頁面（資料夾結構視設定而定）。
archives/、categories/、tags/：彙整頁面的 HTML 檔案。
.nojekyll：告訴 GitHub Pages 不要使用內建的 Jekyll 引擎處理，這對 Hexo 正常顯示非常重要。
CNAME（選填）：如果你有綁定自定義網域，這個檔案會存在於此分支。 
核心概念：Source -> Public -> Deployment
你在 main 的 source/ 下寫 Markdown。
執行 hexo g 後，Hexo 會將其轉換為靜態 HTML 放到 public/。
執行 hexo d 後，Hexo 會將 public/ 的內容推送（Push）到 gh-pages 分支，完成發布。 