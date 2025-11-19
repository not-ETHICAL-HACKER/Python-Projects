l=[]
def two_d_matrix(rows, cols, val=0):
    global l
    l+= [[val for i in range(cols)] for j in range(rows)]
    return l
print(two_d_matrix(3, 4, 7))