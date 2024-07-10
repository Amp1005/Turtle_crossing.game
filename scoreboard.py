from turtle import *

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.font = FONT
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level- {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Ohhh!, Turtle is dead😔", align="center", font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()



