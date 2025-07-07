"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics, BALL_RADIUS, BRICK_ROWS, BRICK_COLS, INITIAL_Y_SPEED

FRAME_RATE = 10
NUM_LIVES = 3


def main():
    """
        Movement and collision detection are performed only when the ball is set to move
        1. Get the ball's velocity
        2. move the ball
        3. Movement and collision detection
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    num_bricks_total = BRICK_ROWS * BRICK_COLS
    bricks_destroyed = 0
    while True:
        if lives <= 0:
            graphics.display_game_over_message()
            break
        if bricks_destroyed >= num_bricks_total:
            graphics.display_win_message()
            break
        if graphics.ball_is_moving:
            dx = graphics.get_ball_dx()
            dy = graphics.get_ball_dy()
            graphics.ball.move(dx, dy)
            if graphics.ball.x <= 0:
                graphics.set_ball_dx(-dx)
                graphics.ball.x = 0
            elif graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_ball_dx(-dx)
                graphics.ball.x = graphics.window.width - graphics.ball.width
            elif graphics.ball.y <= 0:
                graphics.set_ball_dy(-dy)
                graphics.ball.y = 0
            elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                graphics.ball_is_moving = False
                graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
                graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2

            collided_object = None
            # The default value is no collision. Once a collision occurs, the state will be reassigned.
            ball_diameter = BALL_RADIUS * 2
            obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            if obj1 is not None:
                collided_object = obj1

            if collided_object is None:
                obj2 = graphics.window.get_object_at(graphics.ball.x + ball_diameter, graphics.ball.y)
                if obj2 is not None:
                    collided_object = obj2

            if collided_object is None:
                obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + ball_diameter)
                if obj3 is not None:
                    collided_object = obj3

            if collided_object is None:
                obj4 = graphics.window.get_object_at(graphics.ball.x + ball_diameter, graphics.ball.y + ball_diameter)
                if obj4 is not None:
                    collided_object = obj4

            if collided_object is not None:
                if collided_object is graphics.paddle:
                    current_dy = graphics.get_ball_dy()
                    if current_dy >= 0:
                        graphics.set_ball_dy(-INITIAL_Y_SPEED)
                    else:
                        graphics.set_ball_dy(INITIAL_Y_SPEED)

                # if the object is not paddle, then it would be bricks
                else:
                    graphics.window.remove(collided_object)
                    bricks_destroyed += 1
                    graphics.set_ball_dy(-dy)
                    if bricks_destroyed >= num_bricks_total:
                        pause(FRAME_RATE)

        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
