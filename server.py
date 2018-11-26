import socket
import threading

global_User = []
global_connection = []


def serverListen(connection, address, Name):
    while(True):
        try:
            data = connection.recv(1024).decode('utf-8')
        except ConnectionResetError:
            print(Name + " has left!!!")
            global_User.remove(address)
            global_connection.remove(connection)
            connection.close()
            break
        for each in global_connection:
            if each != connection:
                each.send((Name+"-->"+data).encode('utf-8'))

def serverSend(conn):
    for each in conn:
        each.send(('Available User: '+str(len(global_User)-1)).encode('utf-8'))


if __name__ == '__main__':
    objectSocket = socket.socket()
    print("Server Started !!!!")
    print("Waiting for clients!!!")
    objectSocket.bind(('127.0.0.1', 12000))
    objectSocket.listen(3)

    while True:
        try:
            connection, address = objectSocket.accept()
            global_User.append(address)
            global_connection.append(connection)
            Name = connection.recv(20).decode('utf-8')
            serverSend(global_connection)
            print(Name + ' came in chat room!!!')
            threading.Thread(target=serverListen, args=(connection,address,Name,)).start()
        except ConnectionResetError as e:
            pass

