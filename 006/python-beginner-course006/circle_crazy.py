import turtle
import random

screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)


def change_color():
    r = random.random()
    g = random.random()
    b = random.random()
    t.color(r, g, b)


for i in range(0, 400, 10):
    t.circle(i)
    change_color()

screen.mainloop()
