import time
import requests
import json


with open("config.json") as config_file:
    json_data = json.load(config_file)

ip = json_data["server_ip"]

counter = 0
while True:
    #counter = counter + 1
    #with open("tempData.txt", "w") as file:
    #    file.write(f"{counter}")
    #    print(counter)

    data = f"2022.12.30 08:33:28 TEMPERATUR2 off 0 19.4 19.7"
    response = requests.post(f"http://{ip}:5000/message", data=data)
    print(response.text)

    time.sleep(1)
