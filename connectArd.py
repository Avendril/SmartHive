import serial
import time

def Read_Weight():
	while 1:
		ser = serial.Serial(
			port='/dev/ttyACM0',
			baudrate = 9600,
			parity = serial.PARITY_NONE,
			stopbits = serial.STOPBITS_ONE,
			bytesize = serial.EIGHTBITS,
			timeout = 1
			)

		
		data = ser.readline()
		return data

#while 1:
#	x = ser.readline()
#	print x
