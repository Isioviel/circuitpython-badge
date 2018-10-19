import badge

badge.init()

screen = badge.Pix()
screen.pixel(3, 3, 10)
screen.pixel(10, 7, 10)
badge.show(screen)
