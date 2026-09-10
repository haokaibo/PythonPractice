# 系统设计练习题：设计一个类 Microsoft Teams 的聊天系统
# System Design Practice: Design a Chat System Like Microsoft Teams

> 这是一道典型的 HLD（高层设计）题，面试官通常会先给一个模糊的题目，然后靠你主动提问来收窄范围。下面按真实面试的节奏来走：先给题目，再给一份参考答案（但记住——设计题没有唯一标准答案，面试官更看重你的思考过程和权衡取舍，而不是你是否背下了某个方案）。
>
> This is a classic HLD (high-level design) question. Interviewers usually start with a vague prompt and expect you to narrow the scope through clarifying questions. Below follows the pacing of a real interview: the question first, then a reference answer — but keep in mind there's no single "correct" answer to a design question. Interviewers care more about your reasoning and trade-offs than whether you recite a memorized solution.

---

## 第一步：题目（面试官通常只会说这一句）
## Step 1: The prompt (usually just one sentence)

> "设计一个类似 Microsoft Teams 的聊天系统，支持一对一和群组消息。"
>
> "Design a chat system like Microsoft Teams that supports both one-on-one and group messaging."

面试官期待你先反问几个澄清问题，而不是立刻开始画图。这一步本身就是考察点之一。

The interviewer expects you to ask clarifying questions first, rather than jumping straight into drawing diagrams. This step itself is part of what's being evaluated.

---

## 第二步：你应该主动问的澄清问题
## Step 2: Clarifying questions you should proactively ask

- 需要支持哪些功能？只是文字消息，还是也要图片/文件、已读回执、正在输入提示？
  What features are in scope — just text, or also images/files, read receipts, typing indicators?
- 规模量级：日活用户数（DAU）大概多少？高峰期并发在线人数？
  What's the scale — roughly how many DAU (daily active users)? Peak concurrent online users?
- 消息是否需要保证送达顺序？是否需要"精确送达一次"（exactly-once）？
  Do messages need guaranteed ordering? Do we need exactly-once delivery?
- 离线用户的消息怎么处理？需不需要推送通知？
  How are messages handled for offline users? Do we need push notifications?
- 是否需要支持多端同步（同一账号同时登录手机和电脑）？
  Do we need multi-device sync (same account logged in on phone and desktop at once)?
- 消息历史需要保留多久？是否要支持全文搜索？
  How long is message history retained? Do we need full-text search?

**假设面试官给的范围**（这是本答案采用的假设，实际面试中要根据面试官的回答调整）：
**Assumed scope given by the interviewer** (this is the assumption this answer runs with — adjust based on what your actual interviewer says):

- 支持 1:1 和最多 100 人的群组文字消息
  Support 1:1 and group text messaging for groups up to 100 people
- DAU 5000 万，高峰并发在线 500 万
  50 million DAU, 5 million peak concurrent online users
- 需要消息送达、已读回执、在线状态（presence）
  Need message delivery, read receipts, and presence (online status)
- 离线消息需要缓存，用户上线后拉取
  Offline messages need to be cached and fetched once the user comes back online
- 不要求端到端加密（简化范围，除非面试官特别要求）
  End-to-end encryption is out of scope (to simplify, unless the interviewer asks for it)

---

## 第三步：容量估算（Back-of-envelope）
## Step 3: Capacity estimation (back-of-envelope)

- 5000 万 DAU，假设人均每天发 40 条消息 → 20 亿条消息/天
  50M DAU, assume 40 messages/user/day → 2 billion messages/day
- 平均每秒消息数 = 20亿 / 86400 ≈ **23,000 条/秒**（平均），高峰按 5 倍算 ≈ **115,000 条/秒**
  Average messages/sec = 2B / 86,400 ≈ **23,000 msg/s** (average); at 5x peak load ≈ **115,000 msg/s**
- 假设每条消息平均 200 字节（含元数据）→ 20亿 × 200B ≈ 400GB/天的写入量
  Assuming ~200 bytes per message (including metadata) → 2B × 200B ≈ 400GB/day of write volume
- 消息保留 2 年 → 存储总量约 292TB（不含索引和副本）
  Retaining messages for 2 years → roughly 292TB total storage (excluding indexes and replicas)

