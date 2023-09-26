def id_mtrx(n):
    if(type(n) != int):
        return "Error"
    a=[]
    for i in range(abs(n)):
        b=[]
        for j in range(abs(n)):b.append(1) if j == i else b.append(0)
        a.append(b)
    return a if n>0 else a[::-1]
print(id_mtrx(5))
print(id_mtrx(2))
print(id_mtrx(-3))
