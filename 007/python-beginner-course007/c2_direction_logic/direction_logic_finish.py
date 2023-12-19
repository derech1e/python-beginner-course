import turtle

screen = turtle.Screen()
screen.setup(width=700, height=700)
t = turtle.Turtle()
t.direction = "STOP"


def up():
    print(f"Aktuelle Richtung: {t.direction}")
    if t.direction != "DOWN":
        t.direction = "UP"
    print(f"Neue Richtung: {t.direction}")


def down():
    print(f"Aktuelle Richtung: {t.direction}")
    if t.direction != "UP":
        t.direction = "DOWN"
    print(f"Neue Richtung: {t.direction}")


def left():
    print(f"Aktuelle Richtung: {t.direction}")
    if t.direction != "RIGHT":
        t.direction = "LEFT"
    print(f"Neue Richtung: {t.direction}")


def right():
    print(f"Aktuelle Richtung: {t.direction}")
    if t.direction != "LEFT":
        t.direction = "RIGHT"
    print(f"Neue Richtung: {t.direction}")


screen.listen()  # Setzt den Fokus auf die Turtle um auf Eingaben zu 'hören'
screen.onkeypress(up, "Up")  # Doku hier: https://docs.python.org/3.12/library/turtle.html#turtle.onkeypress
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

screen.mainloop()
