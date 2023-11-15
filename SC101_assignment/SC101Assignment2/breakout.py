"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE:
You have 3 lives to play the classic game: Break the Brick
Try your best to get 100 scores!! Fighting!!
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    heart = NUM_LIVES
    scores = 0
    win_condition = graphics.max_scores()

    # Add the animation loop here!
    while True:
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        # update
        while graphics.is_moving:
            pause(FRAME_RATE)
            graphics.ball.move(vx, vy)
        # check paddle or brick
            if graphics.check_paddle():
                if vy > 0:
                    vy = -vy
            elif graphics.check_brick():
                if vy < 0 or vy > 0:
                    vy = -vy
                    scores += 1
                    if scores == win_condition:
                        graphics.win()
                        break
        # check the edges of the window
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                vx = -vx
            elif graphics.ball.y <= 0:
                vy = -vy
            elif graphics.ball.y - graphics.ball.height >= graphics.window.height:
                heart -= 1
                graphics.lives_board.text = 'lives: '+'★'*heart
                graphics.reset()
                vx = graphics.get_dx()
                vy = graphics.get_dy()
        if heart == 0:
            graphics.game_over()
            break
        if scores == win_condition:
            break
        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
