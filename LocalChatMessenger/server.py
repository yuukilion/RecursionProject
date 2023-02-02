import socket
import os

#TCP/IPソケットの作成
#socketメソッドは常にソケットオブジェクトを返す
#AF_UNIXは同じシステム上のプロセス間の通信を提供、SOCK_STREAMはTCPを使用

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

#ソケットを作成したら、ソケットにアドレスを紐づけ、接続を待ち受けて受け入れる必要がある
#ローカルソケットを使用しているため、AF_UNIXはファイル名をアドレスとして取り込む
server_address = '/socket_file'

#ファイルが存在しないことを確認
#unlinkは、os.removeと等価で、引数のfile_pathを削除
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

#ソケットをアドレスに紐づけ
print('Starting up on {}'.format(server_address))
sock.bind(server_address)

#接続の着信を最大一件まで待ち受ける。一個以上の未受信の接続を受信すると、自動的に接続を拒否。複数回接続する場合は、1以上に設定する。
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
            else:
                print('no data from', client_address)
                break

    finally:
        #接続のクリーンアップ
        print("Closing current connection")
        connection.close()
