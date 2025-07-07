"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5
BRICK_WIDTH = 40
BRICK_HEIGHT = 15
BRICK_ROWS = 10
BRICK_COLS = 10
BRICK_OFFSET = 50
BALL_RADIUS = 10
PADDLE_WIDTH = 75
PADDLE_HEIGHT = 15
PADDLE_OFFSET = 50
INITIAL_Y_SPEED = 3
MAX_X_SPEED = 5


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        paddle_x = (self.window.width - paddle_width) / 2
        paddle_y = self.window.height - paddle_offset - paddle_height
        self.paddle = GRect(paddle_width, paddle_height, x=paddle_x, y=paddle_y)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        ball_x = (self.window.width / 2) - ball_radius
        ball_y = (self.window.height / 2) - ball_radius
        self.ball = GOval(ball_radius * 2, ball_radius * 2, x=ball_x, y=ball_y)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)

        # Default initial velocity for the ball and ball is not moving in the beginning
        self.__dx = 0
        self.__dy = 0
        self.ball_is_moving = False

        onmouseclicked(self.setting_mouse_click)
        onmousemoved(self.setting_mouse_move)

        brick_color_options = ['wheat', 'khaki', 'silver', 'darkred', 'gray', 'beige', 'tan', 'floralwhite']
        for row in range(brick_rows):
            for col in range(brick_cols):
                brick_x = col * (brick_width + brick_spacing)
                brick_y = brick_offset + row * (brick_height + brick_spacing)
                brick = GRect(brick_width, brick_height, x=brick_x, y=brick_y)
                brick.filled = True
                random_color = random.choice(brick_color_options)
                brick.fill_color = random_color
                brick.color = brick.fill_color
                self.window.add(brick)

        self.game_message_label = None

    def setting_mouse_move(self, event):
        """
        Process mouse movement events and let the board move horizontally with the mouse.
        The center of the board is aligned with the x-coordinate of the mouse.
        The board will not extend beyond the left and right borders of the viewport.
        """
        new_paddle_x = event.x - self.paddle.width / 2
        if new_paddle_x < 0:
            new_paddle_x = 0
        elif new_paddle_x + self.paddle.width > self.window.width:
            new_paddle_x = self.window.width - self.paddle.width
        self.paddle.x = new_paddle_x
        # paddle.y will always remain the same as the setting in __init__

    def setting_mouse_click(self, event):
        """
        Handle mouse click events.
        If the ball is not already moving, give it an initial velocity and start moving.
        The click event will work only when the ball is not moving and the click event will make the ball move.
        """
        if not self.ball_is_moving:
            self.ball_is_moving = True
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx
                # 50% chance to reverse x direction

    def get_ball_dx(self):
        return self.__dx

    def get_ball_dy(self):
        return self.__dy

    def set_ball_dx(self, dx):
        self.__dx = dx

    def set_ball_dy(self, dy):
        self.__dy = dy

    def display_game_over_message(self):
        if self.game_message_label is not None:
            self.window.remove(self.game_message_label)
        self.game_message_label = GLabel("Game Over!")
        self.game_message_label.font = "-70"
        label_x = (self.window.width - self.game_message_label.width) / 2
        label_y = (self.window.height - self.game_message_label.height) / 2
        self.window.add(self.game_message_label, label_x, label_y)

    def display_win_message(self):
        if self.game_message_label is not None:
            self.window.remove(self.game_message_label)

        self.game_message_label = GLabel("You Win!")
        self.game_message_label.font = "-70"
        label_x = (self.window.width - self.game_message_label.width) / 2
        label_y = (self.window.height - self.game_message_label.height) / 2
        self.window.add(self.game_message_label, label_x, label_y)