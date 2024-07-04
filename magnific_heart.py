import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(90000) 
bgcolor("white")
color("red")
hideturtle()
penup()
goto(0, -200)
pendown()

begin_fill()

for i in range(6000):
    k = i / 100
    x = hearta(k) * 20
    y = heartb(k) * 20
    goto(x, y)

end_fill()
done()
