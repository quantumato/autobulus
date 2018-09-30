import serial

ser=serial.Serial('/dev/ttyACM0', 9600)

ser.flushInput()

while 1:
	ser.write('A')
	var = ser.read()
	print(var)
