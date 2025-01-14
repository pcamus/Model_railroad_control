# File wifi_ecos.py
# Definition of the interfaces, signals and routes
# info@pcamus.be
# 26/01/24

import network, socket
import struct
from secrets import *
from utime import sleep

# definition of the functions used to control the lan connexion, the signal aspects
# the track occupancy and the tco 
def wifi_connect():
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
        sleep(1)

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
    
    return wlan

# Connect to ECoS.
def ECoS_connect():
    host = "192.168.0.121"
    port = 15471                  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
    except:
        return None
    
    return s


def set_route(s, route_id):
    command="set(" + str(route_id) + ",state[1])"
    s.sendall(command.encode('ascii'))
    data = s.recv(1024)
    print('Received: ', data.decode('ascii'))
    