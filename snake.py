from turtle import Turtle
starting_position=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()


    def add_segment(self,position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segment.append(snake)

    def extend(self):
        self.add_segment(self.segment[-1].position())



    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)
    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)
    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)
    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)


# snake.penup()
