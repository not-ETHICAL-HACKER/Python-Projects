
#!  make this version use the pointers (ones in 3b1b) instead of using particles. (or maybe use both, but make the pointers more prominent)
#! the new version should be more like a flow field, where the pointers are the main focus, and the particles are just there to show the flow of the field. (maybe make the particles fade out over time, so they don't clutter the screen)
#? ex
"""
→  →  ↗  ↑  ↑  ↖  ←
→  ↗  ↑  ↑  ↖  ←  ←
↗  ↑  ↑  ↖  ←  ←  ↙
↑  ↑  ↖  ←  ←  ↙  ↓
↑  ↖  ←  @  ←  ↙  ↓
↖  ←  ←  ←  ↙  ↓  ↓
←  ←  ←  ↙  ↓  ↓  ↘
#! where the @ is the particle, and the ←  ↙  ↓ ↑  ↖ are the pointers, and the # are just empty space. The pointers should be more prominent than the particles, and the particles should fade out over time.
#! remove particles if possible
#! the pointersd should update every frame the pointers are vectors
source ●───────────────▶ head
       (x1,y1)          (x2,y2)
#! normalise and colorcode the pointers based on their direction and magnitude
#? just use a draw func btw (x1,y1) and (x2,y2) are the start and end points of the pointer, respectively
#? dont need the arrow head the line is enough to show the direction of the pointer
"""