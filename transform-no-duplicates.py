def setify(lst):
    lst2 = []
    for e in lst:
        if e not in lst2:
            lst2.append(e)
    return lst2

print(setify([1, 3, 3, 5, 5]))