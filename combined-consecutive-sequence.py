def consecutive_combo(lst1, lst2):
    lst3 = []
    lst3 += lst1 + lst2
    lst3.sort()
    fc = lst3[0]
    for i in range(len(lst3)):
        if(fc+i != lst3[i]):return False
    return True

print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))