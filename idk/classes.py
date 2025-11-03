# goofy_popup.py
import time
import tkinter as tk
from tkinter import messagebox
import threading
import sys

DELAY_SECONDS = 10  # change to whatever delay you want

def show_popup():
    root = tk.Tk()
    root.withdraw()  # hide main window
    messagebox.showinfo("Goofy Ahh Notice", "This is a goofy ahh popup! 😜\nYou ran it, so you deserve it.")
    root.destroy()

def main():
    try:
        print(f"Waiting {DELAY_SECONDS} seconds... (press Ctrl+C to cancel)")
        time.sleep(DELAY_SECONDS)
        # run popup on main thread for tkinter
        show_popup()
    except KeyboardInterrupt:
        print("Cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()