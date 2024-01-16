import turtle


def setup_screen(size, color="orange"):
    screen = turtle.Screen()
    screen.setup(width=size, height=size)
    screen.tracer(0)
    screen.bgcolor(color)
    return screen


def setup_play_field():
    pencil = turtle.Turtle()
    pencil.speed(0)
    pencil.shape('circle')
    pencil.color('black')
    pencil.penup()
    pencil.hideturtle()
    pencil.goto(310, 310)
    pencil.pendown()
    pencil.goto(-310, 310)
    pencil.goto(-310, -310)
    pencil.goto(310, -310)
    pencil.goto(310, 310)
    pencil.penup()
