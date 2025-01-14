## Optical Control Board for track accupancy of Block 5.

This custom board uses Neopixel LEDs to display occupancy of the tracks. White = free, red  = occupied.
The silskscreen depicts the track layout. Detection is made with two 5206 modules from Viessmann. The outputs of the detection module are connected to port expander 0 and read by the RPi Pico that send commands to the Neopixel LEDs to display the occupancy status.

![occupancy01](https://github.com/user-attachments/assets/cf67fe6f-affa-42f7-a174-2cf1cb8f95b5)

