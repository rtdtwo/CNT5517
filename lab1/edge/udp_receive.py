from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import requests
import udp_send

# URL of the cloud server where the data will be pushed to
CLOUD_SERVER_URL = 'http://192.168.9.166:9000'

# IP Addresses and Port numbers of the UDP servers running 
# on two RRi's which have the LEDs connected.
RPI_1_IP = '192.168.9.51'
RPI_2_IP = '192.168.9.194'
RPI_PORT=5001

# Setting up a simple UDP server, used to receive data from
# the RPi having the sensor connected.
PORT_NUMBER = 5000
SIZE = 1024
hostName = gethostbyname('0.0.0.0')
mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))
print("Edge computer listening for input on port {}".format(PORT_NUMBER))

# Infinite loop to continuously look for data being sent
while True:
    # Receiving data from the Sensor RPi.
    (data,addr) = mySocket.recvfrom(SIZE)
    print('Received data: "{}". This will be sent to the server.'.format(data))

    # Using library function to send data to the two RPis having LED connected.
    # The data is received as binary, so it is decoded first. Internally, it is 
    # encoded again to binary before being sent via UDP.
    udp_send.send_data(data.decode(), RPI_1_IP, RPI_PORT)
    udp_send.send_data(data.decode(), RPI_2_IP, RPI_PORT)

    # Using the requests library to send a POST request to the clod server with the data.
    # Format: /set_data?moisture=ok
    requests.post('{}/set_data'.format(CLOUD_SERVER_URL), params={'moisture': data.decode()})