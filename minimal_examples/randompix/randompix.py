'''
circuitpython-badge/minimal_examples/randompix.py

A selection of random infested animations

Aidan T 2018
'''

import badge
from random import randint

badge.init()

p = badge.Pix()

# randomfuzz - Generate n random positioned/brightness pixels
def randomfuzz(density):
    # clear the screen
    for x in range(p.width):
        for y in range(p.height):
            p.pixel(x,y,0)

    badge.show(p)

    # Generate (n) randomly positioned pixels
    for i in range(density):
        rx = randint(0, p.width)
        ry = randint(0, p.height)
        rb = randint(0, 16)
        p.pixel(rx,ry,rb)

    badge.show(p)

# if you want to generate 10 random pixels once:

#randomfuzz(10)

# if you would like a loop, comment out the lines below:

# while True:
#     randomfuzz(10)
#     badge.tick(0.1)

# randombar - generate a random horizontal fading bar
def randombar():
    # clear the screen
    for x in range(p.width):
        for y in range(p.height):
            p.pixel(x,y,0)

    badge.show(p)

    # store a random number for the next bar position
    bar = randint(0, (p.height-1))

    # Generate a random bar and fade over time
    for i in range(17):
        for x in range(p.width):
            p.pixel(x, bar, (16-i))

        badge.show(p)
        badge.tick(0.01)

# If you want to generate 1 random bar:

#randombar()

# If you want to loop, comment out the lines below:

# while True:
#    randombar()

def randomdrops():
    # clear the screen
    for x in range(p.width):
        for y in range(p.height):
            p.pixel(x,y,0)

    badge.show(p)

    # store a random number for the next drop position
    drops = randint(0, (p.width-1))

    # Generate a random drop
    for i in range(p.height+1):
        p.pixel(drops, i, (i+1))
        p.pixel(drops, (i-1), 0)
        badge.show(p)
        badge.tick(0.01)

# If you want to generate 1 random drop:

#randomdrop()

# If you want a loop, comment out the lines below:

# while True:
#    randomdrop()
