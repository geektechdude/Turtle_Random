#!/bin/python3
#geektechstuff
#random turtle

#libraries to import
from random import *
from turtle import *

#defining shapes
def square():
    for x in range(4):
        forward(50)
        right(90)

def triangle():
    for side in range(3):
        forward(50)
        right(120)
        
#set up the area for turtle to use
area = Screen()
area.setup(500,500)
area.bgcolor('white')

#num in range defines how many shapes to create
for num in range(200):
    hideturtle()
    #speed shapes are drawn
    turtle_speed=randint(0,9)
    speed(turtle_speed)
    #creates a random number between 1 and 4
    random_shape=randint(1,4)
    #creates a random number between 1 and 4
    pen_color=randint(1,4)
    #creates a random number between -200 and 200
    rand_x=randint(-200,200)
    #creates a random number between -200 and 200
    rand_y=randint(-200,200)

#goes through pen colour options
    if pen_color==1:
        pencolor('black')
    elif pen_color==2:
        pencolor('blue')
    elif pen_color==3:
        pencolor('red')
    elif pen_color==4:
        pencolor('green')

#goes through shapes options   
    if random_shape==1:
        penup()
        goto(rand_x,rand_y)
        pendown()
        circle(50)
    elif random_shape==2:
        penup()
        goto(rand_x,rand_y)
        pendown()
        square()
    elif random_shape==3:
        penup()
        goto(rand_x,rand_y)
        pendown()
        dot(10)
    elif random_shape==4:
        penup()
        goto(rand_x,rand_y)
        pendown()
        triangle()
