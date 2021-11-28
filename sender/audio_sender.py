def on_button_pressed_a():
    global strip, snd_lvl
    strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.show_string("CLAP")
    while input.sound_level() < 180:
        snd_lvl = Math.round(input.sound_level() * (24 / 180))
        strip = neopixel.create(DigitalPin.P2, snd_lvl, NeoPixelMode.RGB)
        strip.set_brightness(50)
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        basic.pause(100)
    strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.show_leds("""
        . . . . .
                . # . # .
                . . # . .
                # . . . #
                . # # # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

snd_lvl = 0
strip: neopixel.Strip = None
strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
radio.set_group(1)
radio.set_transmit_power(2)

def on_forever():
    radio.send_string("PRESS A")
    basic.pause(200)
basic.forever(on_forever)
