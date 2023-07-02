#!/usr/bin/env python3

import sys
import socket
from datetime import datetime

HOST = input("Please enter the IP address on which you want to check open ports: ")

print("-" * 50)
print("STARTING SCANNING: " + str(datetime.now()))

try:
    for port in range(50, 500):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((HOST, port))
        if result == 0:
            print("Port {}: Open".format(port))
        s.close()

except KeyboardInterrupt:
    print("Exiting program")
    sys.exit()
