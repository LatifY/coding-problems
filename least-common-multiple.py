def lcm(n):
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

print(lcm([1]))
print(lcm([5, 5, 5])    )
print(lcm([67, 34, 12, 3, 2]))
print(lcm([79, 18, 7, 3, 1]))
print(lcm([10, 20, 30, 40, 50]))
print(lcm([2, 3, 5, 7, 11, 13, 17]))
print(lcm([91, 92, 93, 94, 95]))

'''
a = [100, 200, 150]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
  lcm = lcm*i//math.gcd(lcm, i)
print(lcm)
'''