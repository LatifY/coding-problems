from itertools import permutations as perm
from itertools import combinations as comb
import math

p = perm(["a","b","c","d"],3)
c = 0
for a in p:
    print(a)
    c+=1
print(c)
print(math.factorial(3))