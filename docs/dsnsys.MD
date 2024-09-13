I/O multiplexing
Apache and DoS attacks
Servers could not handle 10K concurrent connections because of O(n^2) algorithms used in the kernel.

Client ---- LoadBalancer --- WebServer --- ReaderAPI --- ReaderDB*
   |                             |           |
   |                             |           |
   DNS                           |         MemCache
                                 |
                               WriterAPI
                                 |
                                 |
                                Queue --- WorkerAPI --- WriterDB*
                                             |
                                             |
                                            NoSQL


CDN
Queue

DB*
DB Write Master/Slave
DB Read Replicas
NoSQL

API*
Worker API
Writer API
Reader API

Sharding
Federation

DNS: CloudFlare, Route 53

LoadBalancer: HAProxy, NGINX; 
SSL termination, remove the need to install X.509 certificates on each server
Session persistence, issue cookies and route specific client to the same server
L4 load balancing: look at IP+port, perform NAT
L7 load balancing: 

Reverse Proxy: HAProxy, Nginx; overlapping features with LB
SSL termination, hide servers, compression/caching/static content

Micro Service. Pintrest services: profile, follower, feed, search, upload, etc

Service discovery, Zookeeper - find services by name, address, ports

Worker: create and destroy, or in RAM

Consistency: weak/eventual/strong consistency

RDBMS: ACID - Atomicity, Consistency, Isolation, Durability

Federation (functional partitioning)
Instead of a single DB, could have multiple DBs for: Forums, Users, Products, etc.
* huge functions/tables
* Application logic support needed
* Joining tables is complex

Sharding: seperate the table and store in different DB. As the number of rows grow, more shards are added. 
with replicas of each shard, when one db is down, the traffic can be sent to it's replica db.
No central master node, so writes can be parallel, increase throughputs.
* application logic need to be updated
* Data distribution can become lobsided in a shard, causing shard to be heavy on load
* Joining data from multiple shards is complex
* 

Denormalization: 
Database Normalizaton: 1NF, 2NF, Boyce NF, etc.
* unique rows
* scalar columns
* attributes depend on the whole of every key
* attributes depend ONLY on primary key
Postgres and Oracle's materialized views can store redundant information and keep redundant copies consistent.
Read/Write ratio is normally big, such as 100/1 or 1000/1. join on read can be very expensive and cause significant amount of disk ops.
* Data duplicated
* Constraints can help redundant copies stays in sync which increases complexity
* Denormalized DB under heavy write load might perform worse then normalized DB.
( Tradeoff between write/read and normalized/denormalized )

SQL tuning
benchmark with tools such as ab
profile with tools: slow query log

tightening schema
VARCHAR -> CHAR
TEXT: storing a pointer on disk that is used to locate the text block
Avoid storing large BLOBS, store the location of these objects instead
Set NOT NULL to improve search performance

Index
faster query and aggregation
logarithmic complexity
index requires keep data in memory, require more space
writes could be slower since index needs to be updated
when loading large amounts of data, it might be faster to disable indices, then load the data, then rebuild the indices.

NoSQL: 
Google BigTable, HBase, 
Amazon Dynamo, Cassandra, 
Redis
MongoDB, CouchDB

Consistent hashing


Cache and CDN added
_____________________________________________________________________________________
|                                                                                              
|              |------DNS                              |------------> Write DB *                                                   
|   Browser  --|                                       |                 |                                              
|              |--------------LB---|---Web Servers* ---|                 | Syncing                                                   
|   MobileApp--|                   |            \      |                \|/                                              
|              |------CDN          |             \     |<--- Cache ----- Read DB  *                                                 
|                                  |              \                                                   
|                                  |               \                                                         
|                                  |                |---State Server (Shared session data)                                                  
|                                  |               /                                                 
|                                  |              /                                                   
|                                  |             /     |------------> Write DB *                                                   
|                                  |            /      |                 |                                              
|                                  |---Web Servers* ---|                 | Syncing                                                   
|                                           |          |                \|/                                              
|                                           |          |<--- Cache ----- Read DB  *                                                 
|                                           |                                                  
|                                           |                                                                   
|                                        MSG Queue  ------> Workers*                                                 
|                                                                                           
|                                                                                            
|                                                                                            
|
|
|
|
|

Sticky sessions from LB is not the answer. The solution is stateless sessions
Replicate data across multiple data centers

