import time
import json
import random
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

##
##  IoT device simulation of a electronic bot to send sensor information
##

print("config vars")
# Configure Device
client_id = "WALL-E"
endpoint = "a33d9vvestebwe-ats.iot.us-east-1.amazonaws.com"
root_ca = r"C:\Users\bsolo\Downloads\Certs\wall-e\AmazonRootCA1.pem"
private_key = r"C:\Users\bsolo\Downloads\Certs\wall-e\private.pem.key"
certificate = r"C:\Users\bsolo\Downloads\Certs\wall-e\device-certificate.pem.crt"

print("init")
# Initialize the MQTT client
mqtt_client = AWSIoTMQTTClient(client_id)
mqtt_client.configureEndpoint(endpoint, 8883)
mqtt_client.configureCredentials(root_ca, private_key, certificate)

print("config")
# Configure MQTT client connection settings
mqtt_client.configureOfflinePublishQueueing(-1)  # Infinite offline publish queueing
mqtt_client.configureDrainingFrequency(2)  # Draining: 2 Hz
mqtt_client.configureConnectDisconnectTimeout(10)  # 10 sec
mqtt_client.configureMQTTOperationTimeout(5)  # 5 sec

print("connect")
# Connect to AWS IoT Core
mqtt_client.connect()


# Function to simulate sensor data
def generate_location_sensor_data():
    """
    This function requires no input and generates output for a Location Sensor

    This sensor would log the following details:
    Sample Time - The time the sensor captured the data.
    Device ID - The client id from the iot thing.
    Sensor - This is the 'Location' sensor.
    Direction - Logs a 360 deg directional heading.
    Forward Pitch - logs angle of incline or decline, plus or minus 20.0 deg from level.
    Side Pitch - logs the angle of pitch left to right, plus or minus 20.0 deg from level.

    Location is logged in current and target location by latitude and longitude.
    Curr Lat: Current Latitude in degrees ranging from -90 to +90
    Curr Long:  Current Longitude in degrees ranging from -180 to +180
    Target Lat: Target Latitude in degrees ranging from -90 to +90
    Target Long:  Target Longitude in degrees ranging from -180 to +180
    """

    # Create a list for direction in degrees from 0 to 359.
    dirrange = range(360)
    dirlist = list(dirrange)

    return {
        "sample_time": time.strftime("%Y-%m-%d %H:%M:%S") + f".{int(time.time() * 1000) % 1000:03d}",
        "device_id": client_id,
        "sensor": "Location",
        "direction": random.choice(dirlist),
        "forward_pitch": round(random.uniform(-20.0, 20.0), 2),
        "side_pitch": round(random.uniform(-20.0, 20.0), 2),
        "curr_lat": round(random.uniform(-90.0, 90.0), 2),
        "curr_long": round(random.uniform(-180.0, 180.0), 2),
        "target_lat": round(random.uniform(-90.0, 90.0), 2),
        "target_long": round(random.uniform(-180.0, 180.0), 2)
    }


# Function to simulate steering sensor data
def generate_steer_sensor_data():
    """
    This function requires no input and generates output for a Steering Sensor

    This sensor would log the following details:
    Sample Time - The time the sensor captured the data.
    Device ID - The client id from the iot thing.
    Sensor - This is the 'Steer' sensor.
    Servo Angle - Angle of the servo from neutral -45.0 to 45.0 degrees.
    Servo Current - Current from servo in Milliamps.
    Servo Voltage - Voltage from servo in Volts.
    """

    return {
        "sample_time": time.strftime("%Y-%m-%d %H:%M:%S") + f".{int(time.time() * 1000) % 1000:03d}",
        "device_id": client_id,
        "sensor": "Steer",
        "servo_angle": round(random.uniform(-45.0, 45.0), 2),
        "servo_current": round(random.uniform(0, 25), 2),
        "servo_voltage": round(random.uniform(0, 90), 2)
    }


# Function to simulate Drive Motor data
def generate_drive_motor_data():
    """
    This function requires no input and generates output for a Drive Motor Power Usage.

    This sensor would log the following details:
    Sample Time - The time the sensor captured the data.
    Device ID - The client id from the iot thing.
    Sensor - This is the Drive Motor sensor.
    RPM - Revolutions per Minute of Motor 0 to 3000.0 .
    Current - Current from Drive Motor in Amps.
    Voltage - Voltage from Drive Motor in Volts.
    Temperature - Drive Motor Temperature
    """

    return {
        "sample_time": time.strftime("%Y-%m-%d %H:%M:%S") + f".{int(time.time() * 1000) % 1000:03d}",
        "device_id": client_id,
        "sensor": "Drive",
        "rpm": round(random.uniform(0, 3000), 2),
        "current": round(random.uniform(0, 25), 2),
        "voltage": round(random.uniform(0, 180), 2),
        "temperature": round(random.uniform(0, 200), 2)
    }


# Function to simulate Battery data
def generate_battery_data():
    """
    This function requires no input and generates output for a Battery State.

    This sensor would log the following details:
    Sample Time - The time the sensor captured the data.
    Device ID - The client id from the iot thing.
    Sensor - This is the 'Battery' sensor.
    Current - Current from the Battery in Amps.  This can be Positive or Negative based on Charge/Discharge.
    Voltage - Voltage from the Battery in Volts.
    Temperature - Battery Temperature
    """

    return {
        "sample_time": time.strftime("%Y-%m-%d %H:%M:%S") + f".{int(time.time() * 1000) % 1000:03d}",
        "device_id": client_id,
        "sensor": "Battery",
        "current": round(random.uniform(-25, 25), 2),
        "voltage": round(random.uniform(0, 180), 2),
        "temperature": round(random.uniform(0, 200), 2)
    }


while True:
    # log Location Sensor data.
    topic = f"{client_id}/location"
    sensor_data = generate_location_sensor_data()
    message = json.dumps(sensor_data)
    mqtt_client.publish(topic, message, 1)
    print(f"Published: {message}")

    # log Steer Sensor data.
    topic = f"{client_id}/steer"
    sensor_data = generate_steer_sensor_data()
    message = json.dumps(sensor_data)
    mqtt_client.publish(topic, message, 1)
    print(f"Published: {message}")

    # log Steer Drive Motor data.
    topic = f"{client_id}/motor"
    sensor_data = generate_drive_motor_data()
    message = json.dumps(sensor_data)
    mqtt_client.publish(topic, message, 1)
    print(f"Published: {message}")

    # log Battery data.
    topic = f"{client_id}/battery"
    sensor_data = generate_battery_data()
    message = json.dumps(sensor_data)
    mqtt_client.publish(topic, message, 1)
    print(f"Published: {message}")

    time.sleep(5)  # Publish every 5 seconds
