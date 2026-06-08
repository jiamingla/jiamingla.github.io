# Antigravity Git Commit Rules

當在此專案中生成 Git commit 訊息或規劃 commit 切塊時，必須嚴格遵守以下規範：

1. **參考主要規範**：請參閱 [.github/copilot-instructions.md](../.github/copilot-instructions.md) 中定義的 commit 訊息規範。
2. **語言與長度限制**：使用繁體中文，Subject line 控制在 25 個漢字以內。
3. **動詞與目錄對應**：
   - 動到 `notes/` 使用「新增備忘/整理觀察/更新筆記」
   - 動到 `source/_drafts/` 使用「新增草稿/補骨架/補素材」
   - 動到 `source/_posts/` 使用「新增文章/更新文章」
   - 檔案搬動/重命名使用 `refactor:`，純小修正使用 `fix:`
4. **嚴禁公文化/行銷詞彙**：禁止使用「強調 X 的重要性」、「強化 SEO」等虛浮的描述。
5. **執行限制**：**嚴禁**自動執行 `git commit` 或 `git push`，必須先列出切塊與建議 commit message，交由使用者手動執行。
