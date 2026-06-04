import pygame,random,math
class Particle:
    def __init__(self, x, y, color_name, rgb_color, shape):
        self.c = color_name
        self.color = rgb_color    
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.outer_radius = 100
        self.inner_radius = 25
        self.drag = 0.25
        self.particle_size = 1
        self.shape = shape
        # self.life = 100

    def update(self,p1: 'Particle',p2: 'Particle',c_matrix: dict,s_matrix: dict):
        x1,y1 = p1.x, p1.y
        x2,y2 = p2.x, p2.y
        
        dx = x2 - x1
        dy = y2 - y1
        
        hyp = dx**2+ dy**2

        if hyp < 1 or hyp > self.outer_radius**2:
            return
        
        distance = math.sqrt(hyp)
        
        cosine = dx/distance
        sine = dy/distance
        #! try to make waves by making num of particles large and at start of sim make them all point in a direction and move in it for like 10 frames and then remove the vrctor force and observe whether eave nature of particles can be observed or not
        if hyp < self.inner_radius**2:
            # self.vx += -1/math.sqrt(distance) * cosine
            # self.vy += -1/math.sqrt(distance) * sine
            ...
        elif self.inner_radius**2 < hyp < self.outer_radius**2:
            k = -0.0005
            self.vx += (c_matrix[p1.c][p2.c] * cosine) * 1 / (1 + k * distance)
            self.vy += (c_matrix[p1.c][p2.c] * sine) * 1 / (1 + k * distance)

            func_name = s_matrix[p1.shape][p2.shape][1]
            func = funcs[func_name]
            
            self.vx += func(distance) * cosine * s_matrix[p1.shape][p2.shape][0]
            self.vy += func(distance) * sine * s_matrix[p1.shape][p2.shape][0]
        
    def move(self):
        self.x += self.vx
        self.y += self.vy
    
    def apply_drag(self):
        self.vx *= (1-self.drag)
        self.vy *= (1-self.drag)
    def draw_shape(self,screen, shape, color, x, y):
        if shape == "circle":
            pygame.draw.circle(screen, color, (x, y), self.particle_size)

        elif shape == "square":
            pygame.draw.rect(screen, color,
                            (x-self.particle_size, y-self.particle_size, 2*self.particle_size, 2*self.particle_size))

        elif shape == "triangle":
            points = [
                (x, y-self.particle_size),
                (x-self.particle_size, y+self.particle_size),
                (x+self.particle_size, y+self.particle_size)
            ]
            pygame.draw.polygon(screen, color, points)

    def border_check(self, width, height,circle=False):
        if not circle:
            if self.x < 0:
                self.x = 0
                self.vx *= -0.95
            elif self.x > width:
                self.x = width
                self.vx *= -0.95
            if self.y < 0:
                self.y = 0
                self.vy *= -0.95
            elif self.y > height:
                self.y = height
                self.vy *= -0.95
        else:
            w2 = width//2
            h2 = height//2
            radius = min(w2, h2)
            dx = self.x - w2
            dy = self.y - h2
            dist = math.hypot(dx, dy)
            if dist > radius:
                angle = math.atan2(dy, dx)
                self.x = w2 + radius * math.cos(angle)
                self.y = h2 + radius * math.sin(angle)
                self.vx *= -1
                self.vy *= -1
                
def fix_probs(prob, n, max_len):
    if isinstance(prob, (list, tuple)):
        if not prob:
            prob = [random.random() for _ in range(n)]

        prob = prob[:max_len]
        prob.extend([0] * (max_len - len(prob)))
        
        return [p/sum(prob) for p in prob]
    if isinstance(prob, dict):
        keys = list(prob.keys())[:max_len]
        values = list(prob.values())[:max_len]
        total = sum(values)
        return {k: v/total for k, v in zip(keys, values)}

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
funcs = {
        # "sin":math.sin,
        # "cos":math.cos,
        # "sin_cos":lambda x: math.sin(x)*math.cos(x),
        # "sin^2-cos^2":lambda x: math.sin(x)**2 - math.cos(x)**2,
        # "inv_exp":lambda x: math.exp(-0.01*x),
        # "log_e_1p" :lambda x: math.log1p(abs(x)),
        # "inv_sqrt": lambda x: 1/math.sqrt(abs(x)) if abs(x) > 1 else 0,
        # "atan(sin,cos)":lambda x: math.atan2(math.sin(x),math.cos(x)),
        # "inv_sqr":lambda x: 1/x**2 if abs(x) > 1 else 0,
        # "neg":lambda x:-abs(x),
        # "pos":lambda x:abs(x),
        "mex_hat": lambda x: (1 - x*x/25)*math.exp(-x*x/50),
        "gauss": lambda x: math.exp(-((x-25)**2)/50)
}

n_c = 1
n_s = 1
particles: list[Particle] = []
t_colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta'][:n_c]
prob_func = [random.random() for _ in range(len(funcs))]
t_shapes = ['circle', 'square', 'triangle']
prob_color = [random.random() for _ in range(len(t_colors))]
prob_shape = [random.random() for _ in range(len(t_shapes))]
t_dict_colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255)
}
f_name = list(funcs.keys())
prob_func = fix_probs(prob_func, len(funcs), len(funcs))
prob_color = fix_probs(prob_color, len(t_colors), len(t_colors))
prob_shape = fix_probs(prob_shape, len(t_shapes), len(t_shapes))
shape_size = 0.1

true_color_matrix = {
                c1: {
                    c2: round(random.uniform(-1, 1))/10
                for c2 in t_colors
            } 
        for c1 in t_colors
    }
true_shape_matrix = {
        s1: {
                    s2: (round(random.uniform(-1, 1))/10 ,random.choices(f_name,k=1,weights=prob_func)[0]) 
                for s2 in t_shapes
            } 
        for s1 in t_shapes
    }

for _ in range(1_000):
    x = random.uniform(0, WIDTH)
    y = random.uniform(0, HEIGHT)
    color = random.choices(t_colors, k=1, weights=prob_color)[0]
    c = t_dict_colors[color]
    shape = random.choices(t_shapes, k=1, weights=prob_shape)[0]
    particles.append(Particle(x, y,color,c, shape))

running = True
CELL_SIZE = 100
#! change cell size to interaction radius for accurate particles ,ie, CELL_SIZE = outer_radius

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    
    grid = {}

    # Build grid
    for p in particles:
        # Check this cell and its 8 neighboring cells.
        # Since CELL_SIZE ~= interaction radius,
        # particles farther than one cell away cannot interact.
        # This reduces the search from all particles
        # to only nearby particles.
        cx = int(p.x // CELL_SIZE)
        cy = int(p.y // CELL_SIZE)

        if (cx, cy) not in grid:
            grid[(cx, cy)] = []

        grid[(cx, cy)].append(p)    
    for particle in particles:

        cx = int(particle.x // CELL_SIZE)
        cy = int(particle.y // CELL_SIZE)

        for dx_cell in (-1, 0, 1):
            for dy_cell in (-1, 0, 1):

                nearby = grid.get(
                    (cx + dx_cell, cy + dy_cell),
                    []
                )

                for other in nearby:

                    if particle is other:
                        continue

                    particle.update(
                        particle,
                        other,
                        true_color_matrix,
                        true_shape_matrix
                    )

        particle.apply_drag()
    
    for particle in particles:
        particle.move()
        particle.border_check(WIDTH, HEIGHT)
        particle.draw_shape(screen,particle.shape, particle.color, int(particle.x), int(particle.y))
    pygame.display.flip()