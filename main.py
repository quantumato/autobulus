import picamera.array
import picamera
import cv2
import time
import imutils
from signal1 import *

IMG_WIDTH = 240
IMG_HEIGHT = 240
WCENTER = IMG_WIDTH/2
HCENTER = IMG_HEIGHT/2

def testCamera():
	camera = picamera.PiCamera()
	camera.resolution = (240,240)
	camera.start_recording("test.h264")
	camera.wait_recording(5)
	camera.stop_recording()

#NOTE: possible speedup -> convert to grayscale
with picamera.PiCamera() as camera:
	#camera.start_preview()
	#camera finishes warming up

	camera.resolution = (IMG_WIDTH,IMG_HEIGHT)
	camera.framerate = 32
	camera.vflip = True
	camera.hflip = True
	#camera.awb_mode = 'off'
	#camera.awb_gains = (1.0, 1.0)
	time.sleep(2)
	prev = None

	dkernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (18, 18))
	ekernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
	with picamera.array.PiRGBArray(camera, size=(IMG_WIDTH,IMG_HEIGHT)) as stream:
		counter = 0
		for frame in camera.capture_continuous(stream, format='bgr', use_video_port=True):
			image = frame.array
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			gray = cv2.GaussianBlur(gray, (21, 21), 0)
			#cv2.imshow("Frame", gray)
			#print "frame read"

			key = cv2.waitKey(1) & 0xFF

			if prev is None or counter > 0:
				prev = gray.copy().astype("float")
				stream.truncate(0)
				counter = counter - 1
				continue
			else:
				#get the diff between the frames
				cv2.accumulateWeighted(gray, prev, 0.5)
				delta = cv2.absdiff(gray, cv2.convertScaleAbs(prev))

				thresh = cv2.threshold(delta, 10, 255, cv2.THRESH_BINARY)[1]

				#now that we have blobs let's dilate to fill in the holes
				thresh = cv2.dilate(thresh, dkernel, iterations=1)
				thresh = cv2.erode(thresh, ekernel, iterations=1)

				#cv2.imshow("Thresh", thresh)

				#find contours
				#NOTE: without copy() we just get edges
				cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL,\
					cv2.CHAIN_APPROX_SIMPLE)
				#don't know why this line is necessary
				cnts = cnts[0] if imutils.is_cv2() else cnts[1]

				deltax = 0;
				deltay = 0;
				for c in cnts:
					#TODO: tune this value
					if cv2.contourArea(c) < 2500:
						continue

					(x, y, w, h) = cv2.boundingRect(c)
					#cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
					cv2.line(image, (WCENTER, HCENTER), (x+w/2, y+h/2), (0, 255, 0), 5)
					deltax = x+w/2 - WCENTER
					deltay = y+h/2 - HCENTER
					break


				#cv2.imshow("Frame", image)
				print("x",deltax/90.0)	
				print("y",deltay/90.0)	
				
				#rotateYaw(deltax/100.0)
				if deltay != 0:
					rotatePitch((-1)*deltay/90.0)
					counter = 2
				if deltax != 0:
					rotateYaw(deltax/90.0)
					counter = 2

				#not having these lines result in "ghost" images
				prev = gray.copy().astype("float")
				#stream.truncate(0)


				#TODO: handle extrapolation

			stream.truncate(0)
			if key == ord('q'):
				break
