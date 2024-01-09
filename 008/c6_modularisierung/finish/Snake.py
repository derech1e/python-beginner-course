import turtle
from Direction import Direction


class Snake:

    def __init__(self, screen):
        self.screen = screen
        self.t = turtle.Turtle()
        self.t.shape("circle")  # See https://docs.python.org/3.12/library/turtle.html#turtle.shape
        self.t.color("blue")
        self.t.penup()
        self.t.speed(0)
        self.direction = Direction.STOP

        # Methods
        self.__setup_listeners()
        self.__move()  # Klassenspezifische Funktionen können bereits während der Initialisierung aufgerufen werden.

    def __up(self):
        if self.direction != Direction.DOWN:
            self.direction = Direction.UP

    def __down(self):
        if self.direction != Direction.UP:
            self.direction = Direction.DOWN

    def __left(self):
        if self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT

    def __right(self):
        if self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

    def __setup_listeners(self):
        self.screen.listen()
        self.screen.onkeypress(self.__up, "Up")
        self.screen.onkeypress(self.__down, "Down")
        self.screen.onkeypress(self.__left, "Left")
        self.screen.onkeypress(self.__right, "Right")

    def is_colliding(self):
        return self.t.xcor() > 350 or self.t.xcor() < -350 or self.t.ycor() > 350 or self.t.ycor() < -350

    def __move(self):
        if self.direction == Direction.LEFT:
            self.t.setx(self.t.xcor() - 10)

        if self.direction == Direction.RIGHT:
            self.t.setx(self.t.xcor() + 10)

        if self.direction == Direction.UP:
            self.t.sety(self.t.ycor() + 10)

        if self.direction == Direction.DOWN:
            self.t.sety(self.t.ycor() - 10)

        if self.is_colliding():
            self.t.home()

        self.screen.ontimer(self.__move, 20)
