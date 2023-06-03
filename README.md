# 0) Install requirements
- Node requirements
```
npm i
```
- Python requirements
```
conda env create -f environment.yml
```

# 1) Docker Container for Apache Kafka services
* docker-compose.yml 
- Zookeeper service 
- Broker service 

## start docker containers
```
docker-compose up
```

## create a Kafka topic in CLI
```
 docker exec -it kafka /opt/bitnami/kafka/bin/kafka-topics.sh \
      --create \
      --bootstrap-server localhost:9092 \
      --replication-factor 1 \
      --partitions 1 \
      --topic test-topic
```

# 2) node-rdkafka library for node.js
- https://github.com/Blizzard/node-rdkafka 
- Producer:
    Uses the Stream API of the node-rdkafka library to produce messages to the stream 
- Consumer:
    Uses the Standard API of the node-rdkafka library to consume messages on the stream,
    managing individual callbacks and events    

# 3) confluent-kafka library for python3
- https://github.com/confluentinc/confluent-kafka-python 
- https://github.com/joke2k/faker 
- Producer:
    Queues 10 Faker() objects to the stream, with a delivery callback function to manage failed and successful messages
- Consumer:
    Infinite loop to constantly poll the stream for messages

# Notes
- Can have a Kafka producer ran on Node.js and a receiving consumer running on python, language agnostic. 
- Consumers can be grouped by certain kafka topics. 
- Even if a consumer crashes, it can catch up on missed messages published to the stream by the producer. 

## Export conda environment requirements
```
conda env export | grep -v "^prefix: " > environment.yml
```
    
