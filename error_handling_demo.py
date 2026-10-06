sensor_readings = ["24.5", "28.1", "ERROR_SENSOR_5", "30.0", "NULL", "22.8"]

def process_reading(value):
    try:
        temp = float(value)
        print(f'Recorded temperature: {temp}')
    except ValueError:
        print(f"Alert: Skipped invalid sensor data -> {value}")

for sensor_reading in sensor_readings:
    process_reading(sensor_reading)
