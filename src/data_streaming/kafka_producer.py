from kafka import KafkaProducer
import json
import time
import pandas as pd

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_data(file_path, topic):
    data = pd.read_csv(file_path)
    for _, row in data.iterrows():
        message = row.to_dict()
        producer.send(topic, message)
        print(f"Sent: {message}")
        time.sleep(1)  # Simulate streaming

if __name__ == "__main__":
    send_data("data/cleaned_data/cleaned_orders.csv", "orders_topic")
    producer.close()
