# Monetization Decision Harness V0

这是一个 Conversation-First 的个人变现决策 Harness：你只需要和 Codex 对话，Harness 会判断是否需要建立或恢复项目、当前 Stage 最早还缺什么证据，再选择网页研究、直接观察、真实报价、付款或交付中最能改变决定的现实证据，调用最少的 Thinking Skills，并在真正发生持久变化时维护 Workspace。

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

Runtime 会检查现有 Workspace；没有匹配项目时自动建立最小 Project，初始 Stage 为 `opportunity_discovery`。如果结论依赖公开市场，它先做轻量现实扫描，再把取得的事实交给 `opportunity-finder`，必要时使用 `assumption-challenger`。不会要求你先起名、运行命令或手工触发研究。

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

Project bootstrap 本身只创建：

```text
workspace/ai-commerce-short-video/
├── IDEA.md
└── STATE.md
```

内部目录名由 Runtime 自动生成短而稳定的 kebab-case slug。它只是内部 ID；用户不需要参与，创建后也不会因为项目展示名称变化而轻易重命名。

`IDEA.md` 只记录用户已经表达的初始方向、目标、目前认为的用户和关键假设。缺失内容标记为 `unknown`，不会由模型擅自补全。

`STATE.md` 是当前 Stage 的唯一权威入口，包含当前目标、FACT、ASSUMPTION、DECISION、EXPERIMENT、交易计数、最大未知量、Next Gate 和 Next Action。只有真正开始分析一个购买情境后，它才会增加可选的 `purchase_trigger` 摘要；新项目不会预填一屏空字段。

如果同一轮随后真的完成了市场研究，那是 bootstrap 之后的独立持久化动作：Runtime 可以懒创建一个非空的 `01-opportunity/research/R001-….md`，但不会预建研究目录，也不会在项目根增加 `MARKET.md` 或 `RESEARCH.md`。

## Harness 会主动调查真实市场

Harness 不再只依赖用户描述和思维模型。当判断涉及“是否有人做成、平台是否允许、当前价格、用户是否接受、竞品和失败案例、是否值得大额投入”等当前外部事实时，Runtime 才进入 Market Reality Gate。Reality Evidence First 不等于 Web First：能由真实工作流、报价、付款、交付或复购直接回答的问题，不用网页研究代替。

你不需要说“请使用 Agent Reach”。当你问“这个想法是否可行”“有没有人做成”“平台是否允许”“用户是否接受”或“应该参考谁”时，Harness 会判断是否需要联网，并自动选择 Agent Reach 或当前可用的 Web 工具。

```text
Conversation → Resolve Project
↓
Evidence-derived Stage → earliest unresolved uncertainty
↓
选择最便宜且能改变决定的 Reality Evidence
├─ 复用新鲜且范围匹配的证据
├─ 直接观察 / 联系 / 报价 / 付款 / 交付
└─ 当前外部事实关键时才用 market-reality-researcher
↓
Opportunity 只做轻量 Trigger Scan；购买时机关键时才运行完整 Why-Now
↓
Stage-primary Thinking Lens + 最多一个必要的 Optional Lens
↓
Decision → Human Action / Artifact → Reality Feedback
↓
Diagnosis → Next Action / Stage rollback or promotion
```

原则是 `Case First → Pattern First → Replication First`：优先重建已经发生过的交易结构，区分精确案例与相邻案例，再测试当前用户能否复制；不是看到一个趋势就凭空发明复杂产品。

Opportunity Discovery 先区分两件事：Reality/Opportunity Evidence 回答“现实里为什么值得调查”，Investigation Advantage 回答“为什么你能更快、更便宜地学到答案”。Founder Fit、熟悉度和可达性仍然重要，但不会被加进同一个分数来替代交易、持续消费、现有支出、workaround 或其他市场信号。模型提出的新方向可以做有上限的探索，但会保持 `model-derived`、`unvalidated`，不会因为行动计划具体就变成第一市场方向。

比较方向前，Harness 还会先确认它们是不是同一层：H3 可能是工具或内容题目，漫剧是内容形式，小红书是渠道，带货则可能包含商业或变现机制，不能直接排成一张“赚钱方向”榜。用户问如何赚钱时，Runtime 优先比较现实中可观察的赚钱结构——谁获得什么重复价值、谁为哪个结果付钱、钱通过什么机制进入——再把工具、题目、形式和渠道映射为结构中的部件。用户说“可能适合自媒体”仍是可挑战的假设；只有“未来半年只做内容”这类明确承诺才成为当前约束。

实验也不再以“最容易做”为目标。Runtime 先判断哪个安全实验单位总成本能提供最多的决策信息，再在合格方案中选更小的；Founder attention 和放弃其他机会的成本同样计入。赚钱目标下，数小时、多天、多次正式发布或明显人工交付的 Material Experiment 必须说明成功和失败会改变什么、减少哪个 Money-path unknown，以及为什么比更小替代更有信息价值。30～90 分钟、单次、可逆的 Micro Probe 即使 Monetization Bridge 仍未知也可以执行，但只能支持窄的受众或价值判断。

