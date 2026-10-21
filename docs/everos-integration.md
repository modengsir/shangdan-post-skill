# 接入 EverOS（Cloud / 自托管）

EverOS 是给 Agent 的记忆操作系统：把每次任务记成 **Case**，把重复经验提炼成可复用的 **Skill**，用 **Memory Bank** 查看和管理全部记忆。本 Skill 的第 0 步（检索）和第 7 步（回存）正好对上它的两个动作。

产品与文档：
- 产品介绍：https://evermind.ai/everos
- Cloud 文档：https://docs.evermind.ai/cloud/overview
- 开源仓库（自托管）：https://github.com/EverMind-AI/EverOS
- Cloud 入口：https://everos.evermind.ai

## 为什么选它搭这个 Skill
- **Case → Skill 是现成的**：商单经验的沉淀不用自己设计算法，跑过的单自动变下次的 SOP 素材。
- **多格式直接吃**：Brief 的 PDF、表格、文档、邮件原生解析成可检索记忆，不用先转纯文本。
- **记忆可管理**：Memory Bank 里可查、可纠正、可删除、可评价——记错能改，这点对“红线类记忆”至关重要。
- **不锁死**：Cloud 与自托管共用同一套 API，记忆可导出为 Markdown，先 Cloud 起步、以后搬回家不用改 Skill。

## 接入步骤
1. 注册 EverOS Cloud（或按开源仓库 Quick Start 自托管，本地版一个 API Key 即可起服务）。
2. 在助理的环境里配置好访问方式（API Key 走你的密钥管理，**不要写进仓库和帖子**）。
3. 把这三类存量先喂进去（第 0 步的初始语料）：
   - 你的《商单解析清单》/ 历史 SOP 文档；
   - 过去几单的 Brief（先脱敏：报价页、联系人页删除或打码）；
   - 踩坑记录（哪怕是一句话一条：“X 单链接放正文被驳回，应放评论区”）。
4. 对助理说一句：“商单帖 Skill 的记忆后端用 EverOS。”之后每单自动执行：开单先 search、收单 add 一个 Case。

## 操作映射（给助理看的接线表）
| Skill 时机 | EverOS 动作 | 要点 |
|---|---|---|
| 第 0 步 | search：品牌名 / 品类 / “商单红线” | 用 hybrid 或 agentic 检索；结果按时间与可信度排序后再汇总 |
| 第 1 步后 | add：本单 Brief 解析表 | 以本单 slug 为 session/project 标识，方便整单召回 |
| 第 5 步前 | search：“<品类> 有效打法” | 给成稿找历史证据与有效钩子类型 |
| 第 7 步 | add：复盘 Case | 数据、品牌反馈、结论分开写，利于后续提炼 Skill |
| 发现错误 | correct / delete by ID | 在 Memory Bank 先定位，再修正；删后复查衍生记忆已一并清掉 |
| 定期 | 打开 Memory Bank 巡检 | 看自动提炼出的 Skill 是否准确，不准的评价/纠正——它会据此改进 |

## 一个真实形态的闭环（示意）
开单检索到历史教训“福利路径必须写全” → 本单成稿时福利写到最后一步 → 发布后品牌反馈“信息完整、零修改通过” → 复盘回存为 Case → 多个类似 Case 后，这条经验沉淀为 SOP 条目 → 下一单第 0 步直接命中，不用再翻聊天记录。

## 注意事项
- 本地自托管版的检索模式与你的模型配置有关（只配 LLM 时可用关键词检索；混合/智能体检索需要再配 embedding 与 rerank），接入时按官方 Quick Start 的分级说明核对你启用的能力。
- 免费额度与 Pro 价格以 EverOS 官网当前公布为准，本文档不写死数字。
