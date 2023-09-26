# example [1, 1, 0, 0, 0, 1, 0]
         
def freed_prisoners(prison):
    if(prison[0] == 0):return 0
    rc = 0 # recent index
    c = 0
    for p in range(len(prison)):
        if(p>= rc and prison[p] == 1):
            for a in range(len(prison)):
                if prison[a] == 0:
                    prison[a] = 1
                else:
                    prison[a] = 0
            print(prison) 
            c+=1
            rc = p
    return c
print(freed_prisoners([1, 0, 0, 0, 0, 0, 0])) # 4