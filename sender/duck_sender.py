def on_received_string(receivedString):
    global signal, strip
    signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    if signal > -55:
        if receivedString == "DUCK":
            basic.show_icon(IconNames.DUCK)
            strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
            strip.set_brightness(50)
            strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    else:
        basic.show_string("COME CLOSER")
    basic.pause(5000)
    strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
    """)
radio.on_received_string(on_received_string)

strip: neopixel.Strip = None
signal = 0
radio.set_group(2)
radio.set_transmit_power(2)

def on_forever():
    radio.send_string("SEND ME \"DUCK\"")
    basic.pause(100)
basic.forever(on_forever)
