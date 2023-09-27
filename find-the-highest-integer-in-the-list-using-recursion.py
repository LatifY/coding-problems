def find_highest(lst, i = 0, h = 0):
    n = lst[i]
    if(n > h):h = n
    if(i == len(lst) - 1):return h
    return find_highest(lst, i+1, h)


print(find_highest([8]))
print(find_highest([-1, 3, 5, 6, 99, 12, 2]))
print(find_highest([0, 12, 4, 87]))