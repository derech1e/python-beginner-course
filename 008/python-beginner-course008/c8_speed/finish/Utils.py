import turtle


def setup_screen(size, color="orange"):
    screen = turtle.Screen()
    screen.setup(width=size, height=size)
    screen.tracer(0)
    screen.bgcolor(color)
    return screen
