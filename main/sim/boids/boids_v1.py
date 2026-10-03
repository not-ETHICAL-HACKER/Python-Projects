import pygame,math,random
pygame.init()
random.seed(0)
W,H = 500,500
S = 10
N = 100
draw_help = not True
vector_len = 25
fade_const = 200
CELL_SIZE = 100

screen = pygame.display.set_mode((W,H), pygame.RESIZABLE)
pygame.display.set_caption("My Simulation")
fade = pygame.Surface((W, H), pygame.SRCALPHA)
fade.fill((0, 0, 0, fade_const))   # Last number = alpha (0-255) #! smaller alpha val make the trails longer
grid_info = {(cx//CELL_SIZE,cy//CELL_SIZE):{"boids_in_cell":[],"avg_pos": (None,None),"avg_vel": (None,None)} for cx in range(0,W,CELL_SIZE) for cy in range(0,H,CELL_SIZE)}
class boids:
    def __init__(self,x:float,y:float,color:tuple[int,int,int]):
        self.x = x
        self.y = y
        self.color = color
        self.vx = random.uniform(-1,1)
        self.vy = random.uniform(-1,1)
        self.inner_radius = 50
        self.inner_radius_sqr = self.inner_radius ** 2
        self.max_radius = 100
        self.max_speed = 2
        self.max_radius_sqr = self.max_radius ** 2
        self.fov = math.pi * 3/4
        self.fov_cos = math.cos(self.fov)
        self.alignment_str = .01
        self.seperation_str = .25
        self.cohesion_str = 1
    
    def __repr__(self):
        return f"boids(x={self.x:.2f},y={self.y:.2f})"
    
    def update(self):
        self.vx = max(-self.max_speed, min(self.max_speed, self.vx))
        self.vy = max(-self.max_speed, min(self.max_speed, self.vy))
        self.x += self.vx
        self.y += self.vy
    
    def alignment(self,avg_vel):
        avg_vx,avg_vy = avg_vel
        if avg_vx is None or avg_vy is None:
            return
        align_vx = avg_vx - self.vx
        align_vy = avg_vy - self.vy
        magnitude = max(1e-6,math.hypot(align_vx,align_vy))
        ux = align_vx/magnitude
        uy = align_vy/magnitude
        self.vx += ux * self.alignment_str
        self.vy += uy * self.alignment_str

    def seperation(self,boids:list["boids"]):
        for other in boids:
            if other is self:
                continue
            dx = other.x - self.x
            dy = other.y - self.y 
            dist_sqr = dx**2 + dy**2
            if dist_sqr < self.inner_radius_sqr:
                dist = math.sqrt(dist_sqr)
                if dist > 0:
                    ux = dx / dist
                    uy = dy / dist
                    dot = ux * self.vx + uy * self.vy
                    if dot > self.fov_cos:
                        self.vx += -ux * self.seperation_str
                        self.vy += -uy * self.seperation_str
    
    def cohesion(self,avg_pos):
        avg_x,avg_y = avg_pos
        if avg_x is None or avg_y is None:
            return
        dx = avg_x - self.x
        dy = avg_y - self.y
        dist = max(1e-6,math.hypot(dx,dy))
        ux = dx / dist
        uy = dy / dist
        dot = ux * self.vx + uy * self.vy
        if dot > self.fov_cos:
            self.vx += ux * self.cohesion_str
            self.vy += uy * self.cohesion_str
    
    def border_check(self):
        if self.x <= 0 + S:
            self.x = W - S
            # self.vx *= -1
        elif self.x >= W - S:
            self.x = 0 + S
            # self.vx *= -1
        if self.y <= 0 + S:
            self.y = H - S
            # self.vy *= -1
        elif self.y >= H - S:
            self.y = 0 + S
            # self.vy *= -1
running = True
chuds = [boids(random.uniform(0,W),random.uniform(0,H),(255,255,255)) for _ in range(N)]
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            W, H = event.w,event.h
            screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
            fade = pygame.Surface((W, H), pygame.SRCALPHA)
            fade.fill((0, 0, 0, fade_const))
            grid_info = {(cx//CELL_SIZE,cy//CELL_SIZE):{"boids_in_cell":[],"avg_pos": (None,None),"avg_vel": (None,None)} for cx in range(0,W,CELL_SIZE) for cy in range(0,H,CELL_SIZE)}
            
    grid_info = {(cx//CELL_SIZE,cy//CELL_SIZE):{"boids_in_cell":[],"avg_pos": (None,None),"avg_vel": (None,None)} for cx in range(0,W,CELL_SIZE) for cy in range(0,H,CELL_SIZE)}
    for chud in chuds:
        cx = int(chud.x // CELL_SIZE)
        cy = int(chud.y // CELL_SIZE)
        grid_info[(cx,cy)]["boids_in_cell"].append(chud)
        grid_info[(cx,cy)]["avg_pos"] = (sum(b.x for b in grid_info[(cx,cy)]["boids_in_cell"]) / len(grid_info[(cx,cy)]["boids_in_cell"]),sum(b.y for b in grid_info[(cx,cy)]["boids_in_cell"]) / len(grid_info[(cx,cy)]["boids_in_cell"])) #! not scary spagetti just some bs list comprehension 
        grid_info[(cx,cy)]["avg_vel"] = (sum(b.vx for b in grid_info[(cx,cy)]["boids_in_cell"]) / len(grid_info[(cx,cy)]["boids_in_cell"]),sum(b.vy for b in grid_info[(cx,cy)]["boids_in_cell"]) / len(grid_info[(cx,cy)]["boids_in_cell"]))
    for (cx,cy), cell_data in grid_info.items():
        ...
        for dx in (-1,0,1):
            for dy in (-1,0,1):
                neighbor_cell = (cx + dx, cy + dy)
                if neighbor_cell in grid_info:
                    neighbor_boids:list[boids] = grid_info[neighbor_cell]["boids_in_cell"]
                    avg_vel = grid_info[neighbor_cell]["avg_vel"]
                    avg_pos = grid_info[neighbor_cell]["avg_pos"]
                    for chud in cell_data["boids_in_cell"]:
                        chud.alignment(avg_vel)
                        chud.cohesion(avg_pos)
                        chud.seperation(neighbor_boids)
    for chud in chuds:
        magnitude = math.hypot(chud.vx,chud.vy)
        ratio = min(1,magnitude / chud.max_speed)
        chud.color = (int(255 * ratio),) * 3
        chud.update()
        chud.border_check()
    screen.blit(fade, (0, 0))
    for chud in chuds:
        pygame.draw.rect(screen,chud.color,(int(chud.x),int(chud.y),3,3))
    if draw_help:
        for (cx,cy), cell_data in grid_info.items():
            avg_x,avg_y = cell_data["avg_pos"]
            avg_vx,avg_vy = cell_data["avg_vel"]
            if (avg_x is not None and avg_y is not None) and (avg_vx is not None and avg_vy is not None):
                magnitude = math.hypot(avg_vx,avg_vy)
                if magnitude > 0:
                    ux = avg_vx / magnitude
                    uy = avg_vy / magnitude
                    pygame.draw.line(screen,(0,255,0),(int(avg_x),int(avg_y)),(int(avg_x + ux * vector_len),int(avg_y + uy * vector_len)),1)
                    pygame.draw.circle(screen,(0,0,255),(int(avg_x + ux * vector_len),int(avg_y + uy * vector_len)),3)
                pygame.draw.rect(screen,(255,0,0),(int(avg_x),int(avg_y),5,5))
        for cx in range(0,W,CELL_SIZE):
            for cy in range(0,H,CELL_SIZE):
                pygame.draw.line(screen,(255,255,255),(0,cy),(W,cy),1)
                pygame.draw.line(screen,(255,255,255),(cx,0),(cx,H),1)
    pygame.display.update()
    clock.tick(60)
    

pygame.quit()