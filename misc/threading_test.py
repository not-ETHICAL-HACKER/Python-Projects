import threading
import time
import sys

# This variable allows the threads to communicate
stop_loading = False

def loading_bar():
    """This function runs in the background."""
    chars = ["|", "/", "-", "\\"]
    progress = 0
    while not stop_loading:
        for char in chars:
            if stop_loading: break
            
            # Create a simple visual bar
            bar = "#" * (progress % 20)
            sys.stdout.write(f"\r[{char}] Processing: {bar:<20} | Type something: ")
            sys.stdout.flush()
            
            time.sleep(0.1)
            progress += 1
    print("\n[!] Loading thread stopped.")

# 1. Start the background thread
# 'daemon=True' means it will kill itself when the main program ends
t = threading.Thread(target=loading_bar, daemon=True)
t.start()

# 2. Keep the main thread open for input
try:
    while True:
        user_input = input() # The loading bar keeps moving while this waits!
        if user_input.lower() == 'exit':
            stop_loading = True
            break
        print(f"\n[You typed: {user_input}]")
except KeyboardInterrupt:
    stop_loading = True

print("Game Over.")