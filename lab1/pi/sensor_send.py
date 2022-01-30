import RPi.GPIO as GPIO
import time
import udp_send

# Setting up GPIO for sensor
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
 
# Callback whenever sensor data pin goes HIGH or LOW.
def callback(channel):
    if GPIO.input(channel):
        print("Water Detected!")
        udp_send.send_data('ok')
    else:
        print("Water Not Detected!")
        udp_send.send_data('oops')
 
# Adds an event detection, which lets us know if
# the sensor data pin goes high or low
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# If the above event occurs, we setup what to do 
# - i.e. the callback function
GPIO.add_event_callback(channel, callback)
 
# Infinite loop that continuously runs this script. 
# Sleep is to merely avoid using up all the processor capability.
while True:
        time.sleep(1)