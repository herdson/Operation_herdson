import sys, socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8888))
while True:
   msg = input()
   s.sendall(msg.encode())
   data = s.recv(1024)
   if not data:
      break
   print("Echo from Server Data : %s" % data.decode())
s.close()