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
        return self.t.xcor() > 300 or self.t.xcor() < -300 or self.t.ycor() > 300 or self.t.ycor() < -300

    def add_segment(self):
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("circle")
        segment.color("gray")
        segment.penup()
        self.segments.append(segment)

    def update_speed(self):
        if self.speed > 10:
            self.speed -= 5

    def reset(self):
        self.speed = 100
        self.t.home()
        self.direction = Direction.STOP
        for segment in self.segments:
            segment.hideturtle()  # Hide each segment before clearing list

        self.segments.clear()

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

        self.screen.ontimer(self.__move, self.speed)
