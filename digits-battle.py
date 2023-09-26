#odd tek
#even cift

def battle_outcome(num):
    a = []
    new = ""
    for x in str(num):
        a.append(int(x))
    if(len(a) % 2 == 0):
        e = []
        b = 0
        for y in range(int(len(a)/2)):
            e.append(a[b]*10+a[b+1])
            b+=2  
    else:
        e = []
        c = 0
        l = int(len(a)/2)
        for z in range(l+1):
            if(z != l):
                e.append(a[c]*10+a[c+1])
                c+=2
            else:
                e.append(a[c])
    for o in e:
        k = []
        for m in str(o):
            k.append(int(m))
        if(len(k)>1):
            if(k[0] > k[1]):new+=str(k[0])
            if(k[1] > k[0]):new+=str(k[1])
        else:
            new+=str(k[0])
    return int(new)

print(battle_outcome(1234567))
