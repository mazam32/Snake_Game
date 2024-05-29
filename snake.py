from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def create_snake(self):
        for positions in POSITIONS:
            self.add_segment(position=positions)
        
    def move(self):
        for i in range(len(self.all_turtles) - 1, 0, -1):
            pos_to_goto_x = self.all_turtles[i - 1].xcor()
            pos_to_goto_y = self.all_turtles[i - 1].ycor()
            self.all_turtles[i].goto(pos_to_goto_x, pos_to_goto_y)
        self.all_turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    def add_segment(self, position):
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.setposition(position)
            self.all_turtles.append(new_turtle)