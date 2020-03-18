import socket

c = socket.socket()

c.connect(('localhost',9999))

name = input('Enter the connection name : ')
c.send(bytes(name,'utf-8'))
input_name = c.recv(1024).decode()
print('Welcome : ',input_name)
print(c.recv(1024).decode())
option = input('\n Select from one of the above')
c.send(bytes(option,'utf-8'))

response_rcvd = c.recv(1024).decode()
print(response_rcvd)
final_response_rcvd = c.recv(1024).decode()

print(final_response_rcvd)

