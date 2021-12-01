# Micro:Bit Treasure Hunt

### Welcome to the treasure hunt game with micro:bits!

This is how we play this game:
1. We have a set of micro:bits set up as senders 📡 hidden somewhere.
    - These devices are set up by the game organisers before we start.
    - We tell you the number of devices you need to find.
2. You have to build a receiver 📶 to look for the devices.
    - Scroll down to the [`Receiver 📶`](#receiver-) section for pointers.
3. Take a picture of the sender 📡 beacon showing that you have accomplished your task.
    - The [`Sender 📡`](#sender-) beacon will typically have the green lights on for 5 seconds or display "OK" or another icon. 
    - Please note that not all sender beacons have the green lights mounted. Use a receiver to look for them.
    - Make sure you are looking for the senders by scanning for packages on the right channel.

## Setup 🛠
We are using:
* micro:bit ([homepage](https://microbit.org/))
* DFRobot micro:bit Circular RGB Expansion board v2.0 ([docs](https://wiki.dfrobot.com/Micro_bit_Circular_RGB_LED_Expansion_Board_SKU__ROB0150))

## Getting Started
* _(optional)_ Unpack the micro:bit.
* _(optional)_ Assemble the DFRobot micro:bit Circular RGB Expansion board v2.0.
* Get acquainted with [Treasure Hunt](https://microbit.org/projects/make-it-code-it/treasure-hunt/) code for pointers for your receiver. This is not the same code we are using on our sending beacons, but it is inspired by it.

## Sender 📡
1. There are several sending beacons hidden somewhere around you. 
2. Ask organisers how many beacons are hidden out there.
3. All beacons are broadcasting a message on one of the channels between 1 and 7. Assume this unless you are told otherwise.

## Receiver 📶
You need to implement a set of basic functions on your receiver beacon (in addition to functions that you might be told by the sender beacon you might find).

Pseudocode for the receiver beacon:
1. Scan for packages on channel X (typically 1 to 7) and show signal strength.
2. If the signal strength is larger than `-65` print the message that is being transmitted on your micro:bit.
3. The message you receive will tell you what to do.
4. Locate the sending beacon (yes, physically find it!) and do what you have been told in the previous step.
    - It can be something you need to do on the sending beacon.
    - It can be something you need to code on your receiver.

## Bugs?
Bugs happen. Let us know if you encounter a bug or have a feature request, by creating an [issue](https://github.com/mehmandarov/microbit-treasurehunt/issues) or submitting a [PR](https://github.com/mehmandarov/microbit-treasurehunt/pulls). 🙌

## Found them all?
If you want to continue playing with Micro:bits, you may create your own sender to add to future treasure hunts. You are also welcome to submit ideas for new senders without implementing them yourself. 