Logging/Monitoring/Debugging
Metrics: CPU/Memory/DiskIO, etc
Aggregations: for example, total DB performance, cache performance, etc.
Key business metrics: BAU daily visit, visitor retention, visitor spend, etc.
Automation: CI/CD

Database scaling
Sharding - separate the data into chunks and store multiple replicas each
Sharding key (partition key)
Resharding data, celebrity problem (hotspot key problem), Join and denormalization

Principles:
1. Stateless design
2. CAP choice
3. Cache and CDN to improve performance
4. Replicas for each tier
5. Data Sharding
6. Multiple Data Centers
7. Monitoring and Automation


Latency numbers
L1 cache
Branch mispredict
L2 cache

Mutex Lock/Unlock
Main memory reference

Compress 1K bytes with Zippy: 10 um
Send 2K bytes over 1 Gbps network: 20 um

Read 1MB sequentially from RAM: 250 um
Round trip within the same data center

Disk seek: 10ms
Read 1MB seq from network: 10ms
Read 1MB seq from disk: 30ms
Send packet from CA to Netherland round trip: 150ms


QPS and storage est.
300,000,000 monthly active, 50% use daily; -- 150M daily use
2 posts daily -- 300M post daily, avg QPS: 300,000,000/(24*3600) ~= 3500, peak QPS: 3500*2=4000
10% contains media
post size:
post ID: 64bytes
post text: 140 bytes
media: 1M
daily average size: 1M * 30,000,000 = 30T daily;

stored 5 years: 30T * 365 * 5 = 55P
With replicas: 110P


Answer framework
* Red flags
* Ask good questions


1. Clarify problem, functional requirements, non functional requirements

number of users, number of users concurrently
read/write ratio
strong consistency or eventual consistency
technology stack, budget

(News feed, URL shortener, chat system,)
News feed: 
* features: post, friends' post retrieval, timeline, post contains text and media
* mobile or web or both, regional or global, auth
* number of users per day (DAU, daily active users), in total, concurrent size
* read/write ratio (indicate DB), fast response
* CAP choice
* 

2. Propose a high level design and get buy-in

Concurrency anecadotes:
By year 2010, 
* WhatsApp, 24 cores, using Erlang on FreeBSD, handling 2M connections
* MigratoryData, 12 cores, using Java on Linux, handling 10M-12M connections

The Secret to 10 Million Concurrent Connections -The Kernel is the Problem, Not the Solution

* mobileApp, browser -- LB -- Web Servers -- Read/Write DB, Session DB
* MISC: CDN, Cache, MSG Queue
* Back of envelop EST. (10M DAU)
  QPS and Storage
  Number of servers based on No. of concurrency


3. Deep dive into design


4. Wrap up
* Identify bottlenecks
* Give recap of the design
* server failure, network loss, etc. are interesting to talk about.
* if your current design supports 1 million users, what changes do you need to make to support 10 million users?
* Propose other refinements you need if you had more time.

* +++ NEVER GIVE UP +++

Don't:
Don't be unprepared for typical questions
Don't jump into solutions without clarifying
Don't go into too much details on a single component
Don't hesitate to ask for hints
Don't think in silence
Don't think interview is done once you give the design

Time allocation:
Step 1, requirement clarification: 5min
Step 2, HLD: 20min
Step 3, LLD: 25min
Step 4, Wrap: 10


Rate limiter
Clarifications
Functional
1. Limit the speed of requests coming from a user or a node or a network?
2. Requests throttled need to be notified? 
3. Support configuration? Such as number of requests per minute, or per request cooling off period?

Non-functional
1. Client side or Server side?
2. Concurrent users, DAU
3. CAP choice

HLD

LLD



Key-Value store 
quorum consensus
W,R,N
W: A write of quorum W must be acknowledged from W replicas
R: A read quorum of size R means the read needs to be ACK for R times
if W+R>N, strong consistency is guarrenteed

Consistency models: Strong/Weak/Eventual

Inconsistency resolution: versioning and vector clock
vector clock: a (server, version) pair associated with a data item

Detect failures: gossip protocol
* each node maintains a list of node membership which contains id and heartbeat counters
* periodically increment heartbeat counter
* each node periodically sends heartbeats to a set of random nodes, which in turn propogate to another set of nodes
* once nodes receive heartbeats, membership list is updated to the latest info
* if heartbeat has not increased for more than predefined periods, the member is considered as offline.

