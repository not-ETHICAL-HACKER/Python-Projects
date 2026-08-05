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
fade = pygame.Surface((W, H), pygame.SRCALPHA)
fade.fill((0, 0, 0, 10))   # Last number = alpha (0-255)
""" #! smaller alpha val make the trails longer
fade.fill((0,0,0,3))    # Very long trails
fade.fill((0,0,0,10))   # Medium trails
fade.fill((0,0,0,30))   # Short trails
fade.fill((0,0,0,80))   # Very short trails
"""
clock = pygame.time.Clock()
drag = .1


density = 1 #! out of 100
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
a_x_arr = [a[0] for a in atoms]
a_y_arr = [a[1] for a in atoms]
x_arr = [p[0] for p in particles]
y_arr = [p[1] for p in particles]
vx_arr = [1 for _ in range(N)]
vy_arr = [random.uniform(-1e-3,1e-3) for _ in range(N)]

angles = []
teleported = [False] * N
while running and len(angles) < 2500:
    pygame.display.set_caption(f"Particle Life | angles: {len(angles)}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w, event.h
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)

            fade = pygame.Surface((W, H), pygame.SRCALPHA)
            fade.fill((0, 0, 0, 10))
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
    prev_x_arr = x_arr.copy()
    prev_y_arr = y_arr.copy()

    for i in range(N):
        x_arr[i] += vx_arr[i]
        y_arr[i] += vy_arr[i]
        if x_arr[i] > W or x_arr[i] < 0 or y_arr[i] > H or y_arr[i] < 0:
            angles.append(int(math.degrees(math.atan2(vy_arr[i], vx_arr[i]))))
            teleported[i] = True
            x_arr[i] = start_x
            y_arr[i] = random.uniform(0, H)
            vx_arr[i] = 1
            vy_arr[i] = random.uniform(-1e-3, 1e-3)
    screen.blit(fade, (0, 0))
    for i in range(N):
        if not teleported[i]:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (prev_x_arr[i], prev_y_arr[i]),
                (x_arr[i], y_arr[i])
            )
    # for i in range(N):
    #     # pygame.draw.circle(screen, colors[i], (x_arr[i], y_arr[i]), 2)
    #     pygame.draw.rect(screen, (255,255,255), (int(x_arr[i]), int(y_arr[i]), 4, 4))
    for j in range(A):
        pygame.draw.circle(
            screen,
            (255, 0, 255),
            (int(a_x_arr[j]), int(a_y_arr[j])),
            interaction_rad,
            1          # outline thickness
        )
        pygame.draw.circle(screen, (255,255,0), (int(a_x_arr[j]), int(a_y_arr[j])),abs_rad)
    teleported = [False] * N
    pygame.display.update()
    clock.tick(60)
pygame.quit()
import matplotlib.pyplot as pyplt
pyplt.hist(angles,bins=180)
pyplt.show()