from socket import socket, AF_INET, SOCK_DGRAM

mySocket = socket(AF_INET,SOCK_DGRAM)

# Edge computer UDP server IP Address and Port
server_ip = '192.168.56.226'
port = 5000

def send_data(data):
    print('Rpi sending data to Edge computer with IP {} on port {}'.format(server_ip, port))
    mySocket.sendto(data.encode(), (server_ip, port))
