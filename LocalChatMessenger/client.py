import socket
import sys

#TCP/IPソケットの作成
sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

#サーバーが待ち受けているポートにソケットを作成する
server_address = '/socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    #データ送信
    message = b'Sending a message to the server side. Afterwards, will wait for a response to print out.'
    sock.sendall(message)

    #ソケットが閉じるまでのタイムアウトを2秒に設定します
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