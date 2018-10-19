'''
circuitpython-badge/minimal_examples/pixfade.py

Some animations using loops to fade all the leds on the badge :D

Aidan T 2018
'''

import badge

badge.init()

p = badge.Pix()

def fadeinout():
    # f is the current step brightness and x/y to set LED in the grid:
    for f in range(10):
        for x in range(p.width):
            for y in range(p.height):
                p.pixel(x, y, f)
        badge.show(p)
        badge.tick(0.01)

    for f in range(10):
        for x in range(p.width):
            for y in range(p.height):
                p.pixel(x, y, 9-f)
        badge.show(p)
        badge.tick(0.01)

# if you want to fade in and out once:

# fadeinout()

# If you want to run the fade in a loop, uncomment the lines below:

# while True:
#     fadeinout()

# Alternatively import pixfade and use pixfade.fadeinout()

# Fade in and out with alternate horizontal bars
def alternate():
    # f is the current step brightness and x/y to set LED in the grid:
        # % modulo is used to alternate lines
    for f in range(10):
        for x in range(p.width):
            for y in range(p.height):
                if y%2 == 0:
                    p.pixel(x, y, f)
                else:
                    p.pixel(x, y, 9-f)
        badge.show(p)
        badge.tick(0.01)

    for f in range(10):
        for x in range(p.width):
            for y in range(p.height):
                if y%2 == 0:
                    p.pixel(x, y, 9-f)
                else:
                    p.pixel(x, y, f)
        badge.show(p)
        badge.tick(0.01)

# if you want to alternate once:

# alternate()

# If you want to alternate forever, uncomment the lines below:

# while True:
#     alternate()

# Alternatively import pixfade and use pixfade.fadeinout()

# Make a crazy burning arrow thing
def arrow():
    # Clear the screen before the animation:
    for x in range(p.width):
        for y in range(p.height):
            p.pixel(x,y,0)
    badge.show(p)

    # i is the length of the animation, 2 x screen width
    for i in range(p.width*2):
        # Draw the middle vertical pixel, move horizontally with i
        p.pixel(i, int(p.height/2), p.width)
        for f in range(i):
            # make a trail:
            if (p.width-1)-f > -1:
                b = (p.width-1)-f # b is for brightness
            p.pixel((i-f)-1, int(p.height/2), b)
        
        # Now make the wings of the arrow which dim as they spread:
        for n in range(i):
            if n < int(p.height/2):
                ab = p.width-(n*3) # ab is arrow wing brightness
                p.pixel(((i-n)-1), (int(p.height/2)+(n+1)), ab) # upper wing
                p.pixel(((i-n)-1), (int(p.height/2)-(n+1)), ab) # lower wing
                for z in range(i):
                    # Make the arrow trails:
                    if (ab-1)-z > -1:
                        atb = (ab-1)-z
                        p.pixel((((i-n)-z)-1), (int(p.height/2)+(n+1)), atb)
                        p.pixel((((i-n)-z)-1), (int(p.height/2)-(n+1)), atb)

        badge.show(p)
        badge.tick(0.01)

# To make one arrow:

# arrow()

# To loop arrows:

# while True:
#    arrow()
