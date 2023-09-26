p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199] 
def sum_primes(lst):
    s = 0
    for i in lst:
        if i in p:
            s+=i
    if s != 0:return s

#alternative
sum_primes2 = lambda l: sum(x for x in l if 2 in [x, 2**x % x]) if l else None

print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    