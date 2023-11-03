from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []
        self.create_snake()
        self.step = 20
        self.head = self.segments[0]

    def create_snake(self):
        for position in self.starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) -1, 0, -1):
            x_new = self.segments[i - 1].xcor()
            y_new = self.segments[i - 1].ycor()
            self.segments[i].goto(x_new, y_new)
        self.segments[0].forward(self.step)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
