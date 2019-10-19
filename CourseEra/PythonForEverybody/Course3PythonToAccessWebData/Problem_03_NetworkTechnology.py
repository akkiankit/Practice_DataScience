
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#making the connection between two computer at transport layer
# GET http://data.pr4e.org/page1.htm HTTP/1.0

mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#encode converts the string in bytess
# we use encode as there are some strings inside of python that are unicode
print(cmd)
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()
