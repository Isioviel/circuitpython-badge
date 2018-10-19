import badge

badge.init()

LEFT_BUTTONS = {
    badge.K_UP: (0, -1),  # UP
    badge.K_DOWN: (0, 1),  # DOWN
    badge.K_LEFT: (-1, 0),  # LEFT
    badge.K_RIGHT: (1, 0),  # RIGHT
}

RIGHT_BUTTONS = {
    badge.K_S: (0, -1),  # UP
    badge.K_X: (0, 1),  # DOWN
    badge.K_Z: (-1, 0),  # LEFT
    badge.K_O: (1, 0),  # RIGHT
}

left_pos = [3, 3]
right_pos = [10, 7]

screen = badge.Pix()
screen.pixel(3, 3, 10)
screen.pixel(10, 7, 10)
badge.show(screen)


while True:
    badge.tick(0.2)
    keys_pressed = badge.keys()

    for button, direction in LEFT_BUTTONS.items():
        if button & keys_pressed:
            left_pos[0] = (left_pos[0] + direction[0]) % screen.width
            left_pos[1] = (left_pos[1] + direction[1]) % screen.height

    for button, direction in RIGHT_BUTTONS.items():
        if button & keys_pressed:
            right_pos[0] = (right_pos[0] + direction[0]) % screen.width
            right_pos[1] = (right_pos[1] + direction[1]) % screen.height

    screen = badge.Pix()
    screen.pixel(left_pos[0], left_pos[1], 10)
    screen.pixel(right_pos[0], right_pos[1], 10)
    badge.show(screen)