Harness 也会保留业务原型。Content/Media 不会因为服务更容易报价就自动变成咨询或工具业务；Audience Value、Distribution 和 Money Flow 分开验证。小红书、B站、抖音、YouTube 等平台按当前问题既可能是 Distribution Channel，也可能是 Market Observation Environment，但互动量本身不证明利润或付款。

市场研究能证明别人是否在已知条件下做成过，不能单独证明你一定能做成。最终仍需要一个低成本、有停止条件的复现实验。

Market Reality Gate 不会为了展示能力反复搜索。只恢复项目、处理已有实验结果、确认执行细节，或已有研究仍新鲜且范围一致时，可以直接复用证据。新公开市场项目不会仅因“新”或“公开市场”就自动搜索；只有当前市场、政策、价格、案例等外部事实会改变下一步时，才做有决策、时间和停止条件的 bounded check。

### Agent Reach 与覆盖缺口

联网时优先检查 Agent Reach，并用 `agent-reach doctor --json` 的当次结果选择可用 backend；不可用的平台回退到 Codex 的 Web Search、网页读取或 Browser 能力。Agent Reach 是可选的获取层，不是研究方法，也不是结论来源；报告引用打开并核验的原始网页。

登录态平台只使用用户已经授权的会话。Harness 不自动安装、登录、读取或导出 Cookie，也不把 Cookie、Token 或凭据写入仓库。访问不到的平台会记录为 `coverage_gap`，不会声称做过“全网调查”。详细规则见 [`docs/integrations/agent-reach.md`](docs/integrations/agent-reach.md)。

原始网页和批量工具输出只临时放在 `/tmp`。Workspace 保存结构化的研究问题、来源 URL、日期、支持与反对证据、案例验证状态、结论和覆盖缺口，不保存整页 HTML、整篇文章或评论墙。

## Harness 会寻找“为什么现在买”

Harness 不只问“用户有没有痛点”，还会继续问：

- 什么具体事件会让用户现在开始找解决方案？
- 什么时候必须拿到结果，时间是谁定的？
- 不处理或晚处理会损失什么，谁承担损失？
- 承担后果的人是不是 Buyer、Payer 或预算影响者？
- 购买窗口有多长，你能不能在窗口内找到他？
- 紧急任务为什么敢交给你，有没有样片或小单这样的低信任入口？
- 这种情境会不会重复，交付失败的责任是否可承受？

这条完整链路叫 Buying Situation，会按 `BS001`、`BS002` 等稳定 ID 记录。比如同样是“做商品短视频”，618 前 7 天补 50 个 SKU、每批新品的多语言上线、素材衰退后 48 小时补片，是三个不同的购买情境，不能用一个抽象“商家有需求”代替。

高焦虑不等于高成交。Deadline 只有和真实后果、购买能力、可触达性、信任与交付能力结合时，才可能提高商业价值；虚假倒计时、假库存和假稀缺不会被当成需求证据，也不会被建议。反过来，没有 Deadline 的业务也不必被否定：高频使用、持续成本、便利、娱乐或稳定复购同样可能形成真实生意。

详细的 Purchase Trigger、Cost of Delay、Deadline 类型和 Why-Now Gate 见 [`docs/purchase-trigger-protocol.md`](docs/purchase-trigger-protocol.md)。

## 从判断到真人明天能执行

当下一条证据必须由真人观察、找人、联系、报价、收款、交付或运行一个小测试获得时，Runtime 会按 [`docs/human-execution-protocol.md`](docs/human-execution-protocol.md) 给出最小 Execution Packet。它不是 CRM 或固定销售漏斗，而是把“去验证”展开成：去哪找、搜什么、谁算合格、联系哪个角色、做多少、说什么或卖什么、真实价格、记录什么、何时停止和复盘。

低风险首次接触默认使用七项 Micro Packet，不展示一张空表。未知的来源、渠道、决策人或价格会保留为 `unknown`，先给一个有上限的获取步骤，不由模型猜。若暂缓开发，回答必须说明什么现实证据会解锁哪一小段技术工作；连续 `invalid` / `inconclusive` 的修复共享总时间、成本和复盘次数上限，达到上限就暂停、降级或换方向，而不是无限“再试一个渠道”。

