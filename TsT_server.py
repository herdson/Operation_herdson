import sys, socket

IP="192.168.34.196"
Port=8888

sckt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

address=(IP, Port)
sckt.bind(address)
sckt.listen(1)

print("start accept")
clsckt, clad = sckt.accept()
print(clad)

while True:
    data=clsckt.recv(1024)
    if not data:
        break
    clad.sendall(data)
    print("Client: %s" % data.decode())
