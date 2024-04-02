import random
import time
import logging

# Set up logging configuration
logging.basicConfig(filename='warehouse_iot_logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define the sensors and their properties
sensors = [
    {"name": "Temperature Sensor", "unit": "°C", "min_value": 20, "max_value": 25},
    {"name": "Humidity Sensor", "unit": "%", "min_value": 40, "max_value": 60},
    {"name": "Motion Sensor", "unit": None, "events": ["Motion detected", "No motion detected"]},
    {"name": "Light Sensor", "unit": "lux", "min_value": 500, "max_value": 1000},
    {"name": "Door Sensor", "unit": None, "events": ["Door opened", "Door closed"]},
    {"name": "Pressure Sensor", "unit": "hPa", "min_value": 1000, "max_value": 1010},
    {"name": "Proximity Sensor", "unit": None, "events": ["Object detected", "No object detected"]},
    {"name": "Gas Sensor", "unit": "%", "min_value": 0.01, "max_value": 0.05},
    {"name": "Power Meter", "unit": "Watts", "min_value": 1000, "max_value": 2000}
]

# Function to generate random sensor data
def generate_sensor_data(sensor):
    if "events" in sensor:
        return random.choice(sensor["events"])
    else:
        return round(random.uniform(sensor["min_value"], sensor["max_value"]), 2)

# Main function to generate logs
def generate_logs(num_logs):
    for _ in range(num_logs):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        for sensor in sensors:
            data = generate_sensor_data(sensor)
            log_message = f"{timestamp} - {sensor['name']} - {data}"
            if "unit" in sensor:
                log_message += f" {sensor['unit']}"
            logging.info(log_message)
        time.sleep(5)  # Pause for 5 seconds between logs

# Generate 100 logs
generate_logs(100)
