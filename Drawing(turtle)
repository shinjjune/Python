"""
import turtle
t=turtle.Turtle()
t.shape("turtle")
t.color("black")
t.stamp()

move=120

for i in range(6):
    t.forward(80)
    t.pendown()
    t.forward(25)
    t.forward(15)
      #처음으로 돌아감
    t.right(move)
    move += 60
    t.left(move)
    move +=60
"""
import turtle  #그래픽을 이용하고자 할 경우 기본 제공

colors=["red","purple","blue","green","yellow","orange"]
t=turtle.Turtle()
t.shape("turtle")
"""
def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("gold")
    square(50)
    t.end_fill()

s=turtle.Screen()
s.onscreenclick(drawit)
"""

def draw_shape(radius, color1):
    t.left(270)
    t.width(3)
    t.color("black",color1)
    t.begin_fill()
    t.circle(radius/2.0,-180)
    t.circle(radius,180)
    t.left(180)
    t.circle(-radius/2.0,-180)
    t.end_fill()

t.reset()
draw_shape(200,"red")
t.left(270)
draw_shape(200,"blue")
