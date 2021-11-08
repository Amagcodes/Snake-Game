import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

#the window
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(600,600)
wn.tracer(0)

#score
turtle.color("white")
turtle.penup()
turtle.goto(0,250)
turtle.write(f"Score:{score} High Score:{high_score}",align="center",font=("Arial",20,"bold"))
turtle.hideturtle()

#the snake head
head = turtle.Turtle()
head.speed(0)
head.color("yellow")
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = "stop"

#food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,100)

segments = []

#functions

def up():
    if head.direction !="down":
        head.direction = "up"
def down():
    if head.direction !="up":
        head.direction = "down"
def left():
    if head.direction !="right":
        head.direction = "left"
def right():
    if head.direction !="left":
        head.direction = "right"

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction =="down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction=="right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction =="left":
        x = head.xcor()
        head.setx(x - 20)
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(right, "Right")
wn.onkeypress(left, "Left")

while True:
    wn.update()

    #border collision
    if head.ycor() <-290 or head.ycor() >290 or head.xcor()<-290 or head.xcor() >290:
        time.sleep(0.3)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()

        score = 0

        turtle.clear()
        turtle.write(f"Score:{score} High Score:{high_score}",align="center",font=("Arial",20,"bold"))


    #food collision
    if head.distance(food) <20:
        x = random.randint(-270,270)
        y = random.randint(-270,270)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("blue")
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)

        
        score +=1

        if score > high_score:
            high_score = score

        turtle.clear()
        turtle.write(f"Score:{score} High Score:{high_score}",align="center",font=("Arial",20,"bold"))


    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) >0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

            
    move()

    #body collision
    for segment in segments:
        if segment.distance(head) <20:
            time.sleep(0.3)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            score = 0

            turtle.clear()
            turtle.write(f"Score:{score} High Score:{high_score}",align="center",font=("Arial",20,"bold"))
            
            

    time.sleep(delay)
wn.mainloop()
