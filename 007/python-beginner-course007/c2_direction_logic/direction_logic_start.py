import turtle

screen = turtle.Screen()
screen.setup(width=700, height=700)
t = turtle.Turtle()


def up():
    print("Up!")


def down():
    print("Down!")


def left():
    print("Left!")


def right():
    print("Right!")


screen.listen()  # Setzt den Fokus auf die Turtle um auf Eingaben zu 'hören'
screen.onkeypress(up, "Up")  # Doku hier: https://docs.python.org/3.12/library/turtle.html#turtle.onkeypress
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

screen.mainloop()
