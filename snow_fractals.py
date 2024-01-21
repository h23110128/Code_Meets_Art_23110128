import turtle
import random
 
# setup the window with a background color
wn = turtle.Screen()
wn.bgcolor("cyan")
 
# assign a name to your turtle
elsa = turtle.Turtle()
elsa.speed(15)
 
# create a list of colours
 
# create a function to create different size snowflakes
def snowflake(size):
 
    # move the pen into starting position
    elsa.penup()
    elsa.forward(10*size)
    elsa.left(45)
    elsa.pendown()
    elsa.color("white")
 
    # draw branch 8 times to make a snowflake
    for i in range(8):
        branch(size)   
        elsa.left(45)
     
 
# create one branch of the snowflake
def branch(size):
    for i in range(3):
        for i in range(3):
            elsa.forward(10.0*size/3)
            elsa.backward(10.0*size/3)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(10.0*size/3)
        elsa.left(45)
    elsa.right(90) 
    elsa.forward(10.0*size)
 
# loop to create 20 different sized snowflakes 
# with different starting co-ordinates
t=0
s=0
x1=range(-100,101,20)
y1=range(200,-1,-20)
for i in range(20):
    x=x1[i]
    y=y1[i]
    size= 1
    elsa.penup()
    elsa.goto(x, y)
    elsa.pendown()
    snowflake(size)
    t+=20
    s-=20
    if s>100:s=0

 
# leave the window open until you click to close  
wn.exitonclick()  
canvas.postscript(file="f.txt")

from PIL import image
psimage = Image.open("f.txt")
psimage.save("bar.png")
