
________________________________________________________________________________________________
|             |----DNS
| web browser |  
|             |--------- web server
| mobile app  | 

the primitive one



________________________________________________________________________________________________
| 
|             |----DNS
| web browser |  
|             |--------- web server --------- DB
| mobile app  | 

scale up: hardware limit, no failover and redundancy
scale out

2 tiers: web, data



_________________________web___tier___replicas__________________________________________________
| 
|             |----DNS
| web browser |  
|             |--------- load balancer --------- *web servers --------- DB
| mobile app  | 
|

scale web tier with replicas

1. web servers are in private network and hidden behind the load balancer and dns return lb ip
2. redundancy added and can be scaled out
3. stateful or stateless?



___________________________data__tier__replicas___________________________________________________
|
|             |----DNS                                                 |-------> *write DB
| web browser |                                                        |              |                 
|             |--------- load balancer --------- *web servers ---------|              | replication              
| mobile app  |                                                        |             \|/                 
|                                                                      |<-------- *read DB
|

scale data tier with replicas - performance, reliability, ha
consistency and availability
read/write ratio
conflict resolution
how: missing data when a master is down and a replica is promoted to master
data recovery scripts




___________________________cache__________________________________________________________
|
|             |----DNS                                     |-------------> *write DB
| web browser |                                            |                      |                 
|             |----- load balancer ----- *web servers -----|                      | replication              
| mobile app  |                                            |                     \|/                 
|                                                          |<---- cache <---- *read DB
|
cache strategies: read through (more...)
stale data, expiration choice
cache and db consistency (Scaling Memcache at Facebook, more...)
Single Point of Failure, multi cache across different data centers are recommended
Over provision of required memory
Eviction policy: LRU(least recently used), LFU(least frently used), FIFO




___________________________cdn__________________________________________________________
|
|                |----CDN                                     |-------------> *write DB
| web browser----|                                            |                      |                 
|                |----- load balancer ----- *web servers -----|                      | replication              
| mobile app ----|                                            |                     \|/                 
|                |----DNS                                     |<---- cache <---- *read DB
|
1. client A request image.png from CDN
2. if not in CDN, CDN server request it from web app
3. image.png returned from web app and stored in CDN server
4. CDN server return to client A
5. client B request image.png from CDN
6. CDN return image.png directly to client B




___________________________state__server__________________________________________________
|                                                                                            
|                |----CDN                                     |-------------> *write DB
| web browser----|                                            |                      |                 
|                |----- load balancer ----- *web servers -----|                      | replication              
| mobile app ----|                                 |          |                     \|/                 
|                |----DNS                          |          |<---- cache <---- *read DB
|                                                  |                                         
|                                              state server                                          


sticky sessions on lb
state server: NoSQL





___________________________multi__data__center________________________________________________
|                                                                                            
|                |----CDN                                      |-------------> *write DB
| web browser----|                                             |                      |                 
|                |----- load balancer |----- *web servers -----|                      | replication              
| mobile app ----|                    |             |          |                     \|/                 
|                |----DNS             |             |          |<---- cache <---- *read DB
|                                     |             |                                         
|                                     |             |                                      
|                                     |         state server
|                                     |             |
|                                     |             |
|                                     |             |           |-------------> *write DB
|                                     |             |           |                      |                 
|                                     | ----- *web servers -----|                      | replication              
|                                                               |                     \|/                 
|                                                               |<---- cache <---- *read DB
|                                                                                             

tech challenges
traffic redirection: GeoDNS
Data center synchronization (How netflix implementes asynchronous multi-data center replication. more...)
multi data center test and deployment


Ch4: Rate limiter
burst traffic and token bucket

algorithms: token bucket, leaking bucket, sliding window log, sliding window counter
architecture: multiple rate limiter with single data server, rules storage, cache
L7 limiter
L3 limiter with iptables

Design client to reduce the possibility to be rate limited
* use client cache to reduce api call
* do not send too many request
* gracefully recover from exceptions
* add sufficient back off time to retry


Ch5: Consistent hashing: minimal key redistribution, more even distribution(with virtual nodes)
hash ring for keys and servers, it's problems
represent a server with many virtual nodes


