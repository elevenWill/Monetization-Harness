# Monetization Decision Harness V0

这是一个 Conversation-First 的个人变现决策 Harness：你只需要和 Codex 对话，Harness 会判断是否需要建立或恢复项目、当前应该解决哪个未知量，并在真正发生持久变化时维护 Workspace。

它不是名人 Agent 圆桌，也不实现第二套 Agent Runtime。Codex 负责推理、工具调用和文件维护；本仓库提供变现领域的规则、Thinking Skills、长期记忆和行为验收场景。

## 开始使用

1. 在这个仓库根目录启动 Codex。
2. 直接说你的赚钱想法。

例如：

```text
我最近在研究 AI 带货短视频，
感觉这里可能有变现机会，但我还没想清楚怎么做。
```

就这些。你不需要创建项目、填写 slug、选择 Stage、建立目录、更新索引或手工调用 Persona。

Harness 会自动判断当前对话属于哪种情况：

- 普通知识问题或一次性泛讨论：正常回答，不创建 Project。
- 明确且值得持续推进的新变现方向：创建一个最小 Project，并继续当前回答。
- 明显属于已有方向的新进展：恢复对应 Project，读取状态后继续。
- 同时可能属于多个 Project：先避免写错；能安全分析时继续分析，只有归属会影响持久化时才请你确认。

## 三个 Conversation-First 示例

### 1. 新方向

```text
用户：
我最近发现很多律师处理案件材料特别乱，
我想看看这里有没有变现机会。
```

Runtime 会检查现有 Workspace；没有匹配项目时自动建立最小 Project，初始 Stage 为 `opportunity_discovery`，优先使用 `opportunity-finder`，必要时使用 `assumption-challenger`，然后继续讨论你应该观察什么。不会要求你先起名或运行命令。

### 2. 继续旧 Project

```text
用户：
昨天我又问了两个律师，
其中一个说愿意给 500 元让我先做一次。
```

Runtime 会根据索引、`IDEA.md` 和 `STATE.md` 匹配已有律师项目，区分“口头愿意”与“真实付款”，登记应该持久化的新信息，按需创建对应阶段材料，并继续判断下一步。不会再建立一个重复项目。

### 3. 普通问题

```text
用户：
Naval 和 Taleb 最大区别是什么？
```

正常回答，不创建 Project，不修改 Workspace。

## Conversation First，Workspace Second

Workspace 是 Runtime 为了以后继续理解你而维护的长期记忆，不是你为了使用 Runtime 必须维护的项目管理工具。

新 Project 自动创建时只有：

```text
workspace/ai-commerce-short-video/
├── IDEA.md
└── STATE.md
```

内部目录名由 Runtime 自动生成短而稳定的 kebab-case slug。它只是内部 ID；用户不需要参与，创建后也不会因为项目展示名称变化而轻易重命名。

`IDEA.md` 只记录用户已经表达的初始方向、目标、目前认为的用户和关键假设。缺失内容标记为 `unknown`，不会由模型擅自补全。

`STATE.md` 是当前 Stage 的唯一权威入口，包含当前目标、FACT、ASSUMPTION、DECISION、EXPERIMENT、交易计数、最大未知量、Next Gate 和 Next Action。

## Workspace 按真实经历生长

Stage 是状态，不是目录。目录存在只表示历史上确实产生过相关材料；Stage 目录不要求连续，也不允许为了结构完整而预建空目录。

```text
无 Project
↓ 对话形成值得持续追踪的方向
IDEA.md + STATE.md
↓ 真正记录 O001
01-opportunity/O001.md
↓ 用户确认一个真实实验
04-experiments/E001.md
↓ 收到第一笔真实付款
05-transactions/T001.md
```

因此下面完全合法：

```text
workspace/project-a/
├── IDEA.md
├── STATE.md
├── 01-opportunity/
│   └── O001.md
├── 04-experiments/
│   └── E001.md
└── 05-transactions/
    └── T001.md
```

没有独立 Business Artifact 时，即使 `STATE.md` 的 Stage 是 `business_validation`，也不需要创建 `03-business-validation/`。详细规则见 [`docs/workspace-protocol.md`](docs/workspace-protocol.md)。

