import RPi.GPIO as GPIO
import time

def feed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    
    try:
        servo = GPIO.PWM(18,50)
        servo.start(2.5)
        time.sleep(0.44)
    
    finally:
        servo.stop()
        GPIO.cleanup()
        
def feedSnack():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    
    try:
        servo = GPIO.PWM(18,50)
        servo.start(2.5)
        time.sleep(.22)
    
    finally:
        servo.stop()
        GPIO.cleanup()
        
if __name__ == '__main__':
    feed()
    
