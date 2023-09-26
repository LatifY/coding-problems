def max_consec(lst):
    lst.sort()
    print(lst)
    d = [1]
    c = 0
    ind = 0
    for n in range(len(lst)):
        num = lst[n]
        if(n != len(lst)-1):
            if(num+1 == lst[n+1]):
                c+=1
                d[ind] = c
            elif(num == lst[n+1]):
                c+=0
            else:
                c = 1
                ind+=1
                d.append(1)
        else:
            if(lst[-1] == lst[-2]+1):
                d[-1]+=1
    d.sort()
    return d[-1]
            
print(max_consec([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]))