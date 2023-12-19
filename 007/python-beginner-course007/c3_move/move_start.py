import turtle
from Direction import Direction

screen = turtle.Screen()
screen.setup(width=700, height=700)
t = turtle.Turtle()
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


def move():
    # implementation here
    t.xcor()  # Gibt die aktuelle X Koordinate der Turtle zurück
    t.setx(VALUE_HERE)  # Bewegt die Turtle zur angegebenen X Koordinate

    screen.ontimer(FUNCTION_HERE, EXECUTION_DELAY_HERE)  # EXECUTION_DELAY_HERE wird in millisekunden angegeben
    # Doku dazu hier: https://docs.python.org/3.12/library/turtle.html#turtle.TurtleScreen.ontimer


screen.mainloop()
