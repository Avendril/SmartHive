import temp3 as temperature
import humidity as humi
import gyroscope as gyro
import connectArd as weight
import time
import os
import paho.mqtt.publish as publish

def publish_data(queue,message):
	publish.single(str(queue), str(message), hostname="10.37.28.64")

while True:
#Publish data from the ds18b20 sensors from temp3.py file in the same directory
	publish_data("SmartHive/Temperature/Temp1",temperature.Read_Temp1())
	publish_data("SmartHive/Temperature/Temp2",temperature.Read_Temp2())
#Publish data from the MPU6050 sensor from gyroscope.py file in the same directory
	
	#Accelerator data x,y,z
	publish_data("SmartHive/Accelerometer/X-Axis",gyro.Accelerometer_Read_X())
	publish_data("SmartHive/Accelerometer/Y-Axis",gyro.Accelerometer_Read_Y())
	publish_data("SmartHive/Accelerometer/Z-Axis",gyro.Accelerometer_Read_Z())
	#Gyroscope data x,y,z
	publish_data("SmartHive/Gyroscope/X-Axis",gyro.Gyroscope_Read_X())
	publish_data("SmartHive/Gyroscope/Y-Axis",gyro.Gyroscope_Read_Y())
	publish_data("SmartHive/Gyroscope/Z-Axis",gyro.Gyroscope_Read_Z())
	#Temperature data *C
#	publish_data("SmartHive/DHT22/Humidity","Humidity: " + humi.Read_Humidity())
	publish_data("SmartHive/DHT22/Humidity",str(humi.Read_Humidity()))

#Publish data from the Weight Scale connected on Arduino
#	print str(weight.Read_Weight())
	publish_data("SmartHive/Weight",str(weight.Read_Weight()))
	
