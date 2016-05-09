import socket
import os
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
for i in range(10):
  pid = os.fork()
if pid==0:
  while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    if not data: break
    if data == b'close': break
    conn.send(data)
  conn.close()
