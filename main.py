import picamera.array
import picamera
import cv2
import time

IMG_WIDTH = 240
IMG_HEIGHT = 240

def testCamera():
    camera = picamera.PiCamera()
    camera.resolution = (240,240)
    camera.start_recording("test.h264")
    camera.wait_recording(5)
    camera.stop_recording()

if __name__ == "__main__":
    #argparse?


    #NOTE: possible speedup -> convert to grayscale
    with picamera.PiCamera() as camera:
        #camera.start_preview()
        #camera finishes warming up

        camera.resolution = (IMG_WIDTH,IMG_HEIGHT)
        camera.framerate = 32
        time.sleep(2)
        prev = None
        with picamera.array.PiRGBArray(camera, size=(IMG_WIDTH,IMG_HEIGHT)) as stream:
            for frame in camera.capture_continuous(stream, format='bgr', use_video_port=True):
                image = frame.array
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)
                #cv2.imshow("Frame", gray)
                #print "frame read"

                key = cv2.waitKey(1) & 0xFF

                if prev is None:
                    prev = gray.copy().astype("float")
                    stream.truncate(0)
                    continue
                else:
                    #get the diff between the frames
                    cv2.accumulateWeighted(gray, prev, 0.5)
                    delta = cv2.absdiff(gray, cv2.convertScaleAbs(prev))

                    thresh = cv2.threshold(delta, 5, 255, cv2.THRESH_BINARY)[1]

                    cv2.imshow("Frame", thresh)

                    #not having these lines result in "ghost" images
                    #prev = gray.copy().astype("float")
                    #stream.truncate(0)


                stream.truncate(0)
                if key == ord('q'):
                    break
