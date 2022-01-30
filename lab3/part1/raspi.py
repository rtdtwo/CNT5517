# LAB 3 - Metronome Thing
# Group: RTX2080
# Members: Bhavya Kavdia, Ekleen Kaur, Rishabh Tatiraju

# raspi.py - The Raspberry Pi code

import RPi.GPIO as GPIO
import time
import requests
import threading

# If running the REST API server in a different device, 
# this will be http://IP_ADDR:PORT
# If running on the Raspberry Pi itself, it can be
# http://localhost:5000
# Running on a different device will add some network latency,
# which is minimal in the same private networks
BASE_SERVER_URL = 'http://192.168.126.226:5000'

# Setting up our GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Play LED
GPIO.setup(18, GPIO.OUT)
# Play / Learn Mode Switch
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_OFF)

# Learn switch and LED
GPIO.setup(16, GPIO.OUT) # LED
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_OFF) # Switch

# Initially setting both LEDs to OFF
GPIO.output(18, False)
GPIO.output(16, False)

# Flags and global variables
learn_mode = False
tap_times = []
calculated_bpm = None
current_bpm = 0

# Senisitivity of the learn switch bounce time in milliseconds
LEARN_SWITCH_BOUNCE_TIME = 250

# Gets the BPM value stored in the server. Then sleeps for 1 second 
# and recursively calls itself again. Since it is a thread-blocking 
# function call, we use a separate thread to run this code.
# See: spawn_server_read_thread()
def get_bpm_from_server():
    global current_bpm
    if not learn_mode:
        response = requests.get(BASE_SERVER_URL + '/bpm')
        if response.status_code == 200:
            current_bpm = response.json()['result']

    time.sleep(1)
    get_bpm_from_server()

# Blinks the LED as per the mode and current BPM value.
# If mode is PLAY, then keeps blinking as per the current BPM value.
# If mode is LEARN, then keeps checking every one second if user has exited the .
def blink_led_by_bpm():
    global current_bpm
    if not learn_mode:
        if current_bpm > 0:
            time_interval = 60.0 / current_bpm
            GPIO.output(16, True)
            time.sleep(0.2)
            GPIO.output(16, False)
            time.sleep(time_interval - 0.2)
            blink_led_by_bpm()  
        else:
            time.sleep(1)
            blink_led_by_bpm()


# Calculate BPM from the tap timings.
# Takes average of the difference in time of the last 4 tap times.
# If number of taps is less than 4, then calculated BPM is set to 
# null, and then evenutally ignored i.e. not sent to server to update.
def calculate_bpm():
    global calculated_bpm

    if len(tap_times) >=4:
        tap_times_to_consider = tap_times[-4:]
        tap_time_difference = []

        for i in range(len(tap_times_to_consider)):
            if i > 0:
                tap_time_difference.append(tap_times_to_consider[i] - tap_times_to_consider[i-1])

        calculated_bpmillis = sum(tap_time_difference) / len(tap_time_difference)
        calculated_bpm = int(60000.00 / calculated_bpmillis)
    else:
        calculated_bpm = None

    tap_times.clear()


# If calculated BPM is not null, then call the API to 
# update the value at the server.
def update_bpm_to_server():
    global calculated_bpm
    if calculated_bpm is not None:
        response = requests.put(BASE_SERVER_URL + "/bpm?bpm=" + str(calculated_bpm))
        if response.status_code == 200:
            print('BPM value updated to {} at the server'.format(calculated_bpm))
            calculated_bpm = None


# Callback function that is triggered when mode switch is pressed.
def press_mode_switch(channel):
    global learn_mode
    # Set mode as inverse of previous mode
    learn_mode = not learn_mode
    if not learn_mode:
        # When the user exits learn mode, we:
        # 1. Calculate the new BPM (if taps is less than 4 then this is set to None)
        calculate_bpm()
        # 2. Update the BPM to server (if calculated BPM is None then this is ignored)
        update_bpm_to_server()
        # 3. Restart the threads to blink and sync with the server (going to learn mode stops the threads)
        spawn_led_blink_thread()
        spawn_server_read_thread()
        print("In play mode")
    else:
        print("In learn mode")
            
# Callback function that is triggered when learn switch is pressed.
def press_learn_switch(channel):
    global tap_times
    # Get timestamp of the tap, then multiply by 1000 
    # to get millisecond value
    timestamp = time.time() * 1000;
    # Append the timestamp to the tap arrays. This will later be used when calculating the BPM.
    tap_times.append(timestamp)
    # Light up the learn LED for 100 ms and then switch it off
    GPIO.output(18, True)
    time.sleep(0.1)
    GPIO.output(18, False)

# Setup event detection for both switches and add callback and bounce time.
# Bounce time is tweaked from trial and error.
GPIO.add_event_detect(12, GPIO.FALLING, callback = press_mode_switch, bouncetime = 2000) 
GPIO.add_event_detect(23, GPIO.FALLING, callback = press_learn_switch, bouncetime = LEARN_SWITCH_BOUNCE_TIME)

# This creates a new thread that asynchronously calls the server API to sync up with the server.
def spawn_server_read_thread():
    update_from_server_thread = threading.Thread(target=get_bpm_from_server, args=(), kwargs={})
    update_from_server_thread.start()

# This creates a new thread that asynchronously blinks the play LED.
def spawn_led_blink_thread():
    blink_led_thread = threading.Thread(target=blink_led_by_bpm, args=(), kwargs={})
    blink_led_thread.start()

# Start both threads
spawn_server_read_thread()
spawn_led_blink_thread()