import pygame
import numpy as np

pygame.init()
WIDTH,HEIGHT = 1000,700
N = 1000

x_arr = np.random.randint(0,WIDTH,N).astype(float)
y_arr = np.random.randint(0,HEIGHT,N).astype(float)

vx_arr = np.random.rand(N)
vy_arr = np.random.random(N)
color_dict = {
    "RED":(255,0,0),
    "GREEN":(0,255,0),
    "BLUE":(0,0,255)
}

palette = np.array([
    (255,0,0),
    (0,255,0),
    (0,0,255)
])

color_to_idx = {
    'RED': 0,
    'GREEN': 1,
    'BLUE': 2,
    'WHITE':3
}
color_idx = np.random.randint(0, len(palette), N)
colors = palette[color_idx]

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")
font = pygame.font.SysFont(None, 30)

typing = False
text = ""
running = True
clock = pygame.time.Clock()
drag = .1

true_color_matrix = np.random.randint(-1, 2, (len(palette), len(palette)))
true_color_matrix = np.round(true_color_matrix,0)
force_matrix = true_color_matrix[color_idx[:, None], color_idx[None, :]]

mouse_decay_const = .01
decay_const = .1
inner_rad = 10
outer_rad = 1500

while running:
    fps = clock.get_fps()
    pygame.display.set_caption(f"Particle Life | FPS: {fps:.1f}")
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
        elif event.type == pygame.KEYDOWN:

            # Press TAB to start/stop typing
            if event.key == pygame.K_TAB:
                typing = not typing

            elif typing:

                if event.key == pygame.K_RETURN:

                    parts = text.split()

                    if len(parts) == 2:

                        cmd, value = parts

                        try:
                            value = float(value)

                            if cmd == "outer":
                                outer_rad = value

                            elif cmd == "inner":
                                inner_rad = value

                            elif cmd == "drag":
                                drag = value

                            elif cmd == "decay":
                                decay_const = value

                            print(f"{cmd} = {value}")

                        except ValueError:
                            print("Invalid number!")
                    elif len(parts) == 3:
                        c1, c2, value = parts

                        c1 = c1.upper()
                        c2 = c2.upper()

                        if c1 in color_to_idx and c2 in color_to_idx:
                            try:
                                value = float(value)

                                i = color_to_idx[c1]
                                j = color_to_idx[c2]

                                true_color_matrix[i, j] = value
                                force_matrix = true_color_matrix[color_idx[:, None], color_idx[None, :]]

                                print(f"{c1} -> {c2} = {value}")

                            except ValueError:
                                print("Value must be a number.")
                        else:
                            print("Unknown color.")
                    text = ""
                    typing = False
                    
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

                else:
                    text += event.unicode
    mouse_force = 1
    keys = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()
    buttons = pygame.mouse.get_pressed()

    for key in range(pygame.K_0, pygame.K_9 + 1):
        if keys[key]: #! changes force expereienceed based on number pressed
            mouse_force = key - pygame.K_0
    rx = np.random.uniform(-0.1, 0.1, N)
    ry = np.random.uniform(-0.1, 0.1, N)
    dx = x_arr[:,None] - x_arr[None,:]
    dy = y_arr[:,None] - y_arr[None,:]
    dist2 = dx*dx + dy*dy
    mask = dist2 < outer_rad*outer_rad
    dist = np.sqrt(dist2, where=mask, out=np.full_like(dist2, np.inf))
    dist[dist == 0] = np.inf #! to prevent dx checking a particle with its own coords
    inner = dist < inner_rad
    outer = dist > outer_rad
    ux = dx / dist
    uy = dy / dist
    interaction_force = force_matrix.copy()
    overlap_factor = 1.0 - (dist[inner] / inner_rad)
    interaction_force[inner] = -2.0 * overlap_factor
    interaction_force[outer] = 0.0
    dmx = mx - x_arr
    dmy = my - y_arr

    mouse_dist = np.hypot(dmx, dmy)
    mouse_dist = np.maximum(mouse_dist, 0.1)
    
    decay_mouse = np.exp(-mouse_dist*mouse_decay_const)
    decay = np.zeros_like(dist)
    mask = ~outer
    decay[mask] = np.exp(-dist[mask] * decay_const)
    
    if buttons[0]:
        umx = dmx / mouse_dist * mouse_force
        umy = dmy / mouse_dist * mouse_force   
    elif buttons[2]:
        umx = -dmx / mouse_dist * mouse_force
        umy = -dmy / mouse_dist * mouse_force
    else:
        umx,umy = 0,0
    
    fx = ux * interaction_force * decay
    fy = uy * interaction_force * decay
    
    ax = fx.sum(axis=1)
    ay = fy.sum(axis=1)
    
    vx_arr += umx*decay_mouse + rx + ax
    vy_arr += umy*decay_mouse + ry + ay
    
    vx_arr *= 1 - drag
    vy_arr *= 1 - drag
    
    x_arr += vx_arr
    y_arr += vy_arr
    
    if running:
        left = x_arr < 0
        right = x_arr > WIDTH

        vx_arr[left | right] *= -0.90
        x_arr[left] = -x_arr[left]
        x_arr[right] = 2*WIDTH - x_arr[right]   
        top = y_arr < 0
        bottom = y_arr > HEIGHT

        vy_arr[top | bottom] *= -0.90
        y_arr[top] = -y_arr[top]
        y_arr[bottom] = 2*HEIGHT - y_arr[bottom]
    screen.fill((0,0,0))
    if typing:
        pygame.draw.rect(screen, (40,40,40), (20,20,250,40))
        pygame.draw.rect(screen, (255,255,255), (20,20,250,40), 2)

        surface = font.render(text, True, (255,255,255))
        screen.blit(surface, (30,30))
    for i in range(N):
        # pygame.draw.circle(screen, colors[i], (x_arr[i], y_arr[i]), 2)
        pygame.draw.rect(screen, colors[i], (int(x_arr[i]), int(y_arr[i]), 4, 4))
    pygame.display.update()
    clock.tick(60)
pygame.quit()