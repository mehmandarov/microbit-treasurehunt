
def on_button_pressed_a():
    radio.send_string("DUCK")

def on_button_pressed_b():
    global received_string
    my_list = received_string.upper().split()
    my_list.sort()
    sorted_string = "".join(my_list)
    radio.send_string(sorted_string)

def on_received_string(received):
    global signal, received_string
    received_string = received
    signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    LED.rotate(1)
    LED.show()
    # basic.pause(50)
    if signal > -70:
        basic.show_string(received_string)
    else:
        led.plot_bar_graph(Math.map(signal, -128, -42, 0, 9), 9)

def led_init():
    global LED
    LED = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
    LED.clear()
    LED.range(0, 3).show_color(neopixel.colors(NeoPixelColors.ORANGE))
    LED.set_brightness(10)


# Fire events:
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
radio.on_received_string(on_received_string)

signal = 0
received_string = ""
LED: neopixel.Strip = None

led_init()
radio.set_group(7)
