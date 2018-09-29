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


    with picamera.PiCamera() as camera:
        #camera.start_preview()
        #camera finishes warming up

        camera.resolution = (IMG_WIDTH,IMG_HEIGHT)
        camera.framerate = 32
        time.sleep(2)
        with picamera.array.PiRGBArray(camera, size=(IMG_WIDTH,IMG_HEIGHT)) as stream:
            for frame in camera.capture_continuous(stream, format='bgr', use_video_port=True):
                image = frame.array
                cv2.imshow("Frame", image)
                print "frame read"

                key = cv2.waitKey(1) & 0xFF

                stream.truncate(0)
                if key == ord('q'):
                    break
