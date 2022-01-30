from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import RPi.GPIO as GPIO

# Setting up GPIO for LEDs
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# Helper function to switch on LED
def led_on():
    GPIO.output(18, True)

# Helper function to switch off LED
def led_off():
    GPIO.output(18, False)

# Spawning a UDP server which will receive data from the edge computer
# and switch on or off the light accordingly. Implementation below.
PORT_NUMBER = 5001
SIZE = 1024
hostName = gethostbyname('0.0.0.0')
mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))
print("Rpi listening for input on port {}".format(PORT_NUMBER))

# Infinite loop to continuously read data
while True:
    # Receiving from the Edge computer
    (data,addr) = mySocket.recvfrom(SIZE)
    print('Received data: "{}".'.format(data))
    # Decoding the data and checking condition to switch on or off the LED.
    # In our case, if the moisture is 'ok', we switch on the LED, or switch it off.
    data = data.decode()
    if data == 'ok':
        led_on()
    else:
        led_off()


