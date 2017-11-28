#import paho.mqtt.client as mqtt
import time
import os

import temp3 as temperature
import gyroscope as gyro
import connectArd as weight
import humidity as humi

hostname = "87.44.19.170"
temperatureQueue1 = "SmartHive/Temperature/Temp1"
temperatureQueue2 = "SmartHive/Temperature/Temp2"
humidityQueue = "SmartHive/Humidity"
weightQueue = "SmartHive/Weight"
gyroscopeQueueX = "SmartHive/Gyroscope/Axis-X"
gyroscopeQueueY = "SmartHive/Gyroscope/Axis-Y"
gyroscopeQueueZ = "SmartHive/Gyroscope/Axis-Z"

try:
        print("Starting mqtt publishing")

        while True:
                os.system("mosquitto_pub -h " + hostname + " -t " + temperatureQueue1 + " -m " + temperature.Read_Temp1())
                os.system("mosquitto_pub -h " + hostname + " -t " + temperatureQueue2 + " -m " + temperature.Read_Temp2())
                os.system("mosquitto_pub -h " + hostname + " -t " + humidityQueue + " -m " + humi.Read_Humidity())
                os.system("mosquitto_pub -h " + hostname + " -t " + weightQueue + " -m " + weight.Read_Weight())
                os.system("mosquitto_pub -h " + hostname + " -t " + gyroscopeQueueX + " -m " + gyro.Gyroscope_Read_X())
                os.system("mosquitto_pub -h " + hostname + " -t " + gyroscopeQueueY + " -m " + gyro.Gyroscope_Read_Y())
                os.system("mosquitto_pub -h " + hostname + " -t " + gyroscopeQueueZ + " -m " + gyro.Gyroscope_Read_Z())

                time.sleep(0.1)

except KeyboardInterrupt:
        print("Loop was stopped manually")







