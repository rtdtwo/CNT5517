from socket import socket, AF_INET, SOCK_DGRAM

mySocket = socket(AF_INET,SOCK_DGRAM)

def send_data(data, server_ip, port):
    print('Edge computer sending data to Rpi with IP {} on port {}'.format(server_ip, port))
    mySocket.sendto(data.encode(), (server_ip, port))
