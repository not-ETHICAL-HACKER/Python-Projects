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
    """creates a magnet animation in the console."""
    while True:
        for i in range(len(txt)//2):
            sys.stdout.write(" "*i+txt+"\r")
            sys.stdout.flush()
            time.sleep(cd)
        for i in range(len(txt)//2,0,-1):
            sys.stdout.write(" "*i+txt+"\r")
            sys.stdout.flush()
            time.sleep(cd)
bouncy()