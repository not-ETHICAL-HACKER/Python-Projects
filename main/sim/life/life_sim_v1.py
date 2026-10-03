import pygame,math,random
pygame.init()
random.seed(0)
W,H = 500,500
S = 10
N = 250
F = 10
vector_len = 25
fade_const = 10
CELL_SIZE = 100
chuds = [
    (   
        "C_"+ chr((_ % 26) + 65) + str(_), #! food_id
        None, #! target id
        (random.randint(0,W),random.randint(0,H)), #? creature coords
        True, #? wander mode
        0, #? age
        random.gauss(100,10), #? energy
        )
    for _ in range(N)]
max_rad = 100
max_rad_sqr = max_rad ** 2
food_arr = [
    (   
        "F_" + chr((_ % 26) + 65) + str(_), #! food_id
        (random.randint(0,W),random.randint(0,H)), #? food coords
        random.uniform(1000,2000) #? food hp
        ) 
    for _ in range(F)]
min_food_dist = 10
min_food_dist_sqr = min_food_dist ** 2

screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")
fade = pygame.Surface((W, H), pygame.SRCALPHA)
fade.fill((0, 0, 0, fade_const))   # Last number = alpha (0-255) #! smaller alpha val make the trails longer
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w,event.h
            chuds = [
                (   
                    "C_"+ chr((_ % 26) + 65) + str(_), #! food_id
                    None, #! target id
                    (random.randint(0,W),random.randint(0,H)), #? creature coords
                    True, #? wander mode
                    0, #? age
                    random.gauss(100,10), #? energy
                    )
                for _ in range(N)]
            food_arr = [
                (   
                    "F_" + chr((_ % 26) + 65) + str(_), #! food_id
                    (random.randint(0,W),random.randint(0,H)), #? food coords
                    random.uniform(1000,2000) #? food hp
                    ) 
                for _ in range(F)]
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
            fade = pygame.Surface((W, H), pygame.SRCALPHA)
            fade.fill((0, 0, 0, fade_const))
    
    t = pygame.time.get_ticks() / 1000
    for i,chud in enumerate(chuds):
        c_id,t_id,pos,wander,age,energy = chud
        age += 1
        energy -= random.uniform(1e-3,1e-1)
        wander = True if energy > 100 else False
        chuds[i] = (c_id,t_id,pos,wander,age,energy)
    chuds = [chud for chud in chuds if chud[-1] > 0]
    food_arr = [foid for foid in food_arr if foid[-1] > 0]
    for j,foid in enumerate(food_arr):
        f_id,f_pos,f_hp = foid
        # if f_hp <= 0:
        #     food_arr[j] = f_id,(random.randint(0,W),random.randint(0,H)),random.uniform(10,20)
        if j % 2 == 0:
            f_x,f_y = f_pos
            f_x += math.cos(2*t)
            f_y += math.sin(2*t)
        if j % 2 == 1:
            f_x,f_y = f_pos
            f_x += math.cos(t)
            f_y += math.sin(t)
        food_arr[j] = f_id,(f_x,f_y),f_hp
    for i,chud in enumerate(chuds):
        c_id,t_id,pos,wander,age,energy = chud
        c_x,c_y = pos
        for j,foid in enumerate(food_arr):
            
            f_id,f_pos,f_hp = foid
            f_x,f_y = f_pos
            if wander:
                c_x += random.randint(-1,1)
                c_y += random.randint(-1,1)
            else:
                dx = f_x - c_x
                dy = f_y - c_y
                ux,uy = 0,0
                dist_sqr = dx**2 + dy**2
                if dist_sqr < max_rad_sqr:
                        hyp = math.sqrt(dist_sqr)
                        ux = dx/hyp * random.random()
                        uy = dy/hyp * random.random()
                        noise = random.gauss(0,1)
                        ux += noise
                        uy += noise
                        if t_id is None: #! detecting prey during hunt
                            t_id = f_id
                            c_x += ux
                            c_y += uy
                        elif dist_sqr < max_rad_sqr and t_id:
                            c_x += ux
                            c_y += uy
                        if dist_sqr < min_food_dist_sqr:
                            gain = random.gauss(10,10)
                            f_hp -= gain
                            energy += gain
                            c_x += -ux
                            c_y += -uy
                            t_id = None
                        else:
                            f_hp += random.uniform(5,10) #! fotosynthesis
            food_arr[j] = f_id,(f_x,f_y),f_hp 
        chuds[i] = c_id,t_id,(c_x,c_y),wander,age,energy
    screen.blit(fade, (0, 0))
    for chud in chuds:
        c_id,t_id,pos,wander,age,energy = chud
        pygame.draw.rect(screen,(255,)*3,(int(pos[0]),int(pos[1]),3,3))
    for foid in food_arr:
        f_id,f_pos,f_hp = foid
        pygame.draw.rect(screen,(0,255,0),(int(f_pos[0]),int(f_pos[1]),min_food_dist,min_food_dist))
    pygame.display.update()
    clock.tick(60)

pygame.quit()