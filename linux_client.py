import paho.mqtt.client as mqtt
import ssl
import struct
import time
from datetime import datetime

to_client = "123a"
to_server = "b123"

def get_user_input():
    latitude = input("Enter Latitude: ")
    longitude = input("Enter Longitude: ")
    building_id = input("Enter Building ID: ")
    category = input("Enter Category: ")
    return latitude, longitude, building_id, category

def get_weekday_weekend():
    now = datetime.now()
    if now.weekday() < 5:
        return "Weekday"
    else:
        return "Weekend"

def get_power_consumption():
    try:
        output = subprocess.check_output(['powerstat', '-R', '1', '1'], text=True)
        lines = output.splitlines()
        for line in lines:
            if "W" in line and "Average" not in line:  # 查找包含功耗（瓦特）的行
                parts = line.split()
                return float(parts[-1].replace('W', ''))
        return None
    except Exception as e:
        print(f"Error fetching power consumption: {e}")
        return None

def on_connect(client, userdata, flags, rc, properties):
    print("Connected to the broker.")
    client.subscribe(to_client, 0)

def on_message(client, userdata, msg):
    print("Received (topic '" + msg.topic + "'): " + str(msg.payload, encoding='utf8'))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("team2", "qwertyuiop")
client.connect("140.122.185.98", 1883, 60)

client.loop_start()
time.sleep(1)
latitude, longitude, building_id, category = get_user_input()
time.sleep(1)

try:
    while True:
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        weekday_weekend = get_weekday_weekend()

        consumption = get_power_consumption()
        if consumption is None:
            print("Failed to retrieve power consumption data.")
        else:
            data = f"{latitude},{longitude},{building_id},{current_time},{category},{weekday_weekend},{consumption}"
            client.publish(to_server, data, 0)
            print("Sent to server:", data)

        time.sleep(60)  # 每隔60秒发送一次数据
except KeyboardInterrupt:
    print("Exiting program...")
    client.loop_stop()
    client.disconnect()