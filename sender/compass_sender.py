def init_game():
    reset_LED_ring()

def reset_LED_ring():
    global strip
    strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))

def set_LED_green():
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.show_icon(IconNames.STICK_FIGURE)

def on_forever():
    start_transmission()
    global bearing
    bearing = input.compass_heading()

    if bearing < 45 or bearing > 315:
        basic.show_string("N")
        set_LED_green()
        basic.pause(5000)
        init_game()
    else:
        basic.show_string("*")

def start_transmission():
    radio.set_group(5)
    radio.set_transmit_power(2)
    
    # basic.show_string("GO NORTH! Nah, just kidding. Just point me to the north and we are good.")
    radio.send_string("GO NORTH!")
    basic.pause(200)

bearing = 0
strip: neopixel.Strip = None
init_game()
basic.forever(on_forever)
