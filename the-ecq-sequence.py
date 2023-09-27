import time as t
SEQ = [1,2]



def find_gcd_loop(x:int, y:int):
    small_number = 0
    if(x > y):
        small_number = y
    else:
        small_number = x

    for i in range(1, small_number+ 1):
        if(x % i == 0 and y % i == 0):
            value = i

    return value


def find_gcd_recursive():
    pass


def ecg_seq_index(n):
    global SEQ

    count = 3
    while n not in SEQ:
        if count in SEQ:
            count+=1
            continue
        
        last_number = SEQ[-1]
        gcd = find_gcd_loop(count, last_number)
        if(gcd == 1):
            count+=1
            continue
        else:
            SEQ.append(count)
            count = 3
            continue
    value = SEQ.index(n)
    SEQ = [1,2]
    return value

print(ecg_seq_index(3))
print(ecg_seq_index(5))
print(ecg_seq_index(7))