import json
import time
from kafka import KafkaProducer
from datetime import datetime
import random

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                value_serializer=lambda v: json.dumps(v).encode('utf-8'))

cities = ['New York', 'London', 'Tokyo', 'Sydney', 'Rio de Janeiro']

# generates weather data
def generate_weather():
    city = random.choice(cities)
    temperature = round(random.uniform(-10, 40), 1)
    humidity = random.randint(0, 100)
    timestamp = datetime.now().isoformat()
    
    return {
        'city': city,
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': timestamp
    }

while True:
    weather_data = generate_weather()
    producer.send('weather_topic', weather_data)
    print(f"Produced: {weather_data}")
    time.sleep(2)