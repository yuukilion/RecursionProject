import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server_address = '/udp_socket_file'

try:
    #アドレスの紐づけを解除する
    os.unlink(server_address)
except FileNotFoundError:
    pass

print('starting up on {}'.format(server_address))
sock.bind(server_address)

while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)

    print('received {} bytes from {}'.format(len(data), address))
    print(data)

    if data:
        sent = sock.sendto(data,address)
        print('sent {} bytes back to {}'.format(sent, address))