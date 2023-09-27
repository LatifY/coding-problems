def is_same(lst):
    f = lst[0]
    for i in lst:
        if i != f:
            return False
    return True

def reverse_lst(lst):
    new = []
    for i in lst:
        i.reverse()
        new.append(i)
    return new

def is_horizontal(lst):
    value = False
    for i in lst:
        if(is_same(i)): value = True
        else: 
            value = False
            break
    return value

def is_vertical(lst):
    new = []
    for i in range(len(lst[0])):
        new.append([])
        for x in lst:
            new[i].append(x)
    return is_horizontal(new)

def get_diag(lst,mx,my):
    diag = []
    while True:
        try:item= lst[my][mx]
        except:break
        diag.append(item)
        mx +=1
        my-=1
        if(mx < 0 or my < 0):break
    return diag

def is_diagnosis(lst):
    o = []
    l_row = len(lst[-1])
    l_col = len(lst)
    for y in range(1, l_col):
        o.append(get_diag(lst, 0, y))

    if(l_row > 2):
        for x in range(1, l_row - 1):
            o.append(get_diag(lst, x, l_col - 1))
    value = is_horizontal(o)
    return value

def is_wristband(lst):
    if(is_horizontal(lst)):return True
    if(is_vertical(lst)):return True
    if(is_diagnosis(lst)): return True
    print(reverse_lst(lst))
    if(is_diagnosis(reverse_lst(lst))): return True
    return False

print(is_wristband(
[['A', 'B', 'C'], 
['C', 'A', 'B'], 
['B', 'C', 'A'], 
['A', 'B', 'C']]))


input()