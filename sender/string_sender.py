import neopixel

def on_button_pressed_b():
    global state
    state = "show_puzzle"

def on_button_pressed_ab():
    global state 
    state = "puzzle"

def on_received_string(receivedString):
    global signal, strip, string_to_sort, state
    signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    if signal > -55:
        my_list= string_to_sort.upper().split()
        my_list.sort()
        sorted_string = "".join(my_list)
        if receivedString == sorted_string:
            basic.show_icon(IconNames.YES)
            strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
            strip.set_brightness(50)
            strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    else:
        basic.show_string("COME CLOSER")
    basic.pause(5000)
    state = "broadcast"
    strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    basic.show_leds("""
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    . . . . .
                    """)

def on_forever():
    if state == "broadcast":
        radio.send_string("PRESS B")
    elif state == "show_puzzle":
        basic.show_string("SORT & UPPERCASE.")
        basic.show_string("GET STR: PRESS A+B")
    else:
        radio.send_string(string_to_sort)
    basic.pause(100)

def get_random_string():
    strings = ["x8xsabmhhp9nq7326n49",
               "ry45druin3nzalahnfk4",
               "0urk98atrglbwpbidgr2",
               "74q9i2z9ghazyog8tdnj",
               "j948w6vxhzv2frelyhth",
               "gw8fyp7s64b9udpxs21x",
               "aqfswdonsf5p38108kb8",
               "qu4yeyi430gyjburnz4g",
               "pt59553sa5n68if49c7j",
               "17kzyide81t97euc0si5" ]
    return strings[randint(0, strings.length)]

basic.forever(on_forever)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
input.on_button_pressed(Button.B, on_button_pressed_b)
radio.on_received_string(on_received_string)

strip: neopixel.Strip = None
signal = 0
radio.set_group(7)
radio.set_transmit_power(2)
state = "broadcast" # Possible states: broadcast, puzzle
string_to_sort = get_random_string()
