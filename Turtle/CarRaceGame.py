import time 
import turtle
from turtle import Turtle
from random import randint

#WINDOWS SETUP
window=turtle.Screen()
window.title("CAR RACE")
turtle.bgcolor("cyan")
turtle.color("black")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("CAR RACE",font=("Arial",25,"bold"))
turtle.penup()

#DIRT
turtle.speed(0)
turtle.setpos(-400,-180)
turtle.color("grey")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#FINISH LINE
stamp_size=20
square_size=15
finish_line=200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()
for i in range(10):
	turtle.setpos(finish_line,(150-(i*square_size*2)))
	turtle.stamp()
for j in range(10):
	turtle.setpos(finish_line + square_size,((150- square_size)-(j*square_size*2)))
	turtle.stamp()
turtle.ht()


#CAR 1
car1=Turtle()
car1.speed(0)
car1.color("red")
car1.shape("triangle")
car1.penup()
car1.goto(-250,100)


#CAR 2
car2=Turtle()
car2.speed(0)
car2.color("blue")
car2.shape("triangle")
car2.penup()
car2.goto(-250,0)




time.sleep(1)
for i in range(145):
	car1.fd(randint(1,5))
	car2.fd(randint(1,5))

turtle.exitonclick()
turtle.done()
