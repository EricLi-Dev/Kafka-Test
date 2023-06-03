console.log("producer....");
import Kafka from 'node-rdkafka';

const stream = Kafka.Producer.createWriteStream({
    'metadata.broker.list': 'localhost:9092'
}, {}, {topic: 'test-topic'});

function queueMessage(){
    const result = stream.write(Buffer.from("hi"));
    if (result){
        console.log("wrote successfully");
    } else {
        console.log("wrote failed");
    }

}

setInterval(() => {
    queueMessage();
}, 3000)
