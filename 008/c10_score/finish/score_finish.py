from Snake import Snake
from Food import Food
from ScoreManager import ScoreManager
import Utils
import time

screen = Utils.setup_screen(700)
Utils.setup_play_field()

# Setup score manager
scoreManager = ScoreManager()

snake = Snake(screen)
food = Food()


def handle_collision():
    time.sleep(0.5)
    snake.reset()
    scoreManager.reset()


def tick():
    if snake.is_colliding():
        handle_collision()

    for segment in snake.segments:
        if segment.distance(snake.t) < 10:
            handle_collision()

    if snake.t.distance(food.food) < 20:
        food.find_new_location()
        snake.add_segment()
        snake.update_speed()
        scoreManager.add(10)

    screen.update()
    screen.ontimer(tick, 10)


tick()
screen.mainloop()
