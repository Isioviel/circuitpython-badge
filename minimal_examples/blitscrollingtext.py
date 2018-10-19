import badge

badge.init()

text = badge.Pix.from_text('Hello badge!')

screen = badge.Pix()

# Start the text just off the right side of the screen
x_pos = screen.width

while True:
    badge.tick(0.2)

    # Move the text a little further to the left, until it's completely off
    # the screen
    x_pos -= 1
    if x_pos < -text.width:
        x_pos = screen.width

    # ...and draw the text block position 3 pixels below the top of screen,
    # and starting at the current x_pos
    # (blit draws the specified image in the given position on the screen)
    screen.blit(text, x_pos, 3)

    badge.show(screen)
