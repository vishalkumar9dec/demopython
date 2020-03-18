import socket

s = socket.socket()

print('socket created')

s.bind(('localhost',9999))

s.listen(3)

print('Waiting for the connection')

while True:
    c,add = s.accept()
    name = c.recv(1024).decode()
    print('CLient connected',add,name)
    c.send(bytes(name,'utf-8'))
    c.send(bytes('You are now connected to the server'
                 ' What would you like to do today'
                 ' 1. Learn Python '
                 '2. Order Food '
                 '3. Others ','utf-8'))

    opt_rcvd = c.recv(1024).decode()
    if opt_rcvd == '1':
        response = 'Please refer to the Telusko Tutorial on Youtube'
    elif opt_rcvd == '2' :
        response = "You can either use Swiggy or Zomato for the same. But you should avoid this" \
                   "during Corona spread. We encourage you to cook at home"
    else:
        response = "Sorry !! You should be studying right now"

    c.send(bytes(response,'utf-8'))
    final_response = 'I hope i was helpful for you today'
    c.send(bytes(final_response,'utf-8'))

    c.close()