def spawnTarget():
    global randX, randY, target, elapsedTarget, elapsed
    if targetLife > 1000:
        randX = randint(0, 4)
        randY = randint(0, 4)
    else:
        if gun.get(LedSpriteProperty.X) == 4:
            randX = gun.get(LedSpriteProperty.X) + randint(-1, 0)
        elif gun.get(LedSpriteProperty.X) == 0:
            randX = gun.get(LedSpriteProperty.X) + randint(0, 1)
        else:
            randX = gun.get(LedSpriteProperty.X) + randint(-1, 1)
        if gun.get(LedSpriteProperty.Y) == 4:
            randY = gun.get(LedSpriteProperty.Y) + randint(-1, 0)
        elif gun.get(LedSpriteProperty.X) == 0:
            randY = gun.get(LedSpriteProperty.Y) + randint(0, 1)
        else:
            randY = gun.get(LedSpriteProperty.Y) + randint(-1, 1)
    target = [game.create_sprite(randX, randY - 1),
        game.create_sprite(randX - 1, randY),
        game.create_sprite(randX + 1, randY),
        game.create_sprite(randX, randY + 1)]
    if randY - 1 == -1:
        target[0].delete()
    if randX - 1 == -1:
        target[1].delete()
    if randX + 1 == 5:
        target[2].delete()
    if randY + 1 == 5:
        target[3].delete()
    elapsedTarget = 0
    elapsed = input.running_time()

def on_button_pressed_a():
    global startPushed, gameStart, combo, gun, targetLife
    startPushed = True
    if not (gameStart):
        for index in range(3):
            basic.clear_screen()
            music.play_tone(880, music.beat(BeatFraction.QUARTER))
            basic.show_number(3 - index)
            basic.pause(280)
        gameStart = True
        combo = 0
        gun = game.create_sprite(0, 0)
        targetLife = 5000
        spawnTarget()
input.on_button_pressed(Button.A, on_button_pressed_a)

def judgePlayer(bool2: bool):
    global combo, targetLife
    if bool2:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                1,
                1980,
                255,
                0,
                300,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.IN_BACKGROUND)
        game.add_score(1)
        combo += 1
        if combo != 0 and combo % 5 == 0:
            music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                    2559,
                    3674,
                    255,
                    0,
                    300,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.IN_BACKGROUND)
            game.add_life(1)
        if game.score() != 0 and game.score() % 10 == 0:
            music.play_tone(587, music.beat(BeatFraction.EIGHTH))
            music.play_tone(622, music.beat(BeatFraction.EIGHTH))
            music.play_tone(659, music.beat(BeatFraction.EIGHTH))
            if targetLife <= 1000:
                targetLife += -100
            elif targetLife <= 100:
                targetLife += targetLife / 2
            else:
                targetLife += -1000
    else:
        music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                286,
                1,
                255,
                0,
                300,
                SoundExpressionEffect.NONE,
                InterpolationCurve.CURVE),
            SoundExpressionPlayMode.IN_BACKGROUND)
        game.remove_life(1)
        combo = 0
    for 값 in target:
        값.delete()
    spawnTarget()
# reset for emulator

def on_button_pressed_ab():
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

combo = 0
elapsed = 0
elapsedTarget = 0
target: List[game.LedSprite] = []
gun: game.LedSprite = None
randY = 0
randX = 0
targetLife = 0
startPushed = False
gameStart = False
gameStart = False
startPushed = False
joystickReset = [pins.analog_read_pin(AnalogPin.P1),
    pins.analog_read_pin(AnalogPin.P0)]
game.set_life(3)
basic.show_string("Target Blaster!!")

def on_forever():
    global gameStart
    if game.is_game_over():
        if gameStart:
            gameStart = False
            music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                    2559,
                    1,
                    255,
                    0,
                    1000,
                    SoundExpressionEffect.TREMOLO,
                    InterpolationCurve.LOGARITHMIC),
                SoundExpressionPlayMode.UNTIL_DONE)
    if gameStart:
        gun.set(LedSpriteProperty.BRIGHTNESS, 255)
        basic.pause(500)
        gun.set(LedSpriteProperty.BRIGHTNESS, 50)
        basic.pause(500)
basic.forever(on_forever)

def on_forever2():
    global elapsedTarget
    if gameStart:
        elapsedTarget = input.running_time() - elapsed
        # shoot
        if pins.digital_read_pin(DigitalPin.P2) == 1 or input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            music.play_sound_effect(music.create_sound_effect(WaveShape.SQUARE,
                    1600,
                    1,
                    255,
                    0,
                    300,
                    SoundExpressionEffect.NONE,
                    InterpolationCurve.CURVE),
                SoundExpressionPlayMode.IN_BACKGROUND)
            if gun.get(LedSpriteProperty.X) == randX and gun.get(LedSpriteProperty.Y) == randY:
                judgePlayer(True)
            else:
                judgePlayer(False)
        if elapsedTarget >= targetLife:
            judgePlayer(False)
basic.forever(on_forever2)

def on_forever3():
    if gameStart:
        if pins.analog_read_pin(AnalogPin.P1) > joystickReset[0] + 100:
            gun.change(LedSpriteProperty.X, 1)
        elif pins.analog_read_pin(AnalogPin.P1) < joystickReset[0] - 100:
            gun.change(LedSpriteProperty.X, -1)
        if pins.analog_read_pin(AnalogPin.P0) > joystickReset[1] + 100:
            gun.change(LedSpriteProperty.Y, 1)
        elif pins.analog_read_pin(AnalogPin.P0) < joystickReset[1] - 100:
            gun.change(LedSpriteProperty.Y, -1)
        basic.pause(200)
basic.forever(on_forever3)
