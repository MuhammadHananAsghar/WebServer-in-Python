# CREATED BY MUHAMMAD HANAN ASGHAR
from socket import *
mysock = socket(AF_INET,SOCK_STREAM)
mysock.bind(('localhost',3000))
mysock.listen(5)
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.1\r\n'
mysock.send(cmd)
while True:
	data = mysock.recv(5000)
	if len(data) < 1:
		break
	print(data.decode('utf-8'),end=" ")
mysock.close()
