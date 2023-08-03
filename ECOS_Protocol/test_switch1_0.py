# File: test_switch1_0.py
# Send switch command to ECoS station
# See https://docs.micropython.org/en/latest/library/network.WLAN.html for WiFi connection
# See https://docs.micropython.org/en/latest/library/socket.html for socket usage
# See https://docs.python.org/3/library/struct.html for structure management
# info@pcamus.be
# 26/3/2023

import network, socket
import struct
from secrets import *
import utime

#WiFi connection
wlan = network.WLAN(network.STA_IF) # Creates a WLAN object and initializes it
wlan.active(True)
wlan.connect(my_secrets["ssid"],my_secrets["WiFi_pass"])

print("Connection to WiFi network.")
print("---------------------------")
print("Trying to connect to WiFi...")
print()

# Waits for connection or exit with error code if it fails
retry = 10
while (retry > 0):
    wlan_stat=wlan.status()
    if wlan_stat==3:
        print("Got IP")
        break
    if wlan_stat==-1:
        raise RuntimeError('WiFi connection failed')
    if wlan_stat==-2:
        raise RuntimeError('No AP found')    
    if wlan_stat==-3:
        raise RuntimeError('Wrong WiFi password')
    
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    retry = retry-1
    utime.sleep(1)

if wlan_stat!=3:
    raise RuntimeError('WiFi connection failed')


print()
print('Connected to WiFi network: ',end="")
print(wlan.config("ssid"))
print()
ip=wlan.ifconfig()
print("IP info (IP address, mask, gateway, DNS):")
print(ip)
print()

# Now we can use the connection to access Internet.
host = "192.168.0.121"
port = 15471                  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#s.sendall(b'get(1,status)')
for i in range(4):
    s.sendall(b'set(11,switch[1r])')
    data = s.recv(1024)
    print('Received: ', data.decode('ascii'))
    utime.sleep(2)
    
    s.sendall(b'set(11,switch[1g])')
    data = s.recv(1024)
    print('Received: ', data.decode('ascii'))
    utime.sleep(2)    

s.close()

#print('Received: ', data.decode('ascii'))

# Close connection
wlan.disconnect()