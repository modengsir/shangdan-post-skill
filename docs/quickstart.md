# 快速开始（5 分钟）

## 你需要什么
- 一个支持 Agent Skills 的 AI 助理（Claude Code、Codex 或任何能读 `SKILL.md` 并按其行事的 Agent）。
- 可选：EverOS Cloud 账号（用记忆托管模式时），或什么都不用（本地 Markdown 模式）。

## 步骤
1. **安装 Skill**：把仓库根目录的 `SKILL.md`（连同 `templates/`、`docs/`）放进你 Agent 的 skills 目录；不支持 skills 目录的 Agent，就在对话开头让它先读 `SKILL.md`。
2. **填创作者档案**：复制 `memory_local/profile.example.md` 为 `profile.md`，用 10 分钟写清：定位、人设语气、禁区、主平台与常用规格。档案质量决定成稿像不像你。
3. **（可选）选记忆后端**：零依赖 / 本地 Markdown / EverOS 三选一，见 `memory-backends.md`。本地模式无需任何配置，档案和 Case 都在 `memory_local/`。
4. **开第一单**：
   - 可选脚手架：`python3 scripts/new_campaign.py <slug> --brand <品牌>`，会在 `campaigns/<slug>/` 生成 brief / 五问 / 大纲 / 成稿 / 复盘五个空文件。
   - 把 Brief 文件交给助理并说：“按商单帖 Skill 走这个单。”
5. **你只需要做两件事**：在拍板步选角度；发布前看一眼自检结果。中间的解析、五问、成稿、自检由助理走完。
6. **发布后说一句“复盘这单”**：助理会把本单记成 Case 回存。下一单它会先把相关经验调出来——从这一刻起，经验开始复利。

## 验收标准（第一单跑完自查）
- [ ] 解析表 9 项都有内容，缺失项进了“待确认问题”而不是被编出来
- [ ] 五问表五项都有具体答案，钩子是写好的原文不是描述
- [ ] 成稿里必讲点齐、福利路径完整、 Offer 只出现一次
- [ ] 演示 / 数据类内容是真实的，没实跑的部分是占位符
- [ ] 复盘 Case 已回存到你选的记忆后端