这一步不用算得多精确，面试官想看的是你有没有"用数字驱动设计决策"的习惯——比如存储量级会直接影响你选数据库分片策略。

The math doesn't need to be exact here. What the interviewer wants to see is whether you have the habit of letting numbers drive design decisions — for example, storage scale directly informs your database sharding strategy.

---

## 第四步：高层架构（HLD）
## Step 4: High-level architecture (HLD)

```
客户端(Web/桌面/移动) Client (Web/Desktop/Mobile)
      │  (WebSocket 长连接 + HTTPS API / WebSocket persistent connection + HTTPS API)
      ▼
   API 网关 / 负载均衡  API Gateway / Load Balancer
      │
 ┌────┴─────┬──────────┬─────────────┬──────────────┐
 ▼          ▼          ▼             ▼              ▼
连接服务   聊天服务    在线状态服务   通知服务       用户/群组服务
Connection  Chat       Presence      Notification   User/Group
Gateway     Service    Service       Service        Service
      │          │             │              │              │
      └────┬─────┴──────┬──────┴──────┬───────┴──────┬───────┘
           ▼             ▼             ▼              ▼
      消息队列        消息数据库      Redis缓存      推送网关
      Message         Message DB     Redis Cache    Push Gateway
      Queue           (Cosmos DB,    (presence,     (APNs/FCM)
      (Event Hub/      sharded)      session
       Kafka)                        cache)
```

### 核心组件职责
### Core component responsibilities

**连接网关（Connection Gateway）**
**Connection Gateway**

维护客户端的长连接（WebSocket）。因为单机能维持的长连接数有限（通常几万到十几万），这一层需要水平扩展，并且要有一个"连接路由表"记录"用户当前连在哪台网关机器上"——这张表通常放 Redis，因为需要极低延迟的读写。

Maintains the client's persistent WebSocket connection. Since a single machine can only hold a limited number of long-lived connections (typically tens of thousands to a few hundred thousand), this layer needs to scale horizontally, and requires a "connection routing table" tracking which gateway machine each user is currently connected to — this table typically lives in Redis, since it needs extremely low-latency reads and writes.

**聊天服务（Chat Service）**
**Chat Service**

无状态服务，负责：接收消息、写入消息队列、写入数据库、路由给接收方所在的网关。设计成无状态是为了能随意水平扩容。

A stateless service responsible for: receiving messages, writing to the message queue, persisting to the database, and routing to the recipient's gateway. It's designed stateless so it can scale horizontally without constraint.

**在线状态服务（Presence Service）**
**Presence Service**

这是 Teams 这类产品的经典难点。核心思路：
This is a classic hard problem for products like Teams. The core approach:

- 客户端定期发心跳（比如每 30 秒），Presence 服务用 Redis 存 `user_id → last_heartbeat_time`，加一个 TTL（比如 60 秒），超时自动过期视为离线
  The client sends a periodic heartbeat (e.g. every 30 seconds); the Presence service stores `user_id → last_heartbeat_time` in Redis with a TTL (e.g. 60 seconds) — if it expires, the user is treated as offline.
- 状态变化通过 Pub/Sub（Redis Pub/Sub 或 Event Hub）广播给关心这个用户的其他客户端（比如同一个群组的成员）
  Status changes are broadcast via pub/sub (Redis Pub/Sub or Event Hub) to other clients that care about this user (e.g. fellow group members).
- 这里的权衡是"实时性 vs 系统压力"：心跳越频繁，状态越实时，但服务器压力越大——面试时要主动提这个 trade-off
  The trade-off here is real-time accuracy vs. system load: more frequent heartbeats mean more accurate status but more server load — bring this trade-off up proactively in the interview.

**消息队列（Event Hub / Kafka）**
**Message Queue (Event Hub / Kafka)**

消息先写队列再落库，是为了**削峰**和**解耦**：聊天服务不需要同步等数据库写完才返回，可以异步处理，扛住突发流量。同时下游的通知服务、搜索索引服务可以各自订阅同一个消息流，互不阻塞。

Messages are written to the queue before being persisted to the database, for **load-leveling** and **decoupling**: the chat service doesn't have to synchronously wait for the database write to finish before returning — it can process asynchronously and absorb traffic spikes. Meanwhile, downstream services (notifications, search indexing) can each subscribe to the same message stream independently without blocking each other.

