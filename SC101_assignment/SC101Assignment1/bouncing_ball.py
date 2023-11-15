"""
File: 
Name: Jim(2 hours)
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.8
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
is_falling = False
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = 'navy'
    window.add(ball)
    onmouseclicked(start_or_not)
    while True:
        if is_falling:
            if count < 3:
                bouncing()
        pause(DELAY)


def start_or_not(event):
    global is_falling

    if not is_falling:
        is_falling = True

        
def bouncing():
    vy = 0
    while True:
        ball.move(VX, vy)
        vy += GRAVITY
        if ball.y+ball.height > window.height:
            vy *= -REDUCE
        if ball.x > window.width:
            reset_ball()
            break
        pause(DELAY)


def reset_ball():
    global is_falling, count

    window.remove(ball)
    ball.x = START_X
    ball.y = START_Y
    window.add(ball)
    is_falling = False
    count += 1


if __name__ == "__main__":
    main()
