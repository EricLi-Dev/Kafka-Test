from confluent_kafka import Consumer

#Initializing Kafka Consumer
consumer=Consumer({'bootstrap.servers':'localhost:9092','group.id':'python-consumer','auto.offset.reset':'earliest'})
print('Kafka Consumer has been initiated...')

#Subscribe consumer to a topic
print('Available topics to consume: ', consumer.list_topics().topics)
consumer.subscribe(['test-topic'])

#Consumer inifinite loop to poll for messages
def main():
    while True:
        msg=consumer.poll(1.0) #timeout
        if msg is None:
            continue
        if msg.error():
            print('Error: {}'.format(msg.error()))
            continue
        data=msg.value().decode('utf-8')
        print(data)
    consumer.close()

main()
