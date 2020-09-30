from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSock.bind(('', 8080))

while True:
    BUF_SIZE = 2048

    serverSock.listen(3)
    conn, addr = serverSock.accept()
    data = conn.recv(BUF_SIZE)
    msg = data.decode()
    print(msg)

    if msg == 'quit':
        conn.close()
        break

serverSock.close()
