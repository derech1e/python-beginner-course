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
        self.__setup_listeners()
        self.move()  # Klassenspezifische Funktionen können bereits während der Initialisierung aufgerufen werden.

    def up(self):
        if self.direction != Direction.DOWN:
            self.direction = Direction.UP

    def down(self):
        if self.direction != Direction.UP:
            self.direction = Direction.DOWN

    def left(self):
        if self.direction != Direction.RIGHT:
            self.direction = Direction.LEFT

    def right(self):
        if self.direction != Direction.LEFT:
            self.direction = Direction.RIGHT

    def __setup_listeners(self):
        self.screen.listen()
        self.screen.onkeypress(self.up, "Up")
        self.screen.onkeypress(self.down, "Down")
        self.screen.onkeypress(self.left, "Left")
        self.screen.onkeypress(self.right, "Right")

    def is_colliding(self):
        return self.t.xcor() > 350 or self.t.xcor() < -350 or self.t.ycor() > 350 or self.t.ycor() < -350

    def move(self):
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

        self.screen.ontimer(self.move, 20)
