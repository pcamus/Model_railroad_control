## ECoS protocol.

In this project my goal is to control the switching of my turnouts with a Raspberry PI Pico.

The station has a communication protocol using a TCP connection on the 15471 port on which commands are sent. These commands use a string format.

The station is accessed by the means of objects linked to a numeric identifier. In our application we will use the object **11** which is the switching item manager.

The message to be sent is the following : `set(11,switch[<n><d>])`

`<n>` is the turnout number, `<d>` is '**g**' (grün = straight) or '**r**' (rot = deviated)

For instance `set(11,switch[4g])` means set turnout 4 to straigkt position.


