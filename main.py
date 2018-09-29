import picamera.array
import picamera
import cv2
import time

def testCamera():
    camera = picamera.PiCamera()
    camera.resolution = (640,640)
    camera.start_recording("test.h264")
    camera.wait_recording(5)
    camera.stop_recording()

if __name__ == "__main__":
    #argparse?

    with picamera.PiCamera() as camera:
        camera.start_preview()
        #camera finishes warming up

        camera.resolution = (640,480)
        camera.framerate = 32
        time.sleep(2)
        with picamera.array.PiRGBArray(camera, size=(640,480)) as stream:
            for frame in camera.capture_continuous(stream, format='bgr'):
                image = frame.array
                cv2.imshow("Frame", image)

                #key = cv2.waitKey(1) & 0xFF

                stream.truncate(0)
                #if key == ord('q'):
                    #break
