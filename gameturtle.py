from turtle import *


class Sprite(Turtle):
    def __init__(self, shape, color, x, y, step):
        Turtle.__init__(self)
        self.penup()
        self.shape(shape)
        self.color(color)
        self.goto(x, y)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        return dist < 30

    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.goto(x_start, y_start)
        self.setheading(self.towards(x_end, y_end))

    def make_move(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)


player = Sprite("circle", "orange", 0, -100, 10)
enemy1 = Sprite("square", "red", -200, 100, 50)
enemy1.set_move(-200, 0, 200, 0)
enemy2 = Sprite("square", "red", 200, 50, 50)
enemy2.set_move(200, 70, -200, 70)
finish_flag = Sprite("circle", "green", 60, 200, 0)

scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, "Up")
scr.onkey(player.move_down, "Down")
scr.onkey(player.move_right, "Right")
scr.onkey(player.move_left, "Left")


total_score = 0
while total_score < 1:
    enemy1.make_move()
    enemy2.make_move()
    if player.is_collide(finish_flag):
        player.goto(0, -100)
        total_score += 1
        player.write("You WIN!", font=("Arial", 14, "normal"))
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        finish_flag.hideturtle()
        player.write("You LOST!", font=("Arial", 14, "normal"))
        break

enemy1.hideturtle()
enemy2.hideturtle()
exitonclick()
