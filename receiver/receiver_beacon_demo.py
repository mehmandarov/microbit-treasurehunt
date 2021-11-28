
def on_received_string(receivedString):
    global signal
    signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    LED.rotate(1)
    LED.show()
    # basic.pause(50)
    if signal > -50:
        basic.show_string("" + str(signal))
    else:
        # basic.show_string(receivedString)
        led.plot_bar_graph(Math.map(signal, -128, -42, 0, 9), 9)
radio.on_received_string(on_received_string)

signal = 0
LED: neopixel.Strip = None
LED = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
LED.clear()
LED.range(0, 3).show_color(neopixel.colors(NeoPixelColors.ORANGE))
LED.set_brightness(10)
radio.set_group(1)
# basic.pause(50)
