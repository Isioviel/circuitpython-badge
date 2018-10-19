import badge
import random

texts = [
    "Hello world!",
    "Kill all humans!",
    "Resistance is futile.",
    "You will be assimilated.",
]

badge.init()
text = badge.Pix.from_text("Kill all humans!")
screen = badge.Pix()
for y in range(11):
    for x in range(14):
        screen.pixel(x, y, int(abs(x-7 + y-3.5) * 2))
tx = 14
badge.show(screen)
badge.brightness(0)
screen.box(0, 0, 2, 14, 7)
while True:
    screen.blit(text, tx, 3)
    tx -= 1
    if tx < -text.width:
        tx = 14
        text = badge.Pix.from_text(random.choice(texts))
    badge.show(screen)
    badge.tick(1/12)
