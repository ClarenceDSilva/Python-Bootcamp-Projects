from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


def snake_segment_properties():
    """Describes the segment"""
    turtle = Turtle(shape="square")
    turtle.penup()
    turtle.color("white")
    return turtle


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.position = 0
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        # Defining 3 turtles to create a snake
        for _ in range(3):
            turtle = snake_segment_properties()
            turtle.goto(self.position, 0)
            self.position -= 20
            self.snake_segments.append(turtle)

    def reset(self):
        """Resets the snake to the home position to start a new game"""
        for seg in self.snake_segments:
            seg.goto(-650, 650)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def add_segment(self, position):
        turtle = snake_segment_properties()
        turtle.goto(position)
        self.snake_segments.append(turtle)

    def extend(self):
        """Adds a new segment to the snake"""
        self.add_segment(self.snake_segments[-1].position())

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            # This will generate second to last turtle_segment's position which are going to use to move the last turtle
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)

        # Now, move the first turtle_segment ahead
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # Position the head to move up. Cannot move when the head is down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Position the head to move down. Cannot move when the head is up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Position the head to move left. Cannot move when the head is right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Position the head to move right. Cannot move when the head is left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
