from Snake import Snake
from Food import Food
import Utils

screen = Utils.setup_screen(700)
snake = Snake(screen)
food = Food()


def game_loop():
    if snake.t.distance(food.food) < 20:
        food.find_new_location()
        snake.add_segment()

    screen.ontimer(game_loop, 10)


game_loop()
screen.mainloop()
