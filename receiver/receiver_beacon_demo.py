def on_button_pressed_a():
    radio.send_string("DUCK")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global signal
    signal = radio.received_packet(RadioPacketProperty.SIGNAL_STRENGTH)
    LED.rotate(1)
    LED.show()
    # basic.pause(50)
    if signal > -70:
        basic.show_string(receivedString)
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
