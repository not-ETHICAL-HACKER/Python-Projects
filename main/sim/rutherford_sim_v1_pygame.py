import pygame,math,random

pygame.init()

W,H = 500,500
N = 200
A = 60
running = True
interaction_rad = 100
abs_rad = interaction_rad * (1 - 0.9)
atoms_per_column = 6

screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")
clock = pygame.time.Clock()
drag = .1


density = 100 #! out of 100
step = 1/density
spacing = 5 * step
start_y_atom = interaction_rad
start_y = (N - 1) * spacing / 2
start_x = W // 4
center_y = H //2
particles = [(start_x,center_y + (i - (N - 1) / 2) * spacing) for i in range(N)]
atoms = []
c = 0
cc = 0
for i in range(A):
    y_lvl = start_y_atom + cc * interaction_rad
    if i % atoms_per_column == 0:
        c += 1
        cc = 0
        y_lvl = interaction_rad
    cc += 1
    atoms.append((start_x * 2 + interaction_rad* c + random.uniform(-10,10),y_lvl + random.uniform(-10,10)))
"""
for row in range(rows):
    x_offset = (row % 2) * (interaction_rad / 2)

    for col in range(cols):
        x = start_x * 2 + col * interaction_rad + x_offset
        y = row * interaction_rad

        atoms.append((x, y))
"""
a_x_arr = [a[0] for a in atoms]
a_y_arr = [a[1] for a in atoms]
x_arr = [p[0] for p in particles]
y_arr = [p[1] for p in particles]
vx_arr = [1 for _ in range(N)]
vy_arr = [random.uniform(-1e-3,1e-3) for _ in range(N)]

angles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
    dx_arr = []
    dy_arr = []
    ux_arr = []
    uy_arr = []
    hyp_arr = []
    for i in range(A):
        temp_x = []
        temp_y = []
        temp_hyp = []
        for j in range(N):
            dx = a_x_arr[i] - x_arr[j]
            dy = a_y_arr[i] - y_arr[j]
            hyp = max(math.hypot(dx,dy),1e-6)
            temp_hyp.append(hyp)
            temp_x.append(dx/hyp)
            temp_y.append(dy/hyp)
        ux_arr.append(temp_x)
        uy_arr.append(temp_y)
        hyp_arr.append(temp_hyp)
    for i in range(A):
        for j in range(N):
            hyp = hyp_arr[i][j]
            ux = ux_arr[i][j]
            uy = uy_arr[i][j]
            vx = vx_arr[j]
            vy = vy_arr[j]
            if hyp <= abs_rad:
                k = 10**3 * 1/max(1e-3,hyp)
                decay = ((k)/hyp ** 2)
                vy -= uy * decay
                vx -= ux * decay
            elif hyp <= interaction_rad:
                k = 10
                decay = ((k)/hyp ** 2)
                vy -= uy * decay
                vx -= ux * decay
            vx_arr[j] = vx
            vy_arr[j] = vy
    for i in range(N):
        x_arr[i] += vx_arr[i]
        if x_arr[i] > W or x_arr[i] < 0:
            x_arr[i] = start_x
            y_arr[i] = random.uniform(0, H)
            vx_arr[i] = 1
            vy_arr[i] = random.uniform(-1e-3, 1e-3)
        y_arr[i] += vy_arr[i]
    screen.fill((0,0,0))
    for i in range(N):
        # pygame.draw.circle(screen, colors[i], (x_arr[i], y_arr[i]), 2)
        pygame.draw.rect(screen, (255,255,255), (int(x_arr[i]), int(y_arr[i]), 4, 4))
    for j in range(A):
        pygame.draw.circle(
            screen,
            (255, 0, 255),
            (int(a_x_arr[j]), int(a_y_arr[j])),
            interaction_rad,
            1          # outline thickness
        )
        pygame.draw.circle(screen, (255,255,0), (int(a_x_arr[j]), int(a_y_arr[j])),abs_rad)
    pygame.display.update()
    clock.tick(60)
pygame.quit()