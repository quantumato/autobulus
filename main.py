import picamera

if __name__ == "__main__":
    #argparse?
    camera = picamera.PiCamera()
    camera.resolution = (640,640)
    camera.start_recording("test.h264")
    camera.wait_recording(5)
    camera.stop_recording()

