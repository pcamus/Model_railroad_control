# File nextion_dlg.py
# Dialog routine for Nextion display
# https://github.com/gheinzer/micropython-nextion/
# Nextion file Mlb_block5.HMI
# info@pcamus.be
# 21/01/24

from nextion import nextion
from machine import Pin
from sign_route_def import *

display = nextion(Pin(4), Pin(5), 9600)

def blocking_read_Nextion():
    while(True): # wait until a message is sent by Nextion display
        value=display.read()
        #print(value)
        if value!=None:
            break
    
    return value # [0]=0x71 [1]=de [2]=vers [3]=via [4]=pm [5..7]=0xFF
                 # [4]&0xF0 == 0x00 : Montleban
                 # [4]&0xF0 == 0x10 : Gare cachée
                 # [4]&0xF0 == 0x20 : Achouffe
                 # [4]&0xF0 == 0x40 : Colanhan


def check_route_name(value):
    #************************************************************
    if (value[4]&0xF0)==0x00:  # Montleban
        print("Gare de Montleban")
        route=decode_dico_mo[value[1]]+decode_dico_mo[value[2]]

        if value[3]==2:
            route=route+"1"
        if value[3]==4:
            route=route+"2"

        if value[4]==1:
            route=route+"pm"

        print(route)

    #************************************************************
    if (value[4]&0xF0)==0x10:  # Gare cachée
        print("Gare cachée")
        route=decode_dico_gc[value[1]]

        print(route)

    #************************************************************
    if (value[4]&0xF0)==0x20:  # Colanhan
        print("Carrière de Colanhan")
        route=decode_dico_co[value[1]]

        print(route)

    #************************************************************
    if (value[4]&0xF0)==0x40:  # Achouffe
        print("Gare d'Achouffe")
        route=decode_dico_ac[value[1]]

        print(route)

    try:
        selected_route=(routes[route])
    except:
        display.cmd('t24.bco=64528')  # fond orange
        display.cmd('t24.txt="Route incorrecte"')
        return None
    else:
        display.cmd('t24.bco=65535')  # fond blanc
        display.cmd('t24.txt="Route : '+route+'"')
        return selected_route


def occupied_track_disp():
    display.cmd('t24.bco=64512')
    display.cmd('t24.txt="Route occupee."')

def route_end_disp():
    display.cmd('t24.bco=65535')
    display.cmd('t24.txt=""')
    

def display_init(text):
    display.cmd('t0.txt="'+text+'"')

def hide_init_text():
    display.cmd('vis t0,0')
    
def show_init_text():
    display.cmd('vis t0,1')

def hide_stop_next_btn(): # remowe pic and disable buttons
    display.cmd('vis p0,0')
    display.cmd('tsw b0,0')
    display.cmd('vis p1,0')
    display.cmd('tsw b1,0')
    
def show_stop_next_btn(): # redraw pic and enable buttons
    display.cmd('vis p0,1')
    display.cmd('tsw b0,1')
    display.cmd('vis p1,1')
    display.cmd('tsw b1,1')
    
def clear_route_disp(): # clear route radio button via hotspot m0
    display.cmd('click m0,1')

def goto_page(num):
    display.page(num)