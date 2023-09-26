import math
def lcm_of_list(n):
    x=n[0]
    for i in n[1:]:
        if x > i: 
            small = i 
        else: 
            small = x 
        for y in range(1, small+1): 
            if((x % y == 0) and (i % y == 0)): 
                gcd = y
        x = x*i//gcd   
    return x

print(lcm_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) #2520
print(lcm_of_list([13, 6, 17, 18, 19,20, 37])) #27965340
print(lcm_of_list([44, 64, 12, 17, 65])) #2333760
print(lcm_of_list([200, 30, 18, 11, 8, 64, 34])) #2692800