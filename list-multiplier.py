def multiply(l):
    new_l = []
    for e in l:
        new_e = []
        for i in range(len(l)):
            new_e.append(e)
        new_l.append(new_e)
    return new_l

print(multiply(["*", "%", "$"]))