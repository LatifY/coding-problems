def fib_fast(n):
    if n == 0:return 0
    if n == 1: return 1
    return(fib_fast(n-1)+fib_fast(n-2))
print(fib_fast(5))