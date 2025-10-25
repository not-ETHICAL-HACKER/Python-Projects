import time
import sys

def loading_animation():
    print("Loading", end="", flush=True)
    for _ in range(2):
        for i in range(5):
            sys.stdout.write("." * i + "\rLoading" + "." * i)
            sys.stdout.flush()
            time.sleep(0.5)
    print("\nDone!")

# --- main program ---
print("sadge :(")
print("it fucking worked")

loading_animation()
