# This is script monitors GPIO pin #23 with a door contact sensor
# If the sensor is open, it turns on the LED connected on pin #18
# This is hardware dependend on Raspberry PI's
import RPi.GPIO as GPIO
import time


door_pin = 23
led_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(door_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin, GPIO.OUT)
 
while True:
    if GPIO.input(door_pin):
        print("DOOR OPEN!")
        GPIO.output(led_pin, True)
    else:
        print("Door is closed")
        
        
    time.sleep(0.5)
    GPIO.output(18, False)
