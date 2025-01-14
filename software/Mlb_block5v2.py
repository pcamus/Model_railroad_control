# File Mlb_block5v2.py
# Controlling routes and signals via console
# This code is intended to check track occupancy for a given route,
# to turn on signals for the route to their appropriate values,
# turn on signals to red after train is passing, display occupancy on the tco
# and send a route command to the ECoS
# is using a pushbutton to cancel routes 
# https://learn.adafruit.com/adafruit-mcp23017-i2c-gpio-expander
# info@pcamus.be
# 15/01/24

from machine import Timer

import gc
import os
import machine
import sys

from track_tco import disp_tco, disp_tco_off # routines to display routes ont he tco
from sign_route_def import * # definition of signals & routes, routines 
import nextion_dlg
from signals_cmd import *
from wifi_ecos import *

timer_tco=Timer()
occupancy=[0]*14 # track 1..14 occupancy. 1=presence detected
                 # will be used as a global variable to collect data from callback function

def rpi_stat():
    s = os.statvfs('/')
    print(f"Free storage: {s[0]*s[3]/1024} KB")
    print(f"Memory: {gc.mem_alloc()} of {gc.mem_free()} bytes used = {int(gc.mem_alloc()/gc.mem_free()*100)}%")
    print(f"CPU Freq: {machine.freq()/1000000}Mhz")    


def check_route_free(selected_route): # check if a given route is free
    if selected_route:
        for signal in selected_route:
            if occupancy[signal[2]-1]==0: # signal[2]-1 = track protected by signal
                return False              # tracks are numbered 1..14  and I/O data 0..13
    return True


def tco_call(timer):  # get track occupancy values and display occupancy on the tco
    global occupancy  # global variable for occupancy to be shared outside the callback function
    for i in range(0,14):
        occupancy[i]=mcp0[i].value()
    disp_tco(mcp0)    


# main code start here *****************************************************************************
while True:
    nextion_dlg.goto_page(0)
    nextion_dlg.hide_init_text() # hide text zone t0
    nextion_dlg.blocking_read_Nextion() # wait until start button is pressed
    nextion_dlg.show_init_text()
    # Try to connect to WiFi
    nextion_dlg.display_init("Trying to connect to WiFi")
    wic=wifi_connect()

    nextion_dlg.display_init("My IP:"+wic.ifconfig()[0])
    sleep(2)

    s=ECoS_connect() # Connect to ECoS
    if not s:
        nextion_dlg.display_init("Unable to connect to ECos")
        sys.exit()
    else:
        nextion_dlg.display_init("Connected to ECos")
    sleep(2)
    nextion_dlg.goto_page(1)    

    # This timer is used to check periodicaly track occupation and to display it on the tco
    timer_tco.init(freq=0.5, mode=Timer.PERIODIC, callback=tco_call)

    turn_red_all_signals() # when starting, all signals go to red

    while True:
        #*************
        gc.collect()  # run garbage collector & display memory size
#       rpi_stat()
        #*************
        while True:
            route_name=nextion_dlg.blocking_read_Nextion()
            
            if (route_name[4]==0x80): # stop button pressed************
                break # exit the current while loop
            
            selected_route=nextion_dlg.check_route_name(route_name)    
            if selected_route :
                break

        if (route_name[4]==0x80):# stop button pressed*****************
                break  # exit the current while loop
        
        ok=check_route_free(selected_route[0])
        if not ok:
            print("Selected route is occupied")
            nextion_dlg.occupied_track_disp()
            continue
     
        route_id=selected_route[1]
        print("Route id=",route_id)
        if route_id!=0 :
            set_route(s,route_id)

        turn_on_signals(selected_route[0]) # selected_route[0] = list of signals for
                                           # selected route (could be empty)
        

        if selected_route[0]: # if there is at least a signal in the list
            nextion_dlg.hide_stop_next_btn() # hide next and end buttons until route is free

        for signal in selected_route[0]:
            signal_name=signal[0]  
            while (occupancy[signal[2]-1]==1) and mcp0[14].value()==1:
                # tracks are numbered 1..14  and I/O data 0..13
                pass # wait until track is clear or route is canceled
            turn_red_signal(signal_name)

        nextion_dlg.route_end_disp() # clear route name on Nextion
        nextion_dlg.clear_route_disp() # clear radio buttons
        nextion_dlg.show_stop_next_btn() # route is free, show next and end buttons

    s.close()
    turn_off_all_signals()
    disp_tco_off()
    timer_tco.deinit()

            
