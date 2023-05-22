function spawnTarget () {
    if (targetLife > 1000) {
        randX = randint(0, 4)
        randY = randint(0, 4)
    } else {
        if (gun.get(LedSpriteProperty.X) == 4) {
            randX = gun.get(LedSpriteProperty.X) + randint(-1, 0)
        } else if (gun.get(LedSpriteProperty.X) == 0) {
            randX = gun.get(LedSpriteProperty.X) + randint(0, 1)
        } else {
            randX = gun.get(LedSpriteProperty.X) + randint(-1, 1)
        }
        if (gun.get(LedSpriteProperty.Y) == 4) {
            randY = gun.get(LedSpriteProperty.Y) + randint(-1, 0)
        } else if (gun.get(LedSpriteProperty.X) == 0) {
            randY = gun.get(LedSpriteProperty.Y) + randint(0, 1)
        } else {
            randY = gun.get(LedSpriteProperty.Y) + randint(-1, 1)
        }
    }
    target = [
    game.createSprite(randX, randY - 1),
    game.createSprite(randX - 1, randY),
    game.createSprite(randX + 1, randY),
    game.createSprite(randX, randY + 1)
    ]
    if (randY - 1 == -1) {
        target[0].delete()
    }
    if (randX - 1 == -1) {
        target[1].delete()
    }
    if (randX + 1 == 5) {
        target[2].delete()
    }
    if (randY + 1 == 5) {
        target[3].delete()
    }
    elapsedTarget = 0
    elapsed = input.runningTime()
}
input.onButtonPressed(Button.A, function () {
    startPushed = true
    if (!(gameStart)) {
        for (let index = 0; index <= 2; index++) {
            basic.clearScreen()
            music.playTone(880, music.beat(BeatFraction.Quarter))
            basic.showNumber(3 - index)
            basic.pause(280)
        }
        gameStart = true
        combo = 0
        gun = game.createSprite(0, 0)
        targetLife = 5000
        spawnTarget()
    }
})
function judgePlayer (bool: boolean) {
    if (bool) {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 1, 1980, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.InBackground)
        game.addScore(1)
        combo += 1
        if (combo != 0 && combo % 5 == 0) {
            music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 2559, 3674, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.InBackground)
            game.addLife(1)
        }
        if (game.score() != 0 && game.score() % 10 == 0) {
            music.playTone(587, music.beat(BeatFraction.Eighth))
            music.playTone(622, music.beat(BeatFraction.Eighth))
            music.playTone(659, music.beat(BeatFraction.Eighth))
            if (targetLife <= 1000) {
                targetLife += -100
            } else if (targetLife <= 100) {
                targetLife += targetLife / 2
            } else {
                targetLife += -1000
            }
        }
    } else {
        music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 286, 1, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.InBackground)
        game.removeLife(1)
        combo = 0
    }
    for (let 값 of target) {
        값.delete()
    }
    spawnTarget()
}
// reset for emulator
input.onButtonPressed(Button.AB, function () {
    control.reset()
})
let combo = 0
let elapsed = 0
let elapsedTarget = 0
let target: game.LedSprite[] = []
let gun: game.LedSprite = null
let randY = 0
let randX = 0
let targetLife = 0
let startPushed = false
let gameStart = false
gameStart = false
startPushed = false
let joystickReset = [pins.analogReadPin(AnalogPin.P1), pins.analogReadPin(AnalogPin.P0)]
game.setLife(3)
basic.showString("Target Blaster!!")
basic.forever(function () {
    if (game.isGameOver()) {
        if (gameStart) {
            gameStart = false
            music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 2559, 1, 255, 0, 1000, SoundExpressionEffect.Tremolo, InterpolationCurve.Logarithmic), SoundExpressionPlayMode.UntilDone)
        }
    }
    if (gameStart) {
        gun.set(LedSpriteProperty.Brightness, 255)
        basic.pause(500)
        gun.set(LedSpriteProperty.Brightness, 50)
        basic.pause(500)
    }
})
basic.forever(function () {
    if (gameStart) {
        elapsedTarget = input.runningTime() - elapsed
        // shoot
        if (pins.digitalReadPin(DigitalPin.P2) == 1 || input.buttonIsPressed(Button.A) || input.buttonIsPressed(Button.B)) {
            music.playSoundEffect(music.createSoundEffect(WaveShape.Square, 1600, 1, 255, 0, 300, SoundExpressionEffect.None, InterpolationCurve.Curve), SoundExpressionPlayMode.InBackground)
            if (gun.get(LedSpriteProperty.X) == randX && gun.get(LedSpriteProperty.Y) == randY) {
                judgePlayer(true)
            } else {
                judgePlayer(false)
            }
        }
        if (elapsedTarget >= targetLife) {
            judgePlayer(false)
        }
    }
})
basic.forever(function () {
    if (gameStart) {
        if (pins.analogReadPin(AnalogPin.P1) > joystickReset[0] + 100) {
            gun.change(LedSpriteProperty.X, 1)
        } else if (pins.analogReadPin(AnalogPin.P1) < joystickReset[0] - 100) {
            gun.change(LedSpriteProperty.X, -1)
        }
        if (pins.analogReadPin(AnalogPin.P0) > joystickReset[1] + 100) {
            gun.change(LedSpriteProperty.Y, 1)
        } else if (pins.analogReadPin(AnalogPin.P0) < joystickReset[1] - 100) {
            gun.change(LedSpriteProperty.Y, -1)
        }
        basic.pause(200)
    }
})
