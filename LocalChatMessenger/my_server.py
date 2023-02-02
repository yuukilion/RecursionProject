import socket
import os
from faker import Faker

fake = Faker()

print(fake.name())
sock = socket.socket(socket.AF_UNIX,socket.SOCK_STREAM)

server_address = '/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

#ソケットをアドレスに紐づけ
print('Starting up on {}'.format(server_address))
sock.bind(server_address)

sock.listen(1)



while True:
    #acceptはキューにある次の接続を受け入れる。(connection,client_address)のタプルを返す。
    #ソケットは全二重なので、接続はクライアントとデータを送受信するための別のソケットオブジェクト。
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        #データを小分けにして受信し、再送信する
        while True:
            data = connection.recv(16)
            data_str = data.decode('utf-8')
            
            print('Received ' + data_str)
            if data:
                #現在のクライアントにメッセージを送り返す
                response = 'Processing ' + data_str
                connection.sendall(response.encode())
                print(fake.name())
            else:
                print('no data from', client_address)
                break

    finally:
        #接続のクリーンアップ
        print("Closing current connection")
        connection.close()