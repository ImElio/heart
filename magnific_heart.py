import turtle
import math
import time

# Define functions to calculate the heart's coordinates
def hearta(k):
    return 16 * math.sin(k) ** 3

def heartb(k):
    return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

# Configure the Turtle window
turtle.speed(0)          # Set the drawing speed to the maximum
turtle.bgcolor("black")  # Set the background color to black
turtle.color("red")      # Set the pen color to red
turtle.hideturtle()      # Hide the turtle for a cleaner look

# Draw the outline of the heart
turtle.penup()
turtle.goto(0, -200)     # Move to the starting point without drawing
turtle.pendown()
for i in range(360):     # Loop to draw the heart's outline
    k = math.radians(i)
    x = hearta(k) * 20
    y = heartb(k) * 20
    turtle.goto(x, y)

# Fill the heart with an animation
turtle.penup()
turtle.goto(0, -200)     # Move back to the starting point without drawing
turtle.pendown()
turtle.begin_fill()      # Start filling the heart
for i in range(360):     # Loop to fill the heart with an animation
    k = math.radians(i)
    x = hearta(k) * 20
    y = heartb(k) * 20
    turtle.goto(x, y)
    turtle.update()      # Update the drawing
    time.sleep(0.01)     # Wait a bit to create the animation effect

turtle.end_fill()        # Finish filling the heart

# Complete the drawing
turtle.done()            # Finish the turtle graphics
