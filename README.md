# Model_railroad_control

This repository is about controlling my 1/87e railroad layout.

I'm using an ESU [ECoS command station](https://www.esu.eu/en/products/digital-control/ecos-50210-dcc-system/what-ecos-can-do/) to control the train and turnouts position on my layout and I want to add routing and signaling functions using Raspberry Pi Pico modules.

- [First step](Adding_WiFi): adding WiFi to the ECoS station.
- [Second step](ECOS_Protocol): find information about the communication protocol used by the ECoS station and implement the part of this protocol concerning turnouts and routes control.
- [Third step](hardware): desing and test of the routing and signaling interface and control.
