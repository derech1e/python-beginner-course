from Snake import Snake
from Food import Food
import Utils

screen = Utils.setup_screen(700)
snake = Snake(screen)
food = Food()


def tick():
    screen.update()

    if snake.t.distance(food.food) < 20:
        food.find_new_location()
        snake.add_segment()
        snake.update_speed()

    screen.ontimer(tick, 10)


tick()
screen.mainloop()
