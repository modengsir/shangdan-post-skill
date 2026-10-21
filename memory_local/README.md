# 本地 Markdown 记忆层

零云端、纯文本的经验库。助理用读文件 + 全文检索实现 `memory.search`，用新建/修改文件实现 add / correct / delete。

## 结构
```
memory_local/
  profile.md            # 创作者档案（由 profile.example.md 复制改名）
  profile.example.md    # 档案模板（本仓库自带）
  sop.md                # 你沉淀的商单 SOP（自己维护，助理只提议修改）
  cases/                # 每单一个复盘文件：YYYY-MM-DD-<品牌slug>.md
  private/              # 报价 / 结算 / 联系人（默认 .gitignore，不进仓库）
```

## 约定
- Case 文件名带日期，方便按时间排序与检索。
- `sop.md` 只收“验证过两次以上”的结论；单次经验先留在 Case 里，别急着升 SOP。
- correct = 直接改文件并在文末加一行「YYYY-MM-DD 纠正：原 X 改为 Y，因为……」；delete = 删除文件（重要单先备份）。
- 换到 EverOS 时，把 `profile.md`、`sop.md`、`cases/` 逐份喂进去即可完成迁移，格式不用改。
