from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(x= 0, y= 270)
        self.penup()
        self.score = 0
        self.color("white")
        self.write(f"Score: {self.score}", align= ALIGNMENT, font= FONT)
        super().hideturtle()
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align= "center", font=FONT)