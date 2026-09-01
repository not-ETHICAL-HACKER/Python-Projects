u = [chr(i) for i in range(65, 91)]
l = [chr(i) for i in range(97, 97+26)]
def encrypt(txt: str , key: int) -> str:
    enc = ""
    for k in txt:
        if k.isupper():
            enc += u[((ord(k)+key)-65) % 26]
        elif k.islower():
            enc += l[((ord(k)+key)-97) % 26]
        else:
            enc += k
    return enc


def decrypt(txt: str , key:int) -> str:
    dec = ""
    for k in txt:
        if k.isupper():
            dec += u[((ord(k)-key)-65) % 26]
        elif k.islower():
            dec += l[((ord(k)-key)-97) % 26]
        else:
            dec += k
    return dec