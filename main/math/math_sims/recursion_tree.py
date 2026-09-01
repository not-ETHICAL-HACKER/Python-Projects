import random,time,turtle,math,sys
turtle.bgcolor("black")
t = turtle.Turtle(visible=False)
t.color("green")
turtle.tracer(0, 0)
sys.setrecursionlimit(10**4)
c =  00
t.setheading(90)
def tree(length):
    if length < 10:
        global c
        c += 1
        turtle.update()
        t.dot(4,random.choice(["blue","yellow","red","purple"]))
        return
    weight = 0.75
    angle = math.pi*10
    thin = 10
    height =  1
    t.pensize(length/thin)
    t.forward(length/height)
    t.left(angle)
    tree(length*weight)
    t.pensize(length /thin)

    t.right(2*angle)
    tree(length*weight)
    t.pensize(length / thin)

    t.left(angle)
    t.backward(length/height)

def poly(side):
    n = math.tau
    for _ in range(int(n)):
        t.forward(side)
        t.left(360/n)

def recur_shape(side):
    """If you want to know the exact number for the specific starting side you have in your file right now, you can find it instantly with this formula:
    Total Shapes = ceil( ln(1/side) / ln(retention) )
    """
    turtle.colormode(255)
    if side < 1:
        t.clear()
        return
    phi =  (1 + math.sqrt(5)) / 2
    golden_angle = 360 / phi
    retention = 0.999
    t.left(golden_angle)
    t.color(int(255*abs(math.sin(side)))%256, int(255*abs(math.cos(side)))%256, int(255*abs(math.sin(2*side)))%256)
    # t.pensize(side/100)
    t.pensize(max(1,int(math.log10(side))))
    t.forward(side * 0.1)
    poly(side)
    # time.sleep(.01)
    turtle.update()
    recur_shape(side*retention)

def edge(l):
    if l < 1:
        turtle.update()
        return
    angle = 15
    t.forward(10)
    edge(l/4)
    t.left(angle)
    t.forward(10)
    edge(l/4)
    t.left(angle)
    t.forward(10)
    edge(l/4)
    t.left(angle)
    t.forward(10)
    edge(l/4)
    t.left(angle)
    t.forward(10)

recur_shape(10**2*5)

# print(c)
turtle.done()