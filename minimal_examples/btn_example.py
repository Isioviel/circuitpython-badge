import board
import digitalio
import time


# Initialize button Z
btn_z = digitalio.DigitalInOut(board.Z, direction=digitalio.Direction.INPUT)
# the previous line works the same if you choose any other button from board
# as board.S, board.Z, board.O, board.X
# or board.UP, board.LEFT, board.RIGHT, board.DOWN
btn_z.pull = digitalio.Pull.UP

while True:

    # pressed button will have a value of False
    # while unpressed button will have a value of True
    if btn_z.value is False:
        print('button Z was pressed')

    time.sleep(.2)
