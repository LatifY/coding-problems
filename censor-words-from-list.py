def censor_string(t,l,c):
    a=""
    l = list((a.lower() for a in l))
    for x in t.split():
        if(x.lower() in l):a += len(x)*c+" "
        else:a+=x+" "
    return a[:-1]

print(censor_string("Today is a Wednesday!", ["Today", "a"], "-"))