import paho.mqtt.client as mqtt
import time
import os
import csv

to_client = "123a"
to_server = "b123"

# 确保目录存在
os.makedirs('data', exist_ok=True)

# CSV 文件的路径
csv_file_path = 'data/electricity_consumption.csv'

# 如果文件不存在，创建文件并写入标题行
if not os.path.isfile(csv_file_path):
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Latitude", "Longitude", "Building_ID", "Datetime", "Category", "Weekday_Weekend", "Consumption"])

def on_message(client, userdata, msg):
    payload_string = str(msg.payload, encoding='utf8')
    print("Received (topic '" + msg.topic + "'): " + payload_string)

    # 解析数据并写入 CSV 文件
    data = payload_string.split(',')
    if len(data) == 7:  # 确保数据格式正确
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        print("Data saved to CSV:", data)
    else:
        print("Received malformed data:", payload_string)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2,"")
client.on_message = on_message

client.username_pw_set("team2", "qwertyuiop")
print("This runs a simple server to echo client string.")
client.connect("140.122.185.98", 1883, 60)
client.subscribe(to_server, 0)
client.loop_forever()
