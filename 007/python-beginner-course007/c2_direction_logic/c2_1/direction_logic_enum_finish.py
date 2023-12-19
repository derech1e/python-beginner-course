import turtle
from Direction import Direction

screen = turtle.Screen()
screen.setup(width=700, height=700)
t = turtle.Turtle()
t.direction = Direction.STOP


def up():
    print(f"Aktuelle Richtung: {t.direction.name}")
    if t.direction != Direction.DOWN:
        t.direction = Direction.UP
    print(f"Neue Richtung: {t.direction.name}")


def down():
    print(f"Aktuelle Richtung: {t.direction.name}")
    if t.direction != Direction.UP:
        t.direction = Direction.DOWN
    print(f"Neue Richtung: {t.direction.name}")


def left():
    print(f"Aktuelle Richtung: {t.direction.name}")
    if t.direction != Direction.RIGHT:
        t.direction = Direction.LEFT
    print(f"Neue Richtung: {t.direction.name}")


def right():
    print(f"Aktuelle Richtung: {t.direction.name}")
    if t.direction != Direction.LEFT:
        t.direction = Direction.RIGHT
    print(f"Neue Richtung: {t.direction.name}")


screen.listen()  # Setzt den Fokus auf die Turtle um auf Eingaben zu 'hören'
screen.onkeypress(up, "Up")  # Doku hier: https://docs.python.org/3.12/library/turtle.html#turtle.onkeypress
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

screen.mainloop()
