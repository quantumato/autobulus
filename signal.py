import serial
import RPi.GPIO as GPIO

ser=serial.Serial('/dev/ttyACM0', 9600)

ser.flushInput()
GPIO.cleanup()
GPIO.setup(channel, GPIO)
GPIO.setmode(GPIO.BOARD)

def testSerial():
	while 1:
		ser.write('A')
		var = ser.read()
		print(var)

def pinHigh(pin):
	GPIO.output(pin, GPIO.HIGH)

def pinHigh(pin):
	GPIO.output(pin, GPIO.LOW)

def rotateYaw(degrees):
	#40 = high 
	#38 = low
	#36 = high
	#all low to turn off

	#constant to convert degrees to seconds
	deg2sec = 0.1;
	GPIO.setup(40, GPIO.OUT, intiial=GPIO.LOW)
	GPIO.setup(40, GPIO.OUT, intiial=GPIO.LOW)
	GPIO.setup(40, GPIO.OUT, intiial=GPIO.LOW)
	

def rotatePitch(degrees):
	#8 = high
	#10 = low
	#12 = high
	#all low to turn off

	GPIO.setup(40, GPIO.OUT, intiial=GPIO.LOW)
	GPIO.setup(40, GPIO.OUT, intiial=GPIO.LOW)
	GPIO.setup(40, GPIO.OUT, intiial=GPIO.LOW)
