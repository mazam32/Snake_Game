from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.setposition(x= 0, y= 270)
        self.penup()
        self.score = 0
        with open(file= "data.txt") as data:
            self.high_score =int(data.read())
        self.color("white")
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGNMENT, font= FONT)
        super().hideturtle()
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= ALIGNMENT, font= FONT)
        

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode= "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.increase_score()