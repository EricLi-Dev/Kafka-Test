from confluent_kafka import Producer
from faker import Faker
import json
import time
import logging
import random 

#Basic Logging Configuration
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='producer.log',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Initializing Faker
fake = Faker()

#Initializing Kafka Producer
producer = Producer({'bootstrap.servers':'localhost:9092'})
print('Kafka Producer has been initiated...')

#Defining message delivery callback function
def delivery_callback(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = 'Produced message on topic {} with value of {}\n'.format(msg.topic(), msg.value().decode('utf-8'))
        logger.info(message)
        print(message)

def main():
    for _ in range(10):
        data={
           'user_id': fake.random_int(min=20000, max=100000),
           'user_name':fake.name(),
           'user_address':fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
           'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
           'signup_at': str(fake.date_time_this_month())    
           }
        m=json.dumps(data)
        producer.poll(1)
        producer.produce('test-topic', m.encode('utf-8'),callback=delivery_callback)
        producer.flush()
        time.sleep(3)

main()
