import os
import time

# ANSI colors
ORANGE = "\033[38;5;214m"
WHITE = "\033[97m"
RESET = "\033[0m"

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_frame(ball_x, ball_y, width, height):
    """Draws a single frame of the animation with color."""
    clear_screen()
    frame = []
    for y in range(height):
        row = []
        for x in range(width):
            if y == 0 or y == height - 1:  # Top and bottom walls
                row.append(f"{WHITE}- {RESET}" if x == width - 1 else f"{WHITE}-{RESET}")
            elif x == 0 or x == width - 1:  # Side walls
                row.append(f"{WHITE}|{RESET}")
            elif x == int(ball_x) and y == int(ball_y):  # Ball
                row.append(f"{ORANGE}#{RESET}")
            else:
                row.append(' ')  # Empty space
        frame.append("".join(row))
    print("\n".join(frame))

def bouncing_ball_animation(width=40, height=20, initial_x=5, initial_y=5, initial_dx=1, initial_dy=1, delay=0.1):
    """Simulates a bouncing ball animation using colored ASCII art."""
    ball_x, ball_y = initial_x, initial_y
    dx, dy = initial_dx, initial_dy

    while True:
        draw_frame(ball_x, ball_y, width, height)

        # Update ball position
        ball_x += dx
        ball_y += dy

        # Check for collisions with walls and reverse direction
        if ball_x <= 1 or ball_x >= width - 2:
            dx *= -1
        if ball_y <= 1 or ball_y >= height - 2:
            dy *= -1

        time.sleep(delay)

if __name__ == "__main__":
    try:
        bouncing_ball_animation()
    except KeyboardInterrupt:
        print(f"\n{WHITE}Animation stopped.{RESET}")
