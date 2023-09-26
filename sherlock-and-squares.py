from math import sqrt
def squares(a, b):
    x=0
    for i in range(a,b+1):
        if(sqrt(i)%1 == 0):x+=1
    return x
	
print(squares(35, 70))
print(squares(100, 1000))
print(squares(3, 9))
print(squares(17, 24))
print(squares(433, 100000))
print(squares(1, 1000000000))
print(squares(89784519, 103811134))
print(squares(50979851, 733216221))