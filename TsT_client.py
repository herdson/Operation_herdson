import sys,socket
IP="127.0.0.1"
Port=8888

print("Client online")
sckt=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sead=(IP, Port)
sckt.connect(sead)

while True:
    msg=input()
    sckt.sendall(msg.encode())
    data=sckt.recv(1024)
    print("Data from server: %s" % data.decode())
sckt.close()
