myPara = """
- name: "ABC_NOTIFY_QUEUE"
    partitions: 10
    partition_count: 
    replication_factor: 3
    insync.replicas: 2
    io.threads: 8
    network.threads: 5
    replica.fetchers: 2
    config_overrides:
      - cleanup.policy=delete
      - retention.ms=24HR
      - max.message.bytes=30485760
      - replica.lag.time.max.ms=30000
      - socket.receive.buffer.bytes=102400
      - socket.request.max.bytes=104857600
      - socket.send.buffer.bytes=102400
      - unclean.leader.election.enable=true
      - zookeeper.session.timeout.ms=18000
"""

list1 = ["XYZ", "ABC"]

for i in list1:
    modifiedPara = myPara.replace("ABC_NOTIFY_QUEUE",i)
    print(modifiedPara)

# print(myPara)