from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.score = 1
        self.penup() 
        self.goto(-280,265)

        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}",align="left",font=FONT)
    def level_up(self):
        self.score+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)
