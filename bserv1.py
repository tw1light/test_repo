import socket
import os
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
while True:
  for i in range(10):
    npid = os.fork()
  conn, addr = s.accept()
  while True:
    data = conn.recv(1024)
    if not data: break
    if data == b'close()': break
    conn.send(data)
  conn.close()
