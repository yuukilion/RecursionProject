import socket
import os

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = '/udp_socket_file'
address = '/udp_client_socket_file'
message = b'Message to send to the client.'

#このクライアントのアドレスを紐づけする
#AF_UNIXの場合、相手ソケットが送信元アドレスとして受け取るアドレス

#以下のtry-except内でアドレスの紐づけを解除する
try:
    #アドレスの紐づけを解除する
    os.unlink(address)
except FileNotFoundError:
    pass

sock.bind(address)

try:
    #データを送信
    print('sending {!r}'.format(message))
    sent = sock.sendto(message,server_address)

    #応答を受信
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    print('closing socket')
    sock.close()