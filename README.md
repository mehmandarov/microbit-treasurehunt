# Micro:Bit Treasure Hunt

Welcome to the treasure hunt game with micro:bits!

This is how we play this game:
1. We have a set of micro:bits set up as senders 📡 hidden somewhere
    - These devices are set up by the game organisers before we start.
    - We tell you the number of devices you need to find.
3. You have to build a receiver 📶 to look for the devices.
    - Scroll down to the `Receiver 📶` section for pointers.

## Setup 🛠
We are using:
* micro:bit ([homepage](https://microbit.org/))
* DFRobot micro:bit Circular RGB Expansion board v2.0 ([docs](https://wiki.dfrobot.com/Micro_bit_Circular_RGB_LED_Expansion_Board_SKU__ROB0150))

## Sender 📡
1. There are several sending beacons hidden somewhere around you. 
2. Ask organisers how many beacons are hidden out there.
3. All beacons are broadcasting a message on one of the channels between 1 and 6. Assume this unless you are told otherwise.

## Receiver 📶
You need to implement a set of basic functions on your receiver beacon (in addition to functions that you might be told by the sender beacon you might find).

Pseudocode for the receiver beacon:
1. Scan for packages on channel X (typically 1 to 6) and show signal strength.
2. If the signal strength is larger than `-50` print the message that is being transmitted on your micro:bit.
3. The message you receive will tell you what to do.
4. Locate the sending beacon (yes, physically find it!) and do what you have been told in the previous step.
    - It can be something you need to do on the sending beacon
    - It can be something you need to code on your receiver
