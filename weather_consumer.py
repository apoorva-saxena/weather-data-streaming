import json
from kafka import KafkaConsumer

# Create a Kafka consumer
consumer = KafkaConsumer('weather_topic',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# Main loop to consume weather data
for message in consumer:
    weather_data = message.value
    print(f"Received: {weather_data}")
    
    # Process the data (in this example, we'll just check for extreme temperatures)
    if weather_data['temperature'] > 35:
        print(f"ALERT: High temperature in {weather_data['city']}!")
    elif weather_data['temperature'] < 0:
        print(f"ALERT: Freezing temperature in {weather_data['city']}!")