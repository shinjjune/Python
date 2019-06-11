import turtle

colors=["red","purple","blue","green","yellow","orange"]
t=turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)    #최대속도
t.width(3)    #선의 굵기
length=10     #선의 초기 길이

while length<500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length=length+5
