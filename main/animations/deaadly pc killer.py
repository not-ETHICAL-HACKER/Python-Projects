with open("even or odd.py","w") as file:
    file.write('''i=int(input("Enter a number: "))\n''')
    for i in range(10**6):
        if i%2==0:
            e="even"
        else:
            e="odd"
        file.write(f'if i=={i}:\n    print("{i} is {e}")\n')