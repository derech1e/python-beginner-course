import turtle


def setup_screen(size, color="orange"):
    screen = turtle.Screen()
    screen.setup(width=size, height=size)
    screen.bgcolor(color)
    return screen
