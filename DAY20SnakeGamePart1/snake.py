from turtle import Turtle

BODY_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
CREEP_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]

    def create_snake(self):
        for seg in BODY_POSITIONS:
            self.add_parts(seg)

    def add_parts(self, position):
        snake_body = Turtle("square")
        snake_body.color("yellow")
        snake_body.penup()
        snake_body.goto(position)
        self.body_parts.append(snake_body)

    def reset(self):
        for seg in self.body_parts:
            seg.goto(1000, 1000)
        self.body_parts.clear()
        self.create_snake()
        self.head = self.body_parts[0]

    def extend(self):
        self.add_parts(self.body_parts[-1].position())

    def move(self):
        for parts in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[parts - 1].xcor()
            new_y = self.body_parts[parts - 1].ycor()
            self.body_parts[parts].goto(new_x, new_y)

        self.body_parts[0].forward(CREEP_DISTANCE)

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