`workspace/_index.md` 是 Runtime 自动维护的 Project Registry。它只用于发现、匹配和导航，不要求用户手工编辑。

## 什么信息会写入 Workspace

Conversation First 不等于记录每句话。只有以下持久变化才写入：

- 新 Project 被明确确立；
- durable FACT 或真实 Transaction；
- Assumption 状态变化；
- 用户明确接受的 Decision；
- 有边界和停止条件的 Experiment；
- Stage、Next Gate 或 Material Risk 变化。

随口 brainstorm、普通解释、尚未接受的建议和 Thinking Skill 的判断不写入磁盘。

你只需要自然地报告进展，例如：

```text
今天真的有人给了我 300 元，让我帮他做一条商品视频。
```

Runtime 负责匹配项目、登记 `F001` / `T001`、按需创建交易目录、更新 State，并避免把第一笔付款误判成可重复生意。

对象与 stable ID 规则见 [`docs/object-protocol.md`](docs/object-protocol.md)。

## Stage

Stage 表示“当前最早且最重要的未解决 gate”，不是产品完成度，也不由目录是否存在决定。

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

Stage 可以回退。产品上线后无人复购，应回到 `business_validation`，而不是默认继续加功能。完整 gate 见 [`docs/stage-model.md`](docs/stage-model.md)。

## 五个 Thinking Skill

| Skill | 什么时候使用 | 不负责什么 |
| --- | --- | --- |
| `opportunity-finder` | 没有明确客户/问题，只有模糊方向 | 凭空列 AI 产品、证明市场成立 |
| `assumption-challenger` | 把假设当事实、问题问错、开发/研究在逃避验证 | 人格诊断、只拆不建 |
| `business-filter` | 判断客户、付款结果、替代方案、价格和重复逻辑 | 用热度或赞美证明商业模式 |
| `experiment-designer` | 设计小实验；重大下注或零付款大开发时强制考虑 | 无下行上限的“试试看” |
| `leverage-designer` | 重复付款或重复有效交付后建立 SOP、自动化和资产 | 在价值未重复前推动产品化 |

`monetization-orchestrator` 是 Project lifecycle、路由和综合协调器，不是第六个人格。它通常选择 1～2 个必要 Skill，再输出一个综合判断。Persona 来源与保留内容见 [`docs/source-mapping.md`](docs/source-mapping.md)。

## Harness 什么时候会打断你

- 付款为 0，却准备开发完整 SaaS、数据库、UI 或复杂 Agent；
- 因为 AI 能实现，就断言市场存在；
- 因为一个人付款，就立刻产品化；
- 用继续研究或写代码代替真实报价；
- 准备辞职、All-in、投入数月或大量资金；
- 依赖单一客户、平台或 API，失败会让项目出局；
- 产品已上线但没有复购，仍想默认靠加功能解决。

这时 Runtime 会先指出当前最大未知量和未经验证的 Assumption，再给更小的现实行动。

## Behavior Acceptance Scenarios

[`evals/cases/`](evals/cases/) 保存约六个核心 Harness Behavior Acceptance Scenarios，用于修改 `AGENTS.md`、Skills、Router 或 Stage 规则时做人工行为回归。

它们不是自动启动 Codex 的 LLM Evaluation Framework，也不把手工编写的理想答案伪装成真实 Runtime 测试。核心覆盖：自动 Bootstrap、过早开发、第一笔付款、重复付款与 leverage、重大下注、Stage 回退，以及 Workspace lazy growth。

## 开发校验

维护本仓库本身时，可选运行：

```bash
python3 scripts/validate_repo.py
```

这是开发工具，不是使用 Harness 的前置步骤。它只检查可确定验证的内容，例如 Skill 结构、source provenance、链接、STATE 基本字段、Workspace lazy invariant 和 Eval case 结构；不声称验证真实 Codex 推理质量。

## V0 边界

V0 没有 Web UI、API Server、数据库、RAG、MCP Server、自定义 Agent Loop、Agent 投票/辩论、用户/权限系统或自动定时任务。Project discovery、bootstrap、resume、Stage 路由和文件维护直接由 Codex Runtime 按仓库协议执行。
