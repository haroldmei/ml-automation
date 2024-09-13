performance vs availability
latency vs throughput - maximize throughput and appropriate latency

consistency - weak/strong/eventual/cap theorem
(voip, video chat, realtime multiplayer games etc are weak)
(dns, email are eventual; banking is strong)

availability - 
fail-over (master-slave, master-master, master-slave: loss of data before traffic switch, heartbeat is checked)
master-slave, hot/cold standby, traffic only to master
master-master, traffic to both

replicas - 
master-slave, master r/w, one or more slaves read only, replicates can happen from master to slaves, or from one slave to another
master-master, lb or app support to forward r/w, violating ACID as sync latency, *conflict resolution(changes happen in multi masters)

tradeoffs to consider
fail-over traffic loss
writes are replayed and may cause read replicas bogged down
the more replicas the more you need to sync
causing greater replication lag
* writing to the master causing multiple threads in parallel, whereas read replicas only support writing sequencially with a single thread

LB - 



