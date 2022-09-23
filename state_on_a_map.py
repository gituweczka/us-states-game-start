from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 10, 'normal')


class StateOnAMap(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")

    def write_state_name(self, name, x, y):
        self.goto(x, y)
        self.write(f"{name}", move=True, align=ALIGNMENT, font=FONT)

    def end_quiz(self):
        self.goto(0,0)
        self.color("red")
        self.write("Well done!", move=True, align=ALIGNMENT, font=('Courier', 30 , 'normal'))
