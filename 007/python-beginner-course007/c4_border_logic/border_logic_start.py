import turtle
from Direction import Direction

screen = turtle.Screen()
screen.setup(width=700, height=700)
t = turtle.Turtle()
t.shape("circle")  # See https://docs.python.org/3.12/library/turtle.html#turtle.shape
t.color("blue")
t.penup()
t.speed(0)
t.direction = Direction.STOP


def up():
    if t.direction != Direction.DOWN:
        t.direction = Direction.UP


def down():
    if t.direction != Direction.UP:
        t.direction = Direction.DOWN


def left():
    if t.direction != Direction.RIGHT:
        t.direction = Direction.LEFT


def right():
    if t.direction != Direction.LEFT:
        t.direction = Direction.RIGHT


screen.listen()  # Setzt den Fokus auf die Turtle um auf Eingaben zu 'hören'
screen.onkeypress(up, "Up")  # Doku hier: https://docs.python.org/3.12/library/turtle.html#turtle.onkeypress
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")


# implementation here

def move():
    if t.direction == Direction.LEFT:
        t.setx(t.xcor() - 10)

    if t.direction == Direction.RIGHT:
        t.setx(t.xcor() + 10)

    if t.direction == Direction.UP:
        t.sety(t.ycor() + 10)

    if t.direction == Direction.DOWN:
        t.sety(t.ycor() - 10)

    # implementation here

    screen.ontimer(move, 20)


move()
screen.mainloop()
