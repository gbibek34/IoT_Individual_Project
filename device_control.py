import time 
import RPi.GPIO as GPIO # Importing GPIO Control for the servo motor
from pushbullet import Pushbullet # Importing pushbullet for notification

def device_control(auth_status):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # For Servo
    GPIO.setup(11, GPIO.OUT)
    #For LED
    GPIO.setup(37, GPIO.OUT)
    GPIO.output(37, GPIO.LOW)
    GPIO.setup(36, GPIO.OUT)
    GPIO.output(36, GPIO.LOW)
    #For Buzzer
    GPIO.setup(16, GPIO.OUT)
    GPIO.output(16, GPIO.OUT)
    
    # Token of the application
    pb = Pushbullet("o.XBw4z4K0q0jbTsIMUsh44biNiZ7w7ydk")
    
    # Outputs
    if auth_status == True:
        GPIO.output(37, GPIO.HIGH) # LED on

        servo = GPIO.PWM(11,50)

        servo.start(0)
        print("Opening the door...")
        time.sleep(1)

        #Opening
        servo.ChangeDutyCycle(7)
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)
        time.sleep(4.5)

        #Closing
        print("Closing the door...")
        servo.ChangeDutyCycle(2)
        time.sleep(0.5)
        servo.ChangeDutyCycle(0)

        servo.stop()
        GPIO.cleanup()
        print("Door is closed")
        time.sleep(2)
    else:
        GPIO.output(36, GPIO.HIGH)
        GPIO.output(16, GPIO.HIGH)
        dev = pb.get_device("Xiaomi Mi A3")
        push = dev.push_note("Alert","An unauthorized attempt to enter")
        time.sleep(5)
        GPIO.cleanup()