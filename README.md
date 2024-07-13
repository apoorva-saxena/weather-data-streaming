# Weather Data Streaming with Kafka

This project demonstrates a simple weather data streaming application using Apache Kafka. It consists of a producer that generates simulated weather data and a consumer that processes this data in real-time.

## Project Overview

The application is split into two main components:
1. A weather data producer
2. A weather data consumer

The producer generates random weather data for various cities and sends it to a Kafka topic. The consumer reads from this topic and processes the data, generating alerts for extreme temperatures.

## Prerequisites

- Docker and Docker Compose
- Python 3.7+
- pip (Python package manager)

## Setup

1. Clone this repository:
2. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
3.  Start Kafka using Docker compose:
    ```
    docker-compose up -d
    ```
## Running the Application

1. In one terminal, start the producer:
    ```
    python weather_producer.py
    ```    
2. In another terminal, start the consumer:
    ```
    python weather_consumer.py
    ```
## Project Structure

- `docker-compose.yml`: Docker Compose file for setting up Kafka and Zookeeper
- `weather_producer.py`: Script that generates and sends weather data to Kafka
- `weather_consumer.py`: Script that consumes and processes weather data from Kafka
- `requirements.txt`: List of Python dependencies

## How It Works

1. The producer generates random weather data for a list of cities every 2 seconds.
2. This data is sent to a Kafka topic named 'weather_topic'.
3. The consumer subscribes to 'weather_topic' and reads the incoming data.
4. If the temperature is above 35°C or below 0°C, the consumer prints an alert.

## Customization

You can modify the list of cities, temperature ranges, and alert conditions in the respective Python scripts to suit your needs.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
