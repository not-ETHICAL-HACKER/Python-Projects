import turtle,math,random

turtle.bgcolor("black")
turtle.tracer(0)
helper_1 = turtle.Turtle(visible=False)
helper_2 = turtle.Turtle(visible=False)

WIDTH = HEIGHT = 400
num = 10
w2,h2 = WIDTH//2,HEIGHT//2
lightnin_line  = w2 * 0.9
x_arr = [random.randint(-w2,w2) for _ in range(num)]
y_arr = [lightnin_line for _ in range(num)]

def stamp(t:turtle.Turtle,x_arr:list[int],y_arr:list[int],color:str):
    # t.clear()
    t.color(color)
    for x,y in zip(x_arr,y_arr):
        t.penup()
        t.goto(x,y)
        # t.dot(3)
    turtle.update()

def gen_light(i):
    noise = 0.5
    vector_weight = 0.5
    x,y = x_arr[i],y_arr[i]
    if y < -w2:
        return
    if random.random() < .01:
        x_arr.append(x_arr[i])
        y_arr.append(y_arr[i])
    x_arr[i] += random.uniform(-1, 1)

    y_arr[i] -= 2
    if random.random() > 0.5:
        x_arr[i] += random.uniform(-10,10)
    
while True:
    for i in range(len(x_arr)):
        old_x = x_arr[i]
        old_y = y_arr[i]

        gen_light(i)

        helper_1.penup()
        helper_1.goto(old_x, old_y)
        helper_1.pendown()
        helper_1.goto(x_arr[i], y_arr[i])
        turtle.update()