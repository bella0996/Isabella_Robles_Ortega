#Isabella Nahomy Robles Ortega
from turtle import *

bgcolor("black")
speed(0)
pensize(3)
color("#F8C8DC")  # rosa pastel

def linea(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

# I
linea(-350, 100, -300, 100)
linea(-325, 100, -325, -100)
linea(-350, -100, -300, -100)

# S
linea(-270, 100, -220, 100)
linea(-270, 100, -270, 0)
linea(-270, 0, -220, 0)
linea(-220, 0, -220, -100)
linea(-270, -100, -220, -100)

# A
linea(-190, -100, -165, 100)
linea(-140, -100, -165, 100)
linea(-180, 0, -150, 0)

# B
linea(-110, 100, -110, -100)
linea(-110, 100, -70, 70)
linea(-70, 70, -110, 40)
linea(-110, 40, -70, 10)
linea(-70, 10, -110, -20)
linea(-110, -20, -70, -60)
linea(-70, -60, -110, -100)

# E
linea(-40, 100, -40, -100)
linea(-40, 100, 10, 100)
linea(-40, 0, 0, 0)
linea(-40, -100, 10, -100)

# L
linea(40, 100, 40, -100)
linea(40, -100, 90, -100)

# L
linea(120, 100, 120, -100)
linea(120, -100, 170, -100)

# A
linea(200, -100, 225, 100)
linea(250, -100, 225, 100)
linea(210, 0, 240, 0)

hideturtle()
done()
