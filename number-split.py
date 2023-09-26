def number_split(n):
    a=[]
    if(n%2==0):a.extend([int(n/2),int(n/2)])
    else:a.extend([int(n/2-0.5),int(n/2+0.5)])
    return a

#alternative
import math
def number_split2(n):
	return [math.floor(n/2), math.ceil(n/2)]

#alternative2
import math
number_split3=lambda n:[n//2,n-n//2]

print(number_split(4)) # [2, 2]
print(number_split(10)) # [5, 5]
print(number_split(11)) # [5, 6]
print(number_split(0)) # [0, 0]
print(number_split(1)) # [0, 1]
print(number_split(-4)) # [-2, -2]
print(number_split(-5)) # [-3, -2]
print(number_split(-9)) # [-5, -4]