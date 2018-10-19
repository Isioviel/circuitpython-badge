import badge
import gc

badge.init()

# Please note, Sylons are distinct from robots in popular sci-fi series

sylon_going_right = badge.Pix(6, 2)
for row in (0, 1):
    sylon_going_right.pixel(5, row, 16)
    sylon_going_right.pixel(4, row, 16)
    sylon_going_right.pixel(3, row, 12)
    sylon_going_right.pixel(2, row, 8)
    sylon_going_right.pixel(1, row, 4)
    sylon_going_right.pixel(0, row, 2)

sylon_going_left = badge.Pix(6, 2)
for row in (0, 1):
    sylon_going_left.pixel(0, row, 16)
    sylon_going_left.pixel(1, row, 16)
    sylon_going_left.pixel(2, row, 12)
    sylon_going_left.pixel(3, row, 8)
    sylon_going_left.pixel(4, row, 4)
    sylon_going_left.pixel(5, row, 2)

ZOOP = [
    sylon_going_right,
    sylon_going_left,
]

screen = badge.Pix()

# Start the zoop just off the right side of the screen
x_pos = -5

zoop_direction = 0

while True:
    badge.tick(0.05)

    # Move the text a little further to the left, until it's completely off
    # the screen
    if zoop_direction == 0:
        x_pos += 1
        if x_pos > screen.width - 6:
            # Change direction, positionining the zoop prettily
            x_pos = screen.width - 3
            zoop_direction = 1
            # If we don't do this, the GC is sometimes too slow to collect
            # and leads to us running dangerously in/close to MemoryErrors
            gc.collect()
    else:
        x_pos -= 1
        if x_pos < 1:
            # Change direction, positioning the zoop prettily
            x_pos = -4
            zoop_direction = 0

    # ...and draw the text block position 3 pixels below the top of screen,
    # and starting at the current x_pos
    # (blit draws the specified image in the given position on the screen)
    screen.blit(ZOOP[zoop_direction], x_pos, 5)

    badge.show(screen)
