import turtle

from itertools import cycle
colors = cycle(['red','pink','navy','black','blue','gold'])

def draw_circles(size,angle,shift):
     turtle.bgcolor(next(colors))
     turtle.pencolor(next(colors))
     turtle.circle(size)
     turtle.left(angle)
     turtle.backward(shift)
     draw_circles(size+9, angle+6,shift+7)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(30)
draw_circles(30,7,1)
