#!/usr/bin/env python3

import sys  # Importing the sys module for program control and exit handling
import socket  # Importing the socket module for network operations
from datetime import datetime  # Importing the datetime class from the datetime module for working with dates and times

# Prompt the user to enter the IP address to scan for open ports
HOST = input("Please enter the IP address on which you want to check open ports: ")

print("-" * 50)
print("STARTING SCANNING: " + str(datetime.now()))  # Print the current date and time when the scanning starts

try:
    # Iterate over a range of port numbers (from 50 to 84)
    for port in range(50, 85):
        # Create a new socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a default timeout of 1 second for the socket operations
        socket.setdefaulttimeout(1)

        # Attempt to establish a TCP connection with the specified IP address and port number
       # s.connect_ex , The method attempts to establish a TCP connection to the specified address. If the connection is successful, it returns 0 (indicating no error).
      #If the connection is unsuccessful, it returns an error code 
 
        result = s.connect_ex((HOST, port))

        # If the result is 0, the port is open
        if result == 0:
            print("Port {}: Open".format(port))  # Print a message indicating an open port

        # Close the socket connection
        s.close()

except KeyboardInterrupt:
    # If the user interrupts the program with Ctrl+C, print a message and exit
    print("Exiting program")
    sys.exit()
