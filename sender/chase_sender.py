def newRound():
    target.set(LedSpriteProperty.X, randint(0, 4))
    target.set(LedSpriteProperty.Y, randint(0, 4))
    if not (target.is_touching_edge()):
        newRound()

def on_gesture_shake():
    global score, chaser, target, strip
    soundExpression.slide.play()
    score = 0
    chaser = game.create_sprite(2, 2)
    target = game.create_sprite(2, 2)
    target.set(LedSpriteProperty.BLINK, 3)
    target.set(LedSpriteProperty.BRIGHTNESS, 4)
    newRound()
    playgame()
    chaser.delete()
    target.delete()
    soundExpression.happy.play()
    strip = neopixel.create(DigitalPin.P2, 24, NeoPixelMode.RGB)
    strip.set_brightness(50)
    strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
    for index in range(10):
        basic.show_icon(IconNames.HEART)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def playgame():
    global score
    while score < 5:
        if input.is_gesture(Gesture.TILT_LEFT):
            chaser.change(LedSpriteProperty.X, -1)
        elif input.is_gesture(Gesture.TILT_RIGHT):
            chaser.change(LedSpriteProperty.X, 1)
        elif input.is_gesture(Gesture.LOGO_DOWN):
            chaser.change(LedSpriteProperty.Y, -1)
        elif input.is_gesture(Gesture.LOGO_UP):
            chaser.change(LedSpriteProperty.Y, 1)
        basic.pause(100)
        if chaser.is_touching(target):
            score += 1
            if score < 5:
                newRound()
strip: neopixel.Strip = None
chaser: game.LedSprite = None
score = 0
target: game.LedSprite = None
radio.set_group(3)
radio.set_transmit_power(2)

def on_forever():
    radio.send_string("SHAKE ME")
    basic.pause(100)
basic.forever(on_forever)
