def matrix(txt:str)->str:
    b=""
    c=0
    while c<len(txt):
        for i in range(65, 91):
            a=""+b
            print(chr(i))
            if chr(i)==txt[c]:
                c+=1
                b+=chr(i)
    return a
def matrix_2(txt: str) -> str:
    b = ""
    c = 0
    while c < len(txt):
        for i in range(65, 91):
            print(chr(i))
            if chr(i) == txt[c]:
                b += chr(i)
                c += 1
                break           # stop scanning A–Z once matched
    #! improve the idea of matrix the moviening letters
    return b

print(matrix_2("HELLO"))