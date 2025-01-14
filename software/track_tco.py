# file track_tco.py
# Display track occupancy with  neopixel bargraph
# author info@pcamus.be 
# date 18/11/2022
# Neopixel routines adaptated from :
# http://www.pibits.net/code/raspberry-pi-pico-and-neopixel-example-in-micropython.php#codesyntax_1


import array, utime
from machine import Pin, I2C
import rp2
 
# Configure the number of WS2812 LEDs, pins and brightness.
NUM_LEDS = 14
PIN_NUM = 22
brightness = 0.05 # from 0 to 1

#Neopixel protocol is controlled by a pio machine
# Genral Info about rp2: https://docs.micropython.org/en/latest/library/rp2.html#module-rp2
# Specific info for RP2040 : https://docs.micropython.org/en/latest/library/rp2.StateMachine.html
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()
 
 
# Create the StateMachine with the ws2812 program, outputting on Pin(PIN_NUM).
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))
 
# Start the StateMachine, it will wait for data on its FIFO.
sm.active(1)
 
# For the bar graph display with 8 pixels
# Color values (add color if necessary)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)

# Colors list for bagraph
# NUM_LEDS neopixels
disp_list=[BLACK]*NUM_LEDS
disp_off=[BLACK]*NUM_LEDS

# 24 bit data for each neopixel in the GRB order
def pixel_set_and_dim(color, brightness):
    green=int(color[1]*brightness)
    red=int(color[0]*brightness)
    blue=int(color[2]*brightness)
    result= (green<<16)+(red<<8)+blue
    return result

# Used to test library : draws successively all the possible bars
def draw_bar_graph(bar):
    # Array type, see : https://docs.python.org/3/library/array.html
    ar = array.array("I",[0]*NUM_LEDS) # type unsigned integer, initialized with a list of 0

    for i, color in enumerate(bar):
        ar[i]=pixel_set_and_dim(color,brightness)
        
    sm.put(ar, 8) # pushes a word of data to the state machine
    # second parameter indicates a shift value for each pushed data (from ar).
    # data is coded with 32 bits, so the value pushes the 24 bits at the right position.

def disp_tco(mcp):  # switch neopixel to white if track is free, red otherwise
    for i in range(14):
        if (mcp[i].value())==0:
            disp_list[i]=RED
        else:
            disp_list[i]=WHITE

    draw_bar_graph(disp_list)        

        
def disp_tco_off(): # switch tco off
    draw_bar_graph(disp_off)