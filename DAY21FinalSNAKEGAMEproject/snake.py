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
        for parts in BODY_POSITIONS:
            self.add_parts(parts)

    def add_parts(self, parts):
        snake_body = Turtle("circle")
        snake_body.color("yellow")
        snake_body.penup()
        snake_body.goto(parts)
        self.body_parts.append(snake_body)

    def extend(self):
        self.add_parts(self.body_parts[-1].position())

    def creep(self):
        for part_num in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[part_num - 1].xcor()
            new_y = self.body_parts[part_num - 1].ycor()
            self.body_parts[part_num].goto(new_x, new_y)

        self.head.forward(CREEP_DISTANCE)

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

    # def up(self):
    #     self.head.setheading(90)
    #
    # def down(self):
    #     self.head.setheading(270)
    #
    # def left(self):
    #     self.head.setheading(180)
    #
    # def right(self):
    #     self.head.setheading(0)