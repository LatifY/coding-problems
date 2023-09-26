def who_goes_free(n, k): 
    if (n == 1): 
        return 1
    else: 
        return (who_goes_free(n - 1, k) + k-1) % n + 1

print("The chosen place is ", who_goes_free(9, 2))