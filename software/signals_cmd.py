# File signals_cmd.py
# routines to control signals LEDs
# https://learn.adafruit.com/adafruit-mcp23017-i2c-gpio-expander
# info@pcamus.be
# 27/01/24

from sign_route_def import * # we need dictionny of routes & signals

def turn_off_signal(signal_name): # turn all leds of specified signal OFF
    selected_signal=signals_def[signal_name]
    iodev=selected_signal[0]
    list_led=selected_signal[1] # from selected signal in the route extract list of led number            
    for led in list_led.values():
        # turn off the necessary leds
        iodev[led].output(1)


def turn_off_all_signals(): # turn all leds of all signals OFF
    for signal in signals_def.values():
        iodev=signal[0] # extract name of I/O device for this signal
        for led in signal[1].values():
            # turn on the necessary leds
            iodev[led].output(1)


def turn_red_signal(signal_name): # turn a specified signal to red
    turn_off_signal(signal_name)
    selected_signal=signals_def[signal_name]
    iodev=selected_signal[0]
    iodev[selected_signal[1]["R"]].output(0)    


def turn_red_all_signals(): # turn all signals to red
    turn_off_all_signals()
    for signal in signals_def.values():
        iodev=signal[0] # extract name of I/O device for this signal
        iodev[signal[1]["R"]].output(0)
      
      
def turn_on_signals(selected_route): # turn leds of chosen route to appropriate values
    
    for signal in selected_route:
        # for each signal in the selected route
        signal_name=signal[0] # extract signal name
        turn_off_signal(signal_name) # turn off all leds of signal
        
        selected_signal=signals_def[signal_name] # extract signal definition for this signal
        
        iodev=selected_signal[0] # extract name of I/O device for this signal
        
        list_on=signal[1] # for selected signal in the route extract list of leds to turn on
                
        for led in list_on:
            # turn on the necessary leds
            iodev[selected_signal[1][led]].output(0)
