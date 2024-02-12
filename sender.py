import socket
import time
import os

code=""
offset=0

with open("ip.txt") as f:
    ip = f.read()
    f.close()

print("connecting...")
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,7331))
print("connected"+ip)

sends=[]
with open("code.txt") as f:
    sends=f.readlines()
    f.close()

for x in range(len(sends)):
    if(("#" in sends[x])==False):
        s.send(bytes.fromhex('03'))
        s.send(bytes.fromhex(sends[x].replace("\n","")))
        print("send "+sends[x])
s.close()
print("disconnected")
time.sleep(3)
