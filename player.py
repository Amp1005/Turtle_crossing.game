from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0,new_y)

    def is_at_other_side(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

