def list_of_multiples (num, length):
    nums = []
    for i in range(1,length+1):
        nums.append(i*num)
    return nums

print(list_of_multiples(7, 5))