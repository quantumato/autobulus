import serial
import RPi.GPIO as GPIO
import time
import sys

#ser=serial.Serial('/dev/ttyACM0', 9600)

#ser.flushInput()
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

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
	#38 = low	//direction 
	#36 = high	//direction
	#all low to turn off

	#constant to convert degrees to seconds
	#APPROXIMATELY 2-3degrees
	deg2sec = 0.015;

	#run the motor
	
	#LEFT
	#if direction == 1:
	if degrees > 3:
		degrees = 3;
	elif degrees < -3:
		degrees = -3
		
	if degrees < 0:
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(38, GPIO.LOW)
		GPIO.output(36, GPIO.HIGH)
	else:
		GPIO.output(40, GPIO.HIGH)
		GPIO.output(38, GPIO.HIGH)
		GPIO.output(36, GPIO.LOW)

	#sleep
	time.sleep(deg2sec*abs(degrees))

	#STOP
	GPIO.output(40, GPIO.LOW)
	GPIO.output(38, GPIO.LOW)
	GPIO.output(36, GPIO.LOW)
	return 0
	

def rotatePitch(degrees):
	#8 = high	//direction
	#10 = low	//direction
	#12 = high
	#all low to turn off
	
	#constant to convert degrees to seconds
	deg2sec = 0.015;

	#run the motor

	if degrees > 1:
		degrees = 1;
	elif degrees < -1:
		degrees = -1

	#DOWN
	if degrees < 0:
		GPIO.output(8, GPIO.HIGH)
		GPIO.output(10, GPIO.LOW)
		GPIO.output(12, GPIO.HIGH)
	else:
		GPIO.output(8, GPIO.LOW)
		GPIO.output(10, GPIO.HIGH)
		GPIO.output(12, GPIO.HIGH)

	#sleep
	time.sleep(deg2sec*abs(degrees))

	#STOP
	GPIO.output(8, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	return 0
	
'''
if int(sys.argv[2]) != -1:
	rotatePitch(1,int(sys.argv[2]))
if int(sys.argv[1]) != -1:
	rotateYaw(1,int(sys.argv[1]))
'''

rotatePitch(4)
#rotatePitch(2, 1)
