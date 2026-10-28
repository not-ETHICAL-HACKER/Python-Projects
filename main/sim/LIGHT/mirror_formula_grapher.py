import matplotlib.pyplot as plt
import numpy as np
mirror_types = {"concave" : -1, "convex" : 1}
mirror_type = "concave"
focal_length = 10.0
start_u = 0
end_u = 100
num = 10**3
a = [round(float(x), 3) for x in np.linspace(start_u, end_u, num)]
def mirror_formula(mirror_type: str, f: float):
    if mirror_type not in mirror_types:
        raise ValueError(f"Invalid mirror type: {mirror_type}. Must be 'concave' or 'convex'.")
    m_type = mirror_types[mirror_type]
    for u in a:
        sim_u = -max(u, 0.0001)  # Prevent division by zero
        v = (m_type * f * sim_u) / (m_type * f - sim_u)
        yield u,v
    return u,v

plt.ion()
fig, ax = plt.subplots()

fig.patch.set_facecolor("black")
ax.set_facecolor("black")

line, = ax.plot(range(len(a)), a, color="white", linewidth=1.5)

ax.tick_params(colors="white")
c = 0
for obj,img in mirror_formula(mirror_type,focal_length):
    plt.pause(.5) if c == 0 else plt.pause(1e-6)
    line.set_ydata(img)
    ax.set_title(f"Mirror Formula Animation \n Object Position: {obj:.2f} | Image Position: {img:.2f}", color="white")
    c += 1

# Finish in green
line.set_color("green")
plt.pause(0.5)

plt.ioff()
plt.show()