实验完成后，Evidence Ledger 只记录当前测试用到的证据路径，并区分 `success`、严格的 `demand_failure`、`invalid` 和 `inconclusive`。无人看见、找错 Buyer 或价格未真正展示都不能证明需求失败；reason code 不能替代原始证据。详细对象协议见 [`docs/object-protocol.md`](docs/object-protocol.md#experiment)。

## Workspace 按真实经历生长

Stage 是状态，不是目录。目录存在只表示历史上确实产生过相关材料；Stage 目录不要求连续，也不允许为了结构完整而预建空目录。

```text
无 Project
↓ 对话形成值得持续追踪的方向
IDEA.md + STATE.md
↓ 真正记录 O001
01-opportunity/O001.md
↓ 真正形成 BS001（示例属于 business validation）
03-business-validation/buying-situations/BS001-….md
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
- 完成了一次有明确范围和来源的 Research，或重要外部证据变旧；
- 创建了对当前决策可复用的 Case；
- 形成了真实、决策相关的 Buying Situation，或它的 Trigger、Cost of Delay、信任、可触达性、状态发生实质变化；
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

Buying Situation 也按真实经历懒创建，不会给每个项目预建目录。详细记录放在所属 Stage 的 `buying-situations/BS001-….md`，项目根不会出现 `DEADLINE.md`、`URGENCY.md`、`HUMAN-NATURE.md` 或 `BUYING-SITUATIONS.md`。

第一次真实研究可能形成：

```text
workspace/project-a/
├── IDEA.md
├── STATE.md
└── 01-opportunity/
    ├── research/
    │   └── R001-market-reality-scan.md
    └── cases/
        └── C001-closest-precedent.md
```

`R001` 记录调查范围、实际访问渠道、Sources、支持和反面证据、政策、价格、判定、剩余未知量与重查条件。`C001` 只用于值得复用的案例重建，不为每个网页创建。存在真实研究时，`STATE.md` 才增加可选的 `market_evidence` 快照和最近研究链接。

不同问题使用不同证据：平台政策优先当前官方规则；市场存在优先可核验交易和持续运营；用户接受度优先购买、复购、退款或投诉行为；当前用户能否做成，最终优先其自己的付费复现实验。外部案例证明“某种模式曾存在”，不能替代真实交易。

## Stage

Stage 表示“当前最早且最重要的未解决 gate”，不是产品完成度，也不由目录是否存在决定。

| Stage | 当前主要问题 |
| --- | --- |
| `opportunity_discovery` | 哪个真实问题、交易、消费或重复价值模式值得调查？ |
| `problem_validation` | 该问题、期望价值或消费行为是否真实、重复且重要？ |
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

`market-reality-researcher` 也不是 Persona 或 Thinking Lens，而是一个 Evidence-Producing Skill。它发生在 Thinking 之前，负责拆解决策问题、寻找精确和相邻案例、负面证据、官方政策、用户行为、竞品价格，重建交易结构并检查可迁移性；它不占 1～2 个 Thinking Skill 配额。

研究型回答会把结论拆开表达，而不是只说“凭感觉可行”：

- 当前判断；
- 已被验证与尚未验证的部分；
- 最接近的成功模式及不能照抄的部分；
- 平台与合规约束；
- 反面证据；
- 当前最小复现实验；
- 已访问、未访问渠道和最新检查时间。

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

[`evals/cases/`](evals/cases/) 保存 43 个核心 Harness Behavior Acceptance Scenarios，用于修改 `AGENTS.md`、Skills、Router、Stage、Market Reality、Human Execution、Decision Frame 或 Experiment Diagnosis 规则时做人工行为回归。

它们不是自动启动 Codex 的 LLM Evaluation Framework，也不把手工编写的理想答案伪装成真实 Runtime 测试。核心覆盖：Project lifecycle、Stage-first、Reality Evidence 路由、过早开发、交易与 leverage、重大下注、Stage 回退、Workspace lazy growth、市场证据，以及无人看见、错误 Buyer、赞美无付款、友情付款、可执行 sourcing、研究/开发逃避、交付亏损、现实反馈改写方向、样本与 Decision Claim 的匹配、内容 Audience/Payer 分离、内容平台的条件式证据用途、执行具体性不抬升假设、跨层 Candidate 比较、Material Experiment 信息价值，以及用户偏好与明确约束的区别。

[`docs/evaluation-strategy.md`](docs/evaluation-strategy.md) 另定义同模型 `Baseline + Web` 与 `Harness + Web` 的人工 A/B 协议，用 outcome-first 的决策质量、次日可执行性、time-to-evidence/伤害作为主指标，并允许更简单、更聪明的 Baseline 合法获胜。仓库没有伪造任何 A/B 运行结果。

## 开发校验

维护本仓库本身时，可选运行：

```bash
python3 scripts/validate_repo.py
```

这是开发工具，不是使用 Harness 的前置步骤。它只检查可确定验证的内容，例如 Skill 结构、source provenance、链接、STATE 基本字段、Workspace lazy invariant、Market Reality 对象协议和 Eval case 结构；不执行网页研究，也不声称验证真实 Codex 推理质量。

## V0 边界

V0 没有 Web UI、API Server、数据库、向量数据库、RAG、自定义 Agent Loop、Agent 投票/辩论、自动登录/Cookie 管理、通用爬虫平台、消息队列或定时市场监控。Project discovery、bootstrap、resume、Stage/Reality Evidence 路由、条件式 Market Reality/Why-Now、Human Execution 和文件维护直接由 Codex Runtime 按仓库协议执行。
