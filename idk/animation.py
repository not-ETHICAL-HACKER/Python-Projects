import time,sys,random
def marquee(txt:str=" Hello World ",dir:str="left",cd:float=0.1,num:int=10)->None:
    """"Creates a marquee animation in the console."""
    if dir not in ["left","right"]:
        raise ValueError("Direction must be 'left' or 'right'")
    if dir=="left":
        while True:
            sys.stdout.write((txt)*num+"\r")
            sys.stdout.flush()
            time.sleep(cd)
            txt=txt[1:]+txt[0]
    else:
        while True:
            sys.stdout.write((txt)*num+"\r")
            sys.stdout.flush()
            time.sleep(cd)
            txt=txt[-1]+txt[:-1]
def bouncy(txt:str=" Hello World ",cd:float=0.1)->None:
    """creates a bouncy animation in the console."""
    while True:
        for i in range(len(txt)//2):
            sys.stdout.write(" "*i+txt+"\r")
            sys.stdout.flush()
            time.sleep(cd)
        for i in range(len(txt)//2,0,-1):
            sys.stdout.write(" "*i+txt+"\r")
            sys.stdout.flush()
            time.sleep(cd)
def majic(txt:str):
    while True:
        for i,ch in enumerate(txt):
            sys.stdout.write(" "* (len(txt)-i) + txt[-i] + "\r")
            sys.stdout.flush()
            time.sleep(0.1)
import winsound as w
l=list("abcdefghijklmnopqrstuvwxyz")
import sys as s
import time
def magnet(frames:list,fps:float=60,Title:bool=False):
    a=0
    new=False
    if not Title:
        while True:
            if new:
                print()
                new=False
            for i in range(len(frames)):
                s.stdout.write((" "*(i-a))+(frames[i-a])+("\r"))
                s.stdout.flush()
                w.Beep(500,100)
                time.sleep(1/fps)
            a+=1
            if a==len(frames):
                a=0
                new=True
    else:
        while True:
            for i in range(len(frames)):
                a=len(frames)-1
                #for alternate animation ie,|\-/ at the same time at diff animate times ig

magnet(l)