**消息数据库（Cosmos DB，按会话分片）**
**Message Database (Cosmos DB, sharded by conversation)**

- 分区键（partition key）选 `conversation_id`，因为查询几乎总是"拉某个会话的消息列表"，这样同一个会话的消息在物理上聚在一起，查询效率高
  The partition key is `conversation_id`, since queries are almost always "fetch the message list for a given conversation" — keeping messages from the same conversation physically co-located makes reads efficient.
- 每条消息的 `message_id` 用类似 Snowflake 的算法生成，保证**递增有序**，这样不需要额外排序就能保证消息按时间顺序展示
  Each message's `message_id` is generated using a Snowflake-like algorithm, guaranteeing **monotonic ordering** — so messages display in chronological order without needing an extra sort step.

**通知服务（Notification Service）**
**Notification Service**

处理离线用户的消息。逻辑：聊天服务写完消息后，检查接收方是否在线（查 Presence）；如果离线，把消息塞进"待推送队列"，通知服务负责调用 APNs/FCM 推送手机通知，用户上线后再从数据库拉取未读消息。

Handles messages for offline users. Logic: after the chat service persists a message, it checks whether the recipient is online (via Presence); if offline, the message goes into a "pending push" queue, and the notification service calls APNs/FCM to push a mobile notification. The user fetches unread messages from the database once they come back online.

---

## 第五步：几个关键的深挖点（面试官大概率会追问）
## Step 5: Key follow-up questions (the interviewer will very likely dig into these)

### 1. 消息怎么保证送达顺序，又不重复？
### 1. How do you guarantee message ordering without duplicates?

- 顺序：同一个会话的消息，客户端和服务端都用**单调递增的消息 ID**（不是简单自增，用 Snowflake 类算法避免多机冲突）来排序，客户端按 ID 排序展示，不依赖到达时间
  Ordering: for messages within the same conversation, both client and server sort by a **monotonically increasing message ID** (not a naive auto-increment — use a Snowflake-style algorithm to avoid collisions across machines). The client displays messages sorted by ID, not by arrival time.
- 去重：客户端发消息时带一个幂等键（比如 UUID），服务端用这个键做去重（存一个短期的 Redis Set 或者靠数据库唯一索引），防止网络重试导致消息发两遍
  Deduplication: the client attaches an idempotency key (e.g. a UUID) when sending a message; the server deduplicates on this key (via a short-lived Redis Set or a database unique index), preventing network retries from sending the same message twice.

### 2. 群组消息怎么处理"扇出"问题？
### 2. How do you handle the "fan-out" problem for group messages?

群组人数从几个人到上百人不等，两种策略：
Group size ranges from a few people to a few hundred. Two strategies:

- **写扩散（Fan-out on write）**：消息到达时，立刻给群里每个成员的"收件箱"都写一份。适合小群（成员少，写入代价可控），读取快。
  **Fan-out on write**: when a message arrives, immediately write a copy into every member's "inbox." Good for small groups (write cost is manageable), and reads are fast.
- **读扩散（Fan-out on read）**：消息只存一份在会话里，用户拉取时再实时查询自己所在的会话列表。适合超大群（避免写放大），但读的时候要多查一次。
  **Fan-out on read**: the message is stored once, in the conversation; the user's client queries their conversation list live when fetching. Good for very large groups (avoids write amplification), but adds an extra query on read.
- Teams 场景下群组上限不算特别大（题目假设 100 人），写扩散是合理选择；如果是"上万人的频道"（类似 Slack workspace 广播），就要考虑读扩散或者混合方案。这个对比本身就是一个很好的面试加分点，主动提出来。
  In the Teams scenario the group cap isn't huge (100 people, per our assumption), so fan-out-on-write is a reasonable choice; for a "channel with tens of thousands of members" (like a Slack workspace broadcast), you'd want fan-out-on-read or a hybrid. Raising this comparison proactively is a strong interview signal.

### 3. 单点故障和弹性怎么设计？
### 3. How do you design for fault tolerance and eliminate single points of failure?

- 连接网关、聊天服务都做成无状态、多实例部署，前面挂负载均衡
  Connection gateways and the chat service are stateless, deployed as multiple instances behind a load balancer.
