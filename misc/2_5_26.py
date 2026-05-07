def change(char: str, file: str):
    with open(file) as f:
        print(f.read().replace(char, " "))


def num_of(file: str):
    with open(file) as f:
        v = c = u = l = 0
        txt = f.read()
        for ch in txt:
            if ch.lower() in "aeiou":
                v += 1
            elif ch.lower() not in "aeiou" and ch.isalpha():
                c += 1
            if ch.isupper():
                u += 1
            elif ch.islower():
                l += 1


def ETCount(file: str):
    with open(file) as f:
        e = t = 0
        txt = f.read()
        for ch in txt:
            if ch in "Ee":
                e += 1
            elif ch in "Tt":
                t += 1
        return e, t


def replace(file: str, char: str):
    with open(file, "r+") as fin, open("1"+file, "w") as fout:
        lines = fin.readlines()
        l = []
        ll = []
        for line in lines:
            if char in line:
                l.append(line)
                continue
            else:
                ll.append(line)
        fin.seek(0)
        fin.writelines(ll)
        fout.writelines(l)
