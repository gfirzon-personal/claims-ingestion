import json
import time
from confluent_kafka import Producer

### If Kafka is running inside Docker but your script is running outside, 
# replace localhost with the correct host (host.docker.internal or the container IP).


# Kafka broker configuration
#KAFKA_BROKER = "localhost:9092"
KAFKA_BROKER = "kafka:9092"
#KAFKA_BROKER = "172.17.0.2:9092"
KAFKA_TOPIC = "test_topic"

# Kafka Producer Configuration
producer_conf = {
    "bootstrap.servers": KAFKA_BROKER,
    "client.id": "python-producer"
}

# Create Kafka Producer
producer = Producer(producer_conf)

def acked(err, msg):
    """Delivery callback for message acknowledgment"""
    if err:
        print(f"Message failed delivery: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Function to produce messages
def produce_messages():
    for i in range(10):
        key = f"key-{i}"
        value = json.dumps({"index": i, "message": f"Hello Kafka {i}"})

        # Send message
        producer.produce(KAFKA_TOPIC, key=key, value=value, callback=acked)
        producer.poll(0)  # Serve delivery callback events

        print(f"Produced message {i}")
        time.sleep(1)  # Simulate real-time event generation

    producer.flush()  # Ensure all messages are delivered

if __name__ == "__main__":
    produce_messages()
