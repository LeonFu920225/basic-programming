import turtle
import random
t = turtle.Pen()
max = 100
min = 50
t.speed(0.5)
colorList = ['green', 'red', 'blue']
for i in range(max,min,-1):
    t.color(random.choice(colorList))
    t.circle(i)
    t.forward(5)