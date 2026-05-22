# FLOW FIELDS
# every point on screen has an angle (direction)
# N turtles each follow the angle at their current position, step, repeat
# dont clear trails - let them accumulate
# angle can be defined as:
#   sin(x) * cos(y)          -> smooth rippling lanes, easy starting point
#   perlin noise              -> organic, needs 'noise' library
#   distance from a point     -> spiral/galaxy effect
#   time-varying field        -> field shifts while particles are moving
# the screen slowly fills with flowing lines
import turtle
import random
import time
import math

t = turtle.Turtle()
t.color("blue")
turtle.bgcolor("black")
t.speed(0)
width = turtle.window_width()
height = turtle.window_height()
print(width, height)
i = input()

turtle.done()
