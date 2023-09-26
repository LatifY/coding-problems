from itertools import combinations

def extract_primes(num):
    a = []
    for i in str(num):
        a.append(int(i))
    perm = combinations(a,0)
    for per in perm:
        print(per)
extract_primes(1313)