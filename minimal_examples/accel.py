import badge
import time


def cls():
    for x in range(screen.width):
        for y in range(screen.height):
            screen.pixel(x, y, 0)
    badge.show(screen)


def update(xold, yold, xnew, ynew, bright):
    # set the old pixel to dark
    screen.pixel(xold, yold, 0)
    # and the new one to light
    screen.pixel(xnew, ynew, 10)
    badge.show(screen)

# main below here

xpos = 7
ypos = 5
xnew = xpos
ynew = ypos

badge.init()
screen = badge.Pix()
cls()
screen.pixel(xpos, ypos, 10)
badge.show(screen)


while True:
    a = badge.accel()
    print(a)
    if a[0] > 500:
        xnew = xpos - 1
        if xnew <= 0:
            xnew = 0
    elif a[0] < -500:
        xnew = xpos + 1
        if xnew >= screen.width:
            xnew = screen.width - 1
    if a[1] < -500:
        ynew = ypos - 1
        if ynew <= 0:
            ynew = 0
    elif a[1] > 500:
        ynew = ypos + 1
        if ynew >= screen.height:
            ynew = screen.height - 1

    update(xpos, ypos, xnew, ynew, 10)
    xpos = xnew
    ypos = ynew
    time.sleep(0.5)