Ch6: Design Key-Value store
Redis can store 2**32 keys, 4 billion keys
distributed hash table, CAP theorem
System components
* data partition
* data replication
* consistency
* inconsistency resolution
* handling failures
* system architecture design
* write path
* read path


Ch7: ID generator
1. Multi-master: auto_increment feature in DB
2. UUID: 128bit number
3. Ticket server: centralized auto_increment server, data synchronization
4. Twitter Snowflake
Clock synchronization, NTP, Section length tuning(how to support low concurrency but long term applications?), HA

Ch8: URL shortener, generate short URL
* Step 1
1. create short url, redirect to original long url when click/input short url.
2. more then 100 million urls created a day.
3. (need to consider amount of redirect request?)
4. how long is the shortened url? what characters can be used?
5. can support customized url?
6. can shorted urls be deleted or updated?
7. what's the r/w ratio?

Back of envelop estimate
1. QPS - 100 million urls created per day, 4 million/hr, ~70k/m created, use up to 10 servers, each created 1.2k/s, can be handled by one web server, plus a slave for redundency.
2. QPS - Read/redirect: assume 10 times as much as write (test, normal access)
3. Storage - 100 million/day, 2 billions websites, in 6 yeas can create up to 200 billion urls. If each url is 100 bytes, total storage will be 20T
4. A normal Redis support 4 billion, 50 redis servers + redundency needed if use k-v memory storage; For each redis, 4G * 100 = 4T memory needed as url (over engineering?)

* Step 2
The API design
1. generate, post - input the original url, 
2. search, get - input the shortened url and check if exist
3. redirect, get - once the server receives the short url, it changes to the long url, with 301 redirect
4. 301 vs 302 - 301 means 'permanently' moved to the long url, so the client browser can cache the results and later request will no longer need to be sent to shortening server;
5. 302 means 'temporarily' moved, meaning the subsequent requests will be sent to shortening server again.
6. 301 is good for reducing server load, while 302 can be used for monitoring/analytics purposes
7. use hash tables to generate short urls

* Step 3, deep dive
1. data model (id, shortURL, longURL)
2. hash value length. hash value can be 0~9,a~z,A~Z total 62 chars. we need to have at least n chars such that 62**n > 200,000,000,000. n=7 is enough
3. hash+collision resolution, CRC32, MD5, SHA-1, causing too long hash value. iteratively append predefined string to long url and regenerate. expensive because it checks collision from db.
    bloom filters, a probabilistic technique to test if an element is a member of a set
4. base 62 conversion, from auto incremented id to base 62 representation, needs a unique id generator, no collision, easy to figure out the next short url
5. Arch:

| Browser ---- LB ==== Webservers ==== Caches, DBs
|                           ||                                                                      
|                           ||                                                                      
|                           ||                                                                      
|                           DBs                                                                       
|                                                                                                 

* Step 4, Wrap up
API design, data model, Hash, ID generator, URL shortening, URL redirectin


Ch8, web crawler


Ch9, push notification
3 types of notifications: mobile, sms, email

Step 1
1. app already contains channel data (email, mobile number or mobile app)? - contact gathering
2. app decide the content and initialize push
3. support opt out?
4. scale of system, 0.5 billion users
5. the latency 200 QPS enough?

6. real-time, soft real-time, user to receive asap but can be slightly delayed when system is overloaded.
7. the supported devices
8. what triggers notifications? client applications(they contact servers to push, or schedule, then the server does what is requested)
9. how many notifications to send on a daily basis - 10m


Step 2. HLD
Different type of notifications
IOS: provider - APNs - IOS
Android: provider - FCM (Firebase Cloud Messaging) - Android
SMS: provider - SMS(Twilio, Nexmo) - user
Email: provider - Email Serice(Sendgrid, Mailchimp) - user

Contact info gathering
Contact info: mobile device tokens, phone numbers, email addresses
1. user install or sign up
2. API server collect user contacts
|
| IOS
| Android   ------- LB  -------- Web Servers*    -------- DB*
| Laptop
|

info schema (one user multiple devices, denormalization/sync)
user_id, type, phone, email, device_token


