## Hardware plateform for the routing and signaling system.

![cntl routes and signals](https://github.com/user-attachments/assets/8ca23532-cb3b-4c64-ad9e-50e5159e5fe6)

- [RPi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/): controler of the system, will be soon upgraded to RPi Pico 2W.
- [MCP 23017 I2C port exoander](https://www.adafruit.com/product/5346): as we need 45 outputs for the LED and 14 inputs for the track occupancy detection, port expanders were necessary.
- [5206 module from Viessmann](https://viessmann-modell.com/en/electronic/electronics-digital/104track-occupancy-detector-8-sections/5206) are used for track occupancy detection. This option is quite expensive and it is possible to use a custom circuit instead ([see here](https://forum.mrhmag.com/post/build-a-simple-block-occupancy-detector-12207949)).
- The user interface used a 7" touch screen from [Nextion](https://nextion.tech/datasheets/nx8048p070-011c/)
- An Optical Control Board for track accupancy using Neopixel LEDs [custom design](ocb)
