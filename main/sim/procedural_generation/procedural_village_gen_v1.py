"""
project idea: procedural village generator

make a complete 2d village procedurally.

stuff it could have:
#!- terrain
#!- roads / paths
#!- houses and buildings
#!- farms / fields
#?- trees / forests
#!- rivers / lakes
#?- wells and random landmarks
#!- village center
#!!- buildings that actually make sense where they are
#!- houses mostly near roads
#?- farms near good land / water
#!!!!- seeds so the same village can be generated again

progression:
v1.x: random terrain + buildings
v2.x: roads connecting buildings
v3.x: make the placement actually logical
v4.x: multiple villages connected by roads
v5.x: simulate the village growing over time
v6.x: population, resources, migration, expansion, etc.

#!main goal:
make it look like an actual village that people built,
not just a bunch of random shit scattered around.

2d only for now.(use turtle for now later use pygame or smth)
#!!!!!!!!! IF USING TURTLE DO NOT MAKE A SHIT TON OF TURT OBJS OR THE PC WILL CRASH.

#//DO NOT START THIS BEFORE EXAMS.
"""
import turtle,math,random
random.seed(0) #seed for reproducibility
turtle.tracer(0)
turtle.colormode(255)
turtle.bgcolor("black")

class Helper(turtle.Turtle):
    def __init__(self,x,y,pen_c:tuple[int,int,int],h_size,h_shape):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color(pen_c)
        self.shapesize(h_size)
        self.shape(h_shape)
        self.x = x
        self.y = y
    
    def print(self,tx,ty):
        self.goto(tx,ty)
        self.pendown()
        self.stamp()
        self.penup()

path_helpers = [
    
]