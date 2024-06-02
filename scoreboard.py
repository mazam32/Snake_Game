from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(x= 0, y= 270)
        self.penup()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.increase_score()
        super().hideturtle()
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGNMENT, font= FONT)
        

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.increase_score()