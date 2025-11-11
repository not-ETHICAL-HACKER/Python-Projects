def ig():
    i=1
    while True:
        i+=i
        yield i
for j in ig():
    print(j)