import badge
import randompix

while True:
    for i in range(40):
        randompix.randomfuzz(i)
        badge.tick(0.1)

    for i in range(40):
        randompix.randomfuzz(40-i)
        badge.tick(0.1)

    for i in range(30):
	randompix.randombar()

    for i in range(30):
	randompix.randomdrops()