hinted handoff: handle temp failures
use anti-entropy protocol to keep replicas in sync
a merkle tree is used for inconsistency detection and minimizing the amount of data transferred.
|                                    n1 ----------- n2                
|                                   /                 \
|                                  /                   \
|                                 /                     \
|                                /                       \
|         -------------  coordinator                     n3     
|                                \                       /
|                                 \                     /  
|                                  \                   /                                         
|                                   \                 /                                          
|                                    n5 ----------- n6                                                         

APIs: get, put
a coordinator (can be dynamically chosen, if one fails, choose a different one)
Nodes are distributed on a ring
dicentralized
data replicated on multiple nodes

node responsibilities:
1. Client API
2. Failure detection
3. Replication
4. Conflict resolution
5. Failure restoration
6. Storage

SSTable: stored-string table
Write steps: 1. logging; 2. cache to memory; 3. write to SSTable if memory full
Read steps: 1. return from memory; 2. if data not in memory, Bloom filter to choose an SSTable, 3. Read from SSTable to memory; 4. return data


Goals/topics
* store big data - partition - consistent hashing
* high availability - replication - sync, conflict resolution, vector clock, versioning, 
* scalability - 
* consistency - tunable consistency, quorum consensus
* temporary failures - sloppy quorum, hinted handoff
* permanent failures - merkle tree/hash tree
* data center outage - cross data center replication
* monitor, log


Unique ID generator

functional:
1. generate id
2. store the id
3. retrieve id
4. id unique and sortable
5. id incrementality
6. do ids only contain numericals?
7. do ids have lenth limit? varying lengths?

non-functional:
1. big data?
2. DAU?
3. concurrency? how many IDs can be generated in a second?
4. 

HLD
1. multi-master replication: databases' auto_increment feature
    hard to scale in multiple data centers
    ids do not go up with time across multiple servers
    it does not scale well when a server is added or removed

2. UUID
    Easy, scale, but: too long, ids do not go up with time, and could be non numeric
  
3. Ticket server (Flicker developed ticket servers)
    use a centralized auto_increment feature
    Numeric IDs, easy to implement and works for small to medium scale apps
    but: SPOF, 

4. Twitter snowflake



1. For a Read-Heavy System - Consider using a Cache. 
2. For a Write-Heavy System - Use Message Queues for async processing 
3. For a Low Latency Requirement - Consider using a Cache and CDN. 
4. Need 𝐀tomicity, 𝐂onsistency, 𝐈solation, 𝐃urability Compliant DB - Go for RDBMS/SQL Database. 
5. Have unstructured data - Go for NoSQL Database. 
6. Have Complex Data (Videos, Images, Files) - Go for Blob/Object storage. 
7. Complex Pre-computation - Use Message Queue & Cache. 
8. High-Volume Data Search - Consider search index, tries or search engine. 
9. Scaling SQL Database - Implement Database Sharding. 
10. High Availability, Performance, & Throughput - Use a Load Balancer. 
11. Global Data Delivery - Consider using a CDN. 
12. Graph Data (data with nodes, edges, and relationships) - Utilize Graph Database. 
13. Scaling Various Components - Implement Horizontal Scaling. 
14. High-Performing Database Queries - Use Database Indexes. 
15. Bulk Job Processing - Consider Batch Processing & Message Queues. 
16. Server Load Management & Preventing DOS Attacks- Use a Rate Limiter. 
17. Microservices Architecture - Use an API Gateway. 
18. For Single Point of Failure - Implement Redundancy. 
19. For Fault-Tolerance and Durability - Implement Data Replication. 
20. For User-to-User fast communication - Use Websockets. 
21. Failure Detection in Distributed Systems - Implement a Heartbeat. 
22. Data Integrity - Use Checksum Algorithm. 
23. Efficient Server Scaling - Implement Consistent Hashing. 
24. Decentralized Data Transfer - Consider Gossip Protocol. 
25. Location-Based Functionality - Use Quadtree, Geohash, etc. 
26. Avoid Specific Technology Names - Use generic terms. 
27. High Availability and Consistency Trade-Off - Eventual Consistency. 
28. For IP resolution & Domain Name Query - Mention DNS (Domain Name System). 
29. Handling Large Data in Network Requests - Implement Pagination. 
30. Cache Eviction Policy - Preferred is LRU (Least Recently Used) Cache.