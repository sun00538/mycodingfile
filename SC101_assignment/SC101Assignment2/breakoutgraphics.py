"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
The classic game: Break the Brick, define the initial parameter here, including window size and number of bricks etc.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 10    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
NUM_LIVES = 3			# Number of attempts


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.p_f = paddle_offset
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)//2,
                        y=self.window.height-self.p_f)
        onmousemoved(self.horizontal_move)

        # Center a filled ball in the graphical window
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)//2,
                        y=(self.window.height-self.ball.height)//2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.is_moving = False
        onmouseclicked(self.start)

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(width=brick_width, height=brick_height)
                self.brick.filled = True
                self.brick.color = 'black'
                if i < 2:
                    self.brick.fill_color = 'red'
                elif 1 < i < 4:
                    self.brick.fill_color = 'orange'
                elif 3 < i < 6:
                    self.brick.fill_color = 'yellow'
                elif 5 < i < 8:
                    self.brick.fill_color = 'green'
                elif 7 < i < 10:
                    self.brick.fill_color = 'blue'
                self.brick.x = j*(brick_width+brick_spacing)
                self.brick.y = i*(brick_height+brick_spacing)+BRICK_OFFSET
                self.window.add(self.brick)

        # Score label
        self.n = 0
        self.label = GLabel(f'Scores: {self.n}', x=0, y=30)
        self.label.font = 'Comic Sans MS-20'
        self.label.color = 'navy'
        self.window.add(self.label)

        # hearts sign
        self.lives_board = GLabel('lives: '+'★'*NUM_LIVES, x=self.brick.width*4, y=self.window.height)
        self.lives_board.font = 'Comic Sans MS-15'
        self.window.add(self.lives_board)

    def horizontal_move(self, mouse):
        """
        Keep paddle move horizontally by mouse.
        """
        if mouse.x+self.paddle.width//2 >= self.window.width:
            self.paddle.x = self.window.width-self.paddle.width
        elif mouse.x-self.paddle.width//2 <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x-self.paddle.width//2
            self.paddle.y = self.window.height-self.p_f

    def start(self, mouse):
        """
        Define the original speed of ball,
        and make sure the ball is not affected by mouseclick when the ball is moving.
        """
        if not self.is_moving:
            self.is_moving = True
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_dx(self):
        """
        Return the horizontal velocity of the ball when start or reset.
        """
        return self.__dx

    def get_dy(self):
        """
        Return the vertical velocity of the ball when start or reset.
        """
        return self.__dy

    def reset(self):
        """
        When the ball is out of the edge, restart the ball.
        """
        self.window.remove(self.ball)
        self.window.add(self.ball, x=(self.window.width - self.ball.width) // 2,
                        y=(self.window.height - self.ball.height) // 2)
        self.is_moving = False

    def check_paddle(self):
        """
        Check the object is paddle or not, when the ball is moving and touching something.
        """
        for x in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                maybe_paddle = self.window.get_object_at(x, y)
                if maybe_paddle is not None:
                    if maybe_paddle is self.paddle:
                        return True

    def check_brick(self):
        """
        Check the object is brick or not, when the ball is moving and touching something.
        """
        for x in range(self.ball.x, self.ball.x + self.ball.width + 1, self.ball.width):
            for y in range(self.ball.y, self.ball.y + self.ball.height + 1, self.ball.height):
                maybe_brick = self.window.get_object_at(x, y)
                if maybe_brick is not None:
                    if maybe_brick is not self.paddle and maybe_brick is not self.label and maybe_brick \
                            is not self.lives_board:
                        self.window.remove(maybe_brick)
                        self.n += 1
                        self.label.text = f'Scores: {self.n}'
                        return True

    def game_over(self):
        """
        When the hearts is consumed, showing 'GAME OVER' to the player.
        """
        the_end = GLabel('GAME OVER', x=self.brick.width*1.5, y=self.window.height//2)
        the_end.color = 'red'
        the_end.font = 'Comic Sans MS-40'
        self.window.add(the_end)

    def win(self):
        """
        When all the bricks is break, showing 'CONGRATULATION' to the player.
        """
        you_did = GLabel('CONGRATULATION!!', x=self.brick.width//2, y=self.window.height//2)
        you_did.color = 'red'
        you_did.font = 'Comic Sans MS-30'
        self.window.add(you_did)
        self.is_moving = False

    @staticmethod
    def max_scores():
        return BRICK_ROWS*BRICK_COLS















