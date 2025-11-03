import time,sys,random
def marquee(txt:str="Hello World",dir:str="left",cd:float=0.1,num:int=10)->None:
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
        pass