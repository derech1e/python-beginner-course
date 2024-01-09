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
        self.segments = []
        self.speed = 100

        # Methods
        self.__setup_listeners()
        self.__move()  # Klassenspezifische Methoden können bereits während der Initialisierung aufgerufen werden.

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

    def add_segment(self):
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("circle")
        segment.color("gray")
        segment.penup()
        self.segments.append(segment)

    def update_speed(self):
        if self.speed > 10:
            self.speed = self.speed - 5

    def __move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)

        if len(self.segments) > 0:
            self.segments[0].goto(self.t.xcor(), self.t.ycor())

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

        self.screen.ontimer(self.__move, self.speed)
