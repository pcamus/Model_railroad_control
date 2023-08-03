## Adding WiFi to the ECoS station.

For its remote control, the ECoS station has an Ethernet interface.

For the intended application, it is much more practical to have a wireless connection and therefore to add WiFi.

I simply use an Ethernet to WiFi Bridge that I configured for my home network. 

This bridge is a [Vonets device](http://www.vonets.com/ProductViews.asp?D_ID=14).

I use the DHCP-server feature in the IP Setup of the ECoS. But before choosing the `Get IP setting from DHCP`, it's necessary to enter  the IP address of your router in the `Gateway` Field. As I have to use the given IP address to connect to the station, I use a static DHCP wich give me always the same address (which is linked to the MAC address of the ECoS).

The setup is the below:
![ECosWiFi](https://github.com/pcamus/Model_railroad_control/assets/55027870/7e408f6d-bf34-4d98-bc85-bf05a035ac46)

From left to right: USB power supply, Vonets Bridge, ECoS station, power supply for the ECos.
