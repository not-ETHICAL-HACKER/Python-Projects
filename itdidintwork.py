print("sadge :(")
print("it fucking worked")
import time,sys,threading
def loading_animation(l:int):
    while True:
        for i in range(5):
            sys.stdout.write((" "*l)+"\r" + "." * i + " " * (5 - i))
            sys.stdout.flush()
            time.sleep(0.5)
t=threading.Thread(target=loading_animation,args=(100,))
t.daemon=True
print("Loading",end=" ")
t.start()
time.sleep(10)