import cmath,turtle,math,time
t = turtle.Turtle(visible=False)
t_2 = turtle.Turtle(visible=False)
turtle.tracer(0, 0)
turtle.bgcolor("black")
t.color("green")
t_2.color("red")

def taylor_exp(z, n):
    """Calculate the Taylor series expansion of e^z up to n terms."""
    result = 0
    arr = []
    for k in range(n):
        result += (z**k) / math.factorial(k)
        arr.append(result)
    return result,arr

def imaginary_exponential(z, n):
    """Calculate the imaginary exponential e^(i*z) using Taylor series."""
    return taylor_exp(1j * z, n)

def draw_complex_exponential(z, n):
    """Draw the complex exponential e^(i*z) on the turtle canvas."""
    _, arr = imaginary_exponential(z, n)
    colors = ["red","orange","yellow","green","cyan","blue","purple"]
    for k, intermediate in enumerate(arr):
        
        t.color(colors[k % len(colors)])
        t.goto(intermediate.real*scale,
            intermediate.imag*scale)
    # t.goto(result.real * scale, result.imag * scale)  # Scale for visibility
    turtle.update()

scale = 100  # Scale for visibility
depth = 20  # Depth of Taylor series expansion

for i in range(0, 360+1):
    #! draw the unit circle
    if i == 0:
        t_2.penup()
        t_2.goto(math.cos(math.radians(i)) * scale, math.sin(math.radians(i)) * scale)
        t_2.pendown()
    t_2.goto(math.cos(math.radians(i)) * scale, math.sin(math.radians(i)) * scale)

for i in range(0, 360+1, 1):
    t.clear()
    z = math.radians(i)
    draw_complex_exponential(z, depth)
    time.sleep(0.05)
turtle.done()