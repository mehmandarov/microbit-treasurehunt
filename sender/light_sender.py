radio.set_group(4)
radio.set_transmit_power(2)
strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))

def on_forever():
    if input.light_level() > 150:
        basic.show_leds("""
            # . # . #
                        . . . . .
                        . . . . .
                        # # . # #
                        . # . # .
        """)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        strip.set_brightness(50)
        basic.pause(5000)
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        basic.clear_screen()
basic.forever(on_forever)

def on_forever2():
    radio.send_string("IT IS A BIT DARK IN HERE")
    basic.pause(200)
basic.forever(on_forever2)
