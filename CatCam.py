import picamera
import time
import random

def takePic(filename):

    cam = picamera.PiCamera()
    cam.resolution = (1600, 1200)
    cam.start_preview
    effects = list(cam.IMAGE_EFFECTS.keys())
    cam.image_effect = effects[random.randint(0,21)]
    time.sleep(3)
    cam.capture(filename)
    cam.stop_preview
