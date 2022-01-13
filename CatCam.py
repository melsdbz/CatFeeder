import picamera
import time

def takePic(filename):

    cam = picamera.PiCamera()

    cam.start_preview
    time.sleep(3)
    cam.capture(filename)
    cam.stop_preview
