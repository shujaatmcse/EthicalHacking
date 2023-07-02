#Note do not creat file name as socket optherwise it could break
#!/bin/python3
#not required just testing import, just with following you can print system version
import sys;
print(sys.version)


#printing date time
from  datetime import datetime as dt;

print(dt.now())

import socket;

HOST="127.0.0.1"
PORT= 5555;
#AF_Net is ipv and SOCK_STREAM IS REFERRING TO THE PORT
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