- 数据库和 Redis 都要有主从复制/多副本，跨可用区部署
  Databases and Redis need primary-replica replication / multiple copies, deployed across availability zones.
- 消息队列本身要能持久化，即使聊天服务重启，消息也不会丢
  The message queue itself must be persistent, so messages aren't lost even if the chat service restarts.
- 可以提一句"chaos engineering"——主动注入故障（比如随机杀掉一个服务实例），验证系统的自愈能力，这是 Azure/Teams 团队公开分享过的实践，提到会显得你做了功课
  Worth mentioning "chaos engineering" — proactively injecting failures (e.g. randomly killing a service instance) to verify the system's self-healing ability. This is a practice the Azure/Teams team has publicly discussed, and bringing it up signals you've done your homework.

### 4. 如何支持多端同步（同一账号手机+电脑同时在线）？
### 4. How do you support multi-device sync (same account online on phone and desktop simultaneously)?

- 连接路由表从 `user_id → 一台网关` 改成 `user_id → 网关列表`（一对多）
  The connection routing table changes from `user_id → one gateway` to `user_id → list of gateways` (one-to-many).
- 消息广播时，给这个用户名下所有在线的连接都推一份
  When broadcasting a message, push a copy to every online connection under that user.
- 已读回执要处理"哪个设备标记已读，其他设备也要同步已读状态"，这本质上是一个小型的状态同步问题，可以用类似"已读位点"（read cursor，记录这个用户在这个会话里读到了第几条消息）的方式解决，而不是给每条消息单独记录已读状态列表（那样存储和同步代价太高）。
  Read receipts need to handle "one device marks as read, other devices need to sync that state." This is essentially a small state-sync problem, solvable with something like a "read cursor" (recording which message ID this user has read up to in this conversation), rather than tracking a read-status list per individual message (which would be far too costly to store and sync).

---

## 第六步：总结陈述（面试收尾时可以这样说）
## Step 6: Closing summary (something you can say to wrap up the interview)

> "整体思路是：连接层用长连接网关做实时通信，中间用消息队列解耦和削峰，存储层按会话分片保证读写效率，在线状态用 Redis + TTL 心跳机制实现。核心的几个权衡是：群组消息的写扩散 vs 读扩散、心跳频率对实时性和系统压力的取舍，以及用消息 ID 而不是时间戳来保证顺序。如果往后进一步优化，可以考虑消息搜索单独做一套 ES 索引，或者引入 CRDT 处理多端并发编辑场景（比如消息编辑/撤回）。"
>
> "The overall approach: the connection layer uses persistent-connection gateways for real-time communication, a message queue in the middle decouples components and smooths out spikes, the storage layer shards by conversation for efficient reads and writes, and presence is implemented with Redis plus a TTL-based heartbeat. The key trade-offs are: fan-out-on-write vs. fan-out-on-read for group messages, heartbeat frequency vs. system load, and using message IDs rather than timestamps for ordering. Further down the line, you could consider a separate Elasticsearch index for message search, or introduce CRDTs to handle multi-device concurrent-edit scenarios like message editing or unsending."

这种收尾方式的作用是让面试官感觉你对整个设计"心里有一张完整地图"，而不是零散地回答了一堆子问题。

The point of a closing summary like this is to leave the interviewer with the impression that you hold a complete mental map of the design, rather than having answered a scattered set of sub-questions.

---

## 练习建议
## Practice suggestions

1. 先只看"第一步/第二步"，自己试着列出你会问的澄清问题，再对比上面的列表
   Read only Step 1/2 first, try listing your own clarifying questions, then compare against the list above.
2. 自己在纸上/白板上画一遍架构图，不要直接抄，画完再对照检查漏掉了哪块
   Draw the architecture diagram yourself on paper or a whiteboard — don't just copy it. Compare afterward to see what you missed.
3. 挑"第五步"里的 4 个追问点，自己先想 2 分钟再看答案——这是面试里最容易卡壳的地方，练的就是这个反应速度
   Pick the 4 follow-up questions in Step 5, think for 2 minutes on your own before checking the answer — this is where interviews most commonly stall, and this is exactly the reaction speed you're practicing.