Notification send/receive
|                                                                               
|                                                           APN      ---------- IOS                
| service 1                                                                              
|                                                           FCN      ---------- Android                    
| service 2                                                                              
|     .       =========== notification system  ==========   SMS      ---------- SMS                                                               
|     .                                                                          
|     .                                                     EmailService ---------- Email                     
| service N                                                                              
|                                                                               
|                                                                               
|                                                                               

Service 1 to N: triggers notification events. (why need N service?)

APNs/FCN/SMS/EmailService: consider extensibility, consider some service is not available in some areas(such FCM is not available in China, so need to think about other services: JPush, PushY)
challenges: SPOF, database scale, cache scale, performance bottleneck


Step 3. LLD
Notification servers, Cache, DB, message queue, workers, etc.
Notification Servers: 
API for services to send notifications. (API details?)
Basic validations to verify emails, phone numbers, etc.
Query the database or cache (user info/device info/notification template)
Put notificaiton to msg queue

CAP
Reliability: 
* data loss - persist notification data and retry.
* a recipient may receive dup notifications, need to reduce it. (some reasons that cause this to happen, such as retry an unfailed, network)
Notification templates, notification settings, rate limiting, retry mechanism, security, 
monitor queued notifications: monitor the number of queued notifications, if the number is large, means the notifications are not processed fast enough and more workers are needed.
events tracking: open rate, click and engagement. events to be tracked:
start, pending, sent, delivered, clicked, unscribed, error...

Step 4. Wrap


Ch11, News feed system
Facebook feeds, Twitter timeline, etc.

Users, News, Friendship
* Mobile App, Browser
* Number of friends a user can have - avg 5000

1. Show friends feeds chronologically
2. Contains text, video, image
3. Publish feeds, retrieve feeds
4. DAU: 10M, QPS: 200
5. Data storage, 10 years of data
6. Eventual consistency
7. 

hotkey problem
use graph database for friend relationship and friend recommendation

Post Service
Fanout service
Notification service
Feed retrieval service


Ch12, Chat system
Users, Messages, Channels, Friends
1. 1 to 1 or 1 to N
2. mobile app, browser
3. scale: 50m DAU
4. group member limit - 1000
5. type of contents - text only (no file attachment, no image or video)
6. message size limit: no more than 100k characters
7. end to end encryption required?
8. chat history storage. 5 years? (forever)
9. 


1. Notification
2. Content type
3. Client type: mobile app, browser
4. DAU and QPS
5. Storage
6. CAP
7. 

* Facebook messenger: 
one on one chat with low delivery latency, small group chat with max 100 people, online presence,
multiple device support, the same account can be logged into multiple device
push notifications


Step 2. HLD
Chat service - 
receive messages from clients, find the right recipients, forward messages to recipients
if a recipient is not online, hold that message on the server until she is online

protocols to be considered:
http and keep-alive, keep-alive header allows a client to maintain a persistent connection. 

sender side initiate a connect, but what about the receiver side?
server initiated connect? polling/long polling? web socket? 
polling: client periodically connect and ask the server, costly for servers
long polling: client hold the connect open, until there are actually new messages, or a timeout reached.
websocket: efficient connection management is critical on the server side.

Services:
stateless services - service discovery, auth service, group management, profile management
stateful service - chat service, presence service, each client maintains a persistent network connection to a chat service, (how it is integrated with service discovery?)
thirdparty integration: push notification is the most important.

1M concurrent users, each connection needs 10k memory, 10G memory to hold all connections?

Long tail data

How to generate message ID. auto_increment in MySQL, however NoSQL normally have no such support. Or use 64bit id generator like snowflake used in Twitter.
local sequence id generator, meaning only unique within a group. 


Step 3. LLD
Service discovery: to recommend the best chat server for a client, based on geographical location, server capacity, etc. 
Apache zookeeper, registers all chat servers, picks the best chat server. the choose of a chat server is after user authentication.

User presence service: when to change user status - user login, user logout, user disconnection, heartbeat
Online status fanout: each friend pair maintains a channel, 



Ch13, Search Autocomplete System


Ch14, Youtube


Ch15, Google Drive


Ch16, 

