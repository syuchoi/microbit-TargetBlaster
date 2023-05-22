# microbit-TargetBlaster
This project is hard block-coded.

That means hardcoded + blockcoded.

It just means we worked very hard on it.

## How to play
This is a game of hitting the bullseye.

You start with 3 lives, and the goal of the game is to survive as long as possible and get a high score by aiming and firing at the center of a cross-shaped bullseye with a gun the size of a single LED.

Pressing the A button starts the game after a 3-second countdown.

The gun is aimed (moved) with the joystick and fired with the joystick button (P2) or A or B.

If you hit the bullseye, which spawns in a random location, you score a point, and if you miss, you lose 1 life.
You also lose 1 life if you don't hit it within 5 seconds.

Each time you hit the bullseye in a row, your combo stacks up, and you gain 1 life for every 5 consecutive hits.

If you lose a life, your combo is reset as well.

As a difficulty adjustment, the time limit to hit the bullseye is shortened by 1 second for every 10 points.

We don't know if this is possible, but just in case, if the time limit is 1 second, it will be reduced by 0.1 seconds after that, and if it is 0.1 seconds, we will start dividing the time limit in half.

When you lose all your lives, the game ends.

Start over from the beginning with the A+B buttons.

We were originally going to have a different animation as the opening when microbit is first turned on, but it kept giving us a capacity exceeded error, so we were forced to replace it with a simple string output.
