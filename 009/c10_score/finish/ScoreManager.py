import turtle


class ScoreManager:
    high_score = 0
    current_score = 0

    def __init__(self):
        self.pencil = turtle.Turtle()
        self.pencil.speed(0)
        self.pencil.shape('circle')
        self.pencil.color('white')
        self.pencil.penup()
        self.pencil.hideturtle()
        self.__draw_score(0)

    def __draw_score(self, current_score):
        self.pencil.clear()
        self.pencil.goto(0, 310)
        self.pencil.write(f'Score: {current_score} High Score: {self.high_score}', align='center', font=('Courier', 24, 'normal'))

    def add(self, score):
        if self.current_score + score > self.high_score:
            self.high_score += score
        self.current_score += score
        self.__draw_score(self.current_score)

    def reset(self):
        self.current_score = 0
        self.__draw_score(0)
