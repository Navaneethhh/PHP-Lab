from turtle import Turtle
t=Turtle()
def hexagon(t,x,y,len):
    t.up()
    t.goto(x,y)
    t.pencolor("green")
    t.setheading(270)
    t.down()
    for count in range(6):
        t.forward(len)
        t.left(60)
hexagon(t,10,20,60)
