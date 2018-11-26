import socket
import threading
import sys

def clientListen(objectSocket):
    while True:
        try:
            response = objectSocket.recv(1024).decode('utf-8')
            print(response)
        except ConnectionResetError or OSError:
            print("Server is shut down!!!")
            objectSocket.close()
            sys.exit()


def clientSend(objectSocket):
    while True:
        request = input()
        objectSocket.sendall(request.encode('utf-8'))
        if request == 'exit':
            objectSocket.close()
            sys.exit()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 12000
    objectSocket = socket.socket()
    try:
        objectSocket.connect((host,port))
    except ConnectionRefusedError:
        print("Connection is refused by the server!!!")
        sys.exit()

    Name = input("Enter you name: ")
    objectSocket.send(Name.encode('utf-8'))
    threading.Thread(target=clientListen, args=(objectSocket,)).start()
    threading.Thread(target=clientSend, args=(objectSocket,)).start()