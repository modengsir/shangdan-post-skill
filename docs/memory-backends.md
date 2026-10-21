# 记忆层：可插拔的三种后端

Skill 本体不绑定任何产品，只依赖 4 个操作。换后端，改的是助理的“记忆接线”，不改流水线。

## 接口约定
| 操作 | 语义 | 本地 Markdown 实现 | EverOS 实现 |
|---|---|---|---|
| `memory.search(query)` | 按关键词/语义找历史 Case、SOP、档案 | 在 `memory_local/` 全文检索（助理读文件） | Cloud API 的 search（keyword / hybrid / agentic） |
| `memory.add(case)` | 存一条新经验 | 新建 `cases/YYYY-MM-DD-<品牌>.md` | API add + flush，过程记为 Case |
| `memory.correct(id, ...)` | 纠正一条记错的 | 直接改对应文件并注明日期 | Memory Bank / API 纠正该条记忆 |
| `memory.delete(id)` | 删一条过时/敏感的 | 删文件（或移入 trash） | API 按 ID 删除（含衍生记忆） |

## 三种后端对比
| | 零依赖 | 本地 Markdown | EverOS |
|---|---|---|---|
| 成本 | 0 | 0 | Cloud 有免费额度；自托管开源免费 |
| 经验沉淀 | 无 | 靠助理每次读文件汇总 | Case 自动提炼为 Skill，越用越准 |
| 检索 | 无 | 全文关键词 | 关键词/向量/混合/智能体检索 |
| 数据在哪 | 不保存 | 你本地，可 git | Cloud 托管，或自托管在自己机器 |
| 适合 | 先试流程 | 个人创作者起步（推荐） | 单量多、多 Agent 共用经验时 |

## 选型建议
- 每月 ≤2 单：本地 Markdown 足够，经验文件也就几十个。
- 每月多单、或多个助理/Agent 要共用同一套经验：上 EverOS。自托管与 Cloud 同一套 API，之后迁移不改 Skill。
- 团队协作：EverOS 按 owner / project 分域，同一套 SOP 可给整个团队的 Agent 用。

## 隐私规则（三后端通用）
- 报价、结算、品牌联系人：只许存进本地私有区（本地模式的 `memory_local/private/`，且该目录默认不进 git；EverOS 模式则干脆不存原文，只存“结算周期 30 天”这类脱敏结论）。
- 对外材料（帖子、截图、录屏、开源示例）出现任何价格/邮箱/手机号，先脱敏再发布。
