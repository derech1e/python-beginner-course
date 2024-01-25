import turtle


class ScoreManager:
    def __init__(self):
        self.pencil = turtle.Turtle()
        self.pencil.speed(0)
        self.pencil.shape('circle')
        self.pencil.color('white')
        self.pencil.penup()
        self.pencil.hideturtle()
        self.high_score = 0
        self.current_score = 0
        self.__draw_score()

    def __draw_score(self):
        self.pencil.clear()
        self.pencil.goto(0, 310)
        self.pencil.write(f'Score: {self.current_score} High Score: {self.high_score}', align='center',
                          font=('Courier', 24, 'normal'))

    def add(self, score):
        self.current_score += score
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.__draw_score()

    def reset(self):
        self.current_score = 0
        self.__draw_score()
