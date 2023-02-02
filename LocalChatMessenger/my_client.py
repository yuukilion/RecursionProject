import socket
import sys

#TCP
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/socket_file'

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    #入力を受け付ける
    message = bytes(input(),'utf-8')
    sock.sendall(message)

    #ソケットが閉じるまでのタイムアウトを2秒に設定
    sock.settimeout(2)
    try:
        while True:
            data = str(sock.recv(32))
            if data:
                print('Server response: ' + data)
            else:
                break
    except(TimeoutError):
        print('Socket timeout, ending listening for server messages')

finally:
    print('closing socket')
    sock.close()
