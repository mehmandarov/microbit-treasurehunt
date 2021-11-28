def start_transmission():
    radio.set_group(6)
    radio.set_transmit_power(2)
    radio.send_string("Touch me!")
    basic.pause(200)
def init_game():
    reset_LED_ring()
def reset_LED_ring():
    global strip
    strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))

def on_logo_pressed():
    set_LED_green()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def set_LED_green():
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    basic.show_icon(IconNames.GIRAFFE)
strip: neopixel.Strip = None
bearing = 0
init_game()

def on_forever():
    start_transmission()
basic.forever(on_forever)
