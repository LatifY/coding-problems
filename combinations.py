def combinations(*items):
    c = 1
    for i in items:
        if(i !=0):
            c*=i
    return c
print(combinations(2, 3, 4))