#swap: a_list[0], a_list[2] = a_list[2], a_list[0]

#lst = [1, 5, 4, 3, 2, 6] (4)
#tru_lst = [1,2,3,4,5,6]
'''
    print(f"Lst: {lst}")
    print(f"Tru Lst: {tru_lst}")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"x: {x}")
'''
def cycle_length(lst, n):
    tru_lst=[]
    tru_lst = sorted(lst)
    x = 0
    while True:
        a = lst.index(n)
        b = tru_lst.index(n)
        if a == b:return x
        else:
            lst[a],lst[b] = lst[b],lst[a]
            n = lst[a]
            x+=1


print(cycle_length([1, 5, 4, 3, 2, 6], 4))
print(cycle_length([1, 4, 2, 3, 5], 4))
print(cycle_length([1, 5, 4, 3, 2, 6], 4))
print(cycle_length([1, 5, 4, 3, 2, 6], 6))
print(cycle_length([1, 5, 4, 3, 2, 6], 5))
print(cycle_length([1, 4, 2, 3, 5], 4))
print(cycle_length([11, 44, 22, 31, 50], 44))
print(cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 7))
print(cycle_length([43, 81, 88, 93, 17, 32, 19, 11], 93))
print(cycle_length([1, 6, 7, 2, 4, 3, 8, 9, 5], 1))
print(cycle_length([1, 6, 7, 2, 4, 3, 9, 8, 5], 6))
print(cycle_length([1, 6, 7, 2, 4, 3, 9, 8, 5], 5))
print(cycle_length([1, 6, 7, 2, 4, 3, 9, 8, 5], 2))
print(cycle_length([1, 6, 7, 2, 4, 3, 9, 8, 5], 3))