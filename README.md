# Monetization Decision Harness V0

一句话：这是一个让 Codex 根据真实证据和项目阶段，纠正变现决策并把长期状态保存在仓库里的个人 Harness。

它不是聊天机器人、名人圆桌或新的 Agent Runtime。Codex 本身负责推理和工具调用；本仓库只提供变现领域的规则、Thinking Skills、项目记忆和验收用例。

## 它怎么工作

```text
你提出一个变现问题
→ Codex 读取项目 IDEA.md + STATE.md
→ 判断 Stage、FACT / ASSUMPTION / DECISION / EXPERIMENT
→ 找到当前最大未知量
→ 只选择 1～2 个必要 Thinking Skill
→ 综合成一个判断和下一步
→ 只有持久状态变化时才写回 Workspace
```

总原则是：Stage Before Solution、Evidence Before Confidence、Transaction Before Automation、Value Before Product、Leverage After Repetition。

## 最快开始

在仓库根目录运行：

```bash
python3 scripts/new_project.py lawyer-case-organizing \
  --goal "验证律师是否愿意为案件资料整理持续付费"
```

脚本会：

- 从 `workspace/_templates/project/` 创建完整阶段目录；
- 初始化 `IDEA.md` 和 `STATE.md`；
- 写入当天日期、项目名和目标；
- 更新 `workspace/_index.md`；
- 拒绝覆盖已有项目。

然后在这个仓库中启动 Codex，并输入：

```text
继续 workspace/lawyer-case-organizing。
先完整读取 IDEA.md 和 STATE.md，告诉我当前 Stage、最大未知量和一个下一步。
```

继续已有项目时只需把项目名换掉。找不到项目名时先看 [`workspace/_index.md`](workspace/_index.md)。不依赖原来的聊天 Thread。

## Workspace

每个真实项目根目录只保留两个内容入口：

```text
workspace/<project>/
├── IDEA.md                  # 项目为何存在
├── STATE.md                 # 唯一当前状态快照
├── 01-opportunity/
├── 02-problem-validation/
├── 03-business-validation/
├── 04-experiments/
├── 05-transactions/
├── 06-leverage/
├── 07-productization/
├── 08-scaling/
└── 99-archive/
```

不要在项目根目录创建 `notes.md`、`report-final.md` 或临时分析。详细材料进入所属阶段；不知道更具体的位置时，进入当前阶段的 `analysis/`。

`STATE.md` 只保存当前 Snapshot 和关键链接。历史事实、实验记录、付款证据、阶段回退原因都留在对应阶段目录，因此文件不会无限膨胀。

完整写入与恢复规则见 [`docs/workspace-protocol.md`](docs/workspace-protocol.md)。

## 如何记录事实

直接告诉 Codex 发生了什么，并提供可引用的证据位置。例如：

```text
今天客户 A 已支付 500 元，付款凭证已脱敏放在这个文件里。
请按 Harness 协议登记事实和交易，并更新当前状态。
```

Codex 应分别登记：

- `T001`：交易本身；
- `F001`：带证据链接的事实；
- `STATE.md`：当前交易计数、Stage、最大未知量和下一步；
- `workspace/_index.md`：如果 Stage、Status 或 Next Gate 改变。

“客户应该喜欢”“市场很大”“某个 Skill 认为可行”都不是 FACT。对象格式和 ID 规则见 [`docs/object-protocol.md`](docs/object-protocol.md)。

## 如何记录实验

告诉 Codex要验证的假设和你能承受的上限：

```text
我决定用 7 天向 10 名独立律师出售 500 元的人工整理服务，
最多投入 300 元；2 笔付款算成功，10 次合格报价且 0 付款算失败。
请登记实验并更新 STATE。
```

一个有效 `E001` 必须包含：被测试的 Assumption、真实行为/付款信号、最大下行、成功/失败条件、期限和停止条件。实验建议只有在你明确接受后才成为 DECISION 并写入 Workspace。

## 如何判断 Stage

Stage 表示“下一个必须解决的未知量”，不是产品看起来多完整。

| Stage | 当前主要问题 |
| --- | --- |
| `opportunity_discovery` | 哪个真实问题值得调查？ |
| `problem_validation` | 问题是否真实、重复且重要？ |
| `business_validation` | 谁为哪个结果付钱，为什么现在付？ |
| `experiment_validation` | 怎样用最小安全实验获得行为证据？ |
| `transaction_validation` | 第一笔钱能否独立重复？ |
| `leverage_discovery` | 哪些重复工作能成为 SOP 或资产？ |
| `productization` | 什么最小产品能保留已验证价值？ |
| `scaling` | 获客和交付能否在经济上持续扩大？ |

Stage 可以回退。产品上线后无人复购，应回到 `business_validation`，而不是默认继续加功能。详细 gate 和回退信号见 [`docs/stage-model.md`](docs/stage-model.md)。

## 五个 Thinking Skill

