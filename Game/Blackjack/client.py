from socket import *

print("==================== START ====================\n")

flag = True

while True:
    clientSock = socket(AF_INET, SOCK_STREAM)
    clientSock.connect(('127.0.0.1', 8080))
    res = clientSock.recv(2024)
    print(res.decode())
    if "win" in res.decode() or "Blackjack" in res.decode():
        clientSock.close()
        break
    if res.decode()[0] == "Y" or not flag:
        pass
    else:
        data = input("(h)it or (s)tand? >> ")
        clientSock.sendall(data.encode())
        if data == "h":
            flag = True
        elif data == "s":
            flag = False