import turtle,math,random,pygame
pygame.init()
W,H = 250,250
random.seed(42)
abs_max = 750
step = 25
pos_arr = [
    (x,y) for x in range(-W,W,step) for y in range(-H,H,step)
]
N = len(pos_arr)
funcs = {
    "sin": lambda x: math.sin(x/50 + pygame.time.get_ticks()/1000) * 5,
    "cos": lambda x: math.cos(x/50 + pygame.time.get_ticks()/1000) * 5,
    "atan2": lambda x: math.atan2(math.sin(x/50 + pygame.time.get_ticks()/1000), math.cos(x/50 + pygame.time.get_ticks()/1000)) * 5,
    "log": lambda x: math.log(abs(math.sin(x/50 + pygame.time.get_ticks()/1000)) + 1) * 5,
    "exp": lambda x: math.exp(math.sin(x/50 + pygame.time.get_ticks()/1000)) * 5,
    "sqrt": lambda x: math.sqrt(abs(math.sin(x/50 + pygame.time.get_ticks()/1000))) * 5,
}
turtle.tracer(0)
turtle.colormode(255)
turtle.bgcolor((0, 0, 0))
helper = turtle.Turtle(shape = "square")
helper.shapesize(0.1, 0.1)
helper.hideturtle()
def draw_rectangle(t, x, y,color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.stamp()
running = True
size = 2
k = 100
colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]
func_k = list(funcs.keys())
funcs_arrs = [random.choice(func_k) for _ in range(N)]
while running:
    '''for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            W2,H2 = W//2,H//2
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

            fade = pygame.Surface((W, H), pygame.SRCALPHA)
            fade.fill((0, 0, 0, 80))
            pos_arr = [
                (x,y) for x in range(0,W,step) for y in range(0,H,step)
            ]
            N = len(pos_arr)
            funcs_arrs = [random.choice(func_k) for _ in range(N)]
            colors = [(random.randint(0,255),random.randint(0,255),random.randint(0,255)) for _ in range(N)]'''
    for i,pos in enumerate(pos_arr):
        x,y = pos
        t = pygame.time.get_ticks() / 1000
        # x += funcs[funcs_arrs[i]](x)
        # y += funcs[funcs_arrs[i]](y)
        x += math.sin((y)/k + t)
        y += math.sin((x)/k + t)
        pos_arr[i] = (x,y)
    helper.clear()
    for i in range(N):
        draw_rectangle(helper, pos_arr[i][0], pos_arr[i][1], colors[i])
    turtle.update()
    print(f"random coords {random.choice(pos_arr)}",end = "\r")
turtle.done()