| Skill | 什么时候用 | 不负责什么 |
| --- | --- | --- |
| `opportunity-finder` | 没有明确客户/问题、只有模糊方向 | 凭空列 AI 产品、证明市场成立 |
| `assumption-challenger` | 把假设当事实、问题问错、开发/研究在逃避验证 | 人格诊断、只拆不建 |
| `business-filter` | 判断客户、付款结果、替代方案、价格和重复逻辑 | 用热度或赞美证明商业模式 |
| `experiment-designer` | 设计小实验；重大下注、零付款大开发时强制考虑 | 无下行上限的“试试看” |
| `leverage-designer` | 重复付款或重复有效交付后做 SOP、自动化、代码/媒体资产 | 在价值未重复前推动产品化 |

`monetization-orchestrator` 是领域路由器，不是第六个人格。它按 State 选择最少必要 Skill，再给出一个综合结论。来源 Persona、保留内容和边界见 [`docs/source-mapping.md`](docs/source-mapping.md)。

## Harness 什么时候会主动打断你

以下情况不应直接顺着做：

- 付款为 0，却准备设计完整 SaaS、数据库、UI 或复杂 Agent；
- 因为 AI 能实现，就断言市场存在；
- 因为一个人付款，就立刻产品化；
- 用继续研究、继续写代码代替报价或销售；
- 准备辞职、All-in、投入数月或大量资金；
- 依赖单一客户、平台或 API，失败会让项目出局；
- 产品已上线但没有复购，仍想靠加功能解决。

这时输出应该先说明当前最大未知量、哪些是 ASSUMPTION，再给一个更小的现实行动。

## 一个项目的真实生命周期

以“律师案件资料整理”为例：

1. `opportunity_discovery`：记录律师如何用文件夹和人工命名处理零散资料。
2. `problem_validation`：观察问题是否在新案件到来时重复，并记录耗时与风险。
3. `business_validation`：确认承办律师还是律所付钱、购买的是整理结果而不是软件。
4. `experiment_validation`：用 7 天 Concierge 报价测试 `A001`，而不是先做后台。
5. `transaction_validation`：出现一笔 500 元付款，只能登记“一个人付过一次”；继续测试独立复购。
6. `leverage_discovery`：多个客户重复购买后，把分类、命名、质检步骤测量成 SOP。
7. `productization`：只把稳定步骤做成窄工具，并保持人工判断与回滚路径。
8. `scaling`：在复购、交付质量和单位经济成立后测试获客。

如果第 7 步后没人复购，记录证据并回到第 3 步，不删除历史。

## 如何查看历史

先读 `workspace/_index.md`，再读项目的 `IDEA.md` 与 `STATE.md`。根据 `STATE.md` 的链接打开当前实验、付款证据或最近一次阶段变化。归档材料进入 `99-archive/`，但稳定 ID 不因移动而改变。

## 如何增加新的 Thinking Skill

未来可以增加 `product-designer`、`execution-simplifier` 或 `decision-auditor`，V0 不实现它们。新增时：

1. 在 `.agents/skills/<skill-name>/` 创建符合 Codex Skill 规范的 `SKILL.md` 和 `agents/openai.yaml`。
2. 把长模型、来源和 few-shot 放入 `references/`、`examples/source/`、`examples/local/`，记录 License 与 commit。
3. 让 Skill 读取 Workspace、遵守 [`docs/review-protocol.md`](docs/review-protocol.md)，并明确使用/禁用边界。
4. 在 orchestrator 的 evidence-based routing rule 中增加状态条件，不按关键词或人物名路由。
5. 增加至少一个应触发、一个不应触发、一个与既有 Skill 冲突的 Eval。
6. 运行完整校验，确保常规路由仍只有 1～2 个 lens。

Orchestrator 只依赖领域 Skill 名，不依赖 Persona 名，因此可以扩展而无需改变 Workspace 协议。

## 验证

运行完整 V0 验收：

```bash
python3 scripts/validate_repo.py
```

它会检查：

- 六个 Skill、触发描述、UI metadata 和来源快照；
- 原 examples/references/LICENSE 与本地只读源的哈希一致性（原目录存在时）；
- Workspace 模板和项目根目录不膨胀；
- 在临时目录真实创建项目并验证拒绝覆盖；
- 本项目 authored Markdown 链接；
- 10 个路由、纠偏、Stage、Evidence、Action、Persistence 与 Resumption 场景。

也可以只运行 Evals：

```bash
python3 evals/run_evals.py
```

## V0 明确不做

V0 没有 Web UI、API Server、数据库、RAG、MCP Server、自定义 Agent Loop、Agent 投票/辩论、用户/权限系统、自动定时任务或 SaaS 化。Evals 是可审计的场景与 golden traces，不是确定性 LLM 行为保证；模型输出仍需要靠仓库规则、真实使用和新增失败用例持续校正。

## 关键目录

```text
AGENTS.md                         Runtime Constitution
.agents/skills/                   六个 repo-level Skills
docs/                             Stage、对象、审查、来源与写入协议
workspace/_templates/project/     项目模板
workspace/_index.md               个人商业知识库入口
scripts/new_project.py            项目初始化
scripts/validate_repo.py          完整验收
evals/cases/                      场景规范
evals/results/                    手工模拟 golden traces
evals/fixtures/                   Repo-only 恢复测试材料
```
