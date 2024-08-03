from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}",False,"center",("Arial", 15, "normal"))
        self.hideturtle()


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",False,"Center",("Arial", 15, "normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Courier", 15, "normal"))
