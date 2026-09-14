from TokenProcessor import TokenProcessor as TP
running = True
input_mode = True
output_mode = not input_mode
c = -1
while running:
    c += 1
    if not running:
        break
    if c == 0:
        ...
        inp = input("Enter your input: ")
    else:
        inpt = input("> ")
    if 'run' in inp:
        running = False
        output_mode = True
        input_mode = False
    tokens = inp.split()
    tp = TP(tokens)
    if output_mode:
        tp.basic_func()