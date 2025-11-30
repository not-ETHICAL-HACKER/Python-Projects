import plotly.graph_objects as go
import matplotlib.pyplot as plt
import numpy as np
import math
from colorama import Fore, init, Style, Back
c1 = Fore.BLUE+Style.BRIGHT+Back.BLACK
c2 = Fore.RED+Style.BRIGHT+Back.BLACK
c3 = Fore.GREEN+Style.BRIGHT+Back.BLACK
init(autoreset=True)
a=np.linspace(0,2*math.pi,3600)
tan_vals = np.tan(a)
cot_vals = 1 / np.tan(a)

# Mask large values (near asymptotes)
tan_vals[np.abs(tan_vals) > 50] = None
cot_vals[np.abs(cot_vals) > 50] = None

fig = go.Figure()

# tan(x)
fig.add_trace(go.Scatter(
    x=a, y=tan_vals,
    mode='lines',
    name='tan(x)',
    line=dict(width=2)
))

# cot(x)
fig.add_trace(go.Scatter(
    x=a, y=cot_vals,
    mode='lines',
    name='cot(x)',
    line=dict(width=2)
))

# Vertical asymptotes
fig.add_vline(x=np.pi/2, line_dash='dash', line_color='black')
fig.add_vline(x=3*np.pi/2, line_dash='dash', line_color='black')

fig.update_layout(
    title="tan(x) and cot(x) — Plotly Interactive Graph",
    xaxis_title="x (radians)",
    yaxis_title="Value",
    yaxis=dict(range=[-31.4, 31.4]),
    template="plotly_dark",
    showlegend=True
)

fig.show()
for i in a:
    break
    print(f"{Back.BLACK+Fore.WHITE+Style.BRIGHT}{i:.3f} =>>\t{c1}Sin = {math.sin(i):.3f}\t{c2}Cos = {math.cos(i):.3f}\t{c3}Tan = {math.tan(i):.3f}")
