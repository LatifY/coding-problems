def bitwise_and(n1, n2):
    n1 = '{0:08b}'.format(n1)
    n2 = '{0:08b}'.format(n2)
    print(n1)
    print(n2)
    n3 = ""
    for i in range(8):
        if(n1[i] == "1" and n1[i] == n2[i]):n3+="1"
        else:n3+="0"
    return n3

def bitwise_or(n1, n2):
    n1 = '{0:08b}'.format(n1)
    n2 = '{0:08b}'.format(n2)
    n3 = ""
    for i in range(8):
        if((int(n1[i])+int(n2[i])) in [1,2]):n3+="1"
        else:n3+="0"
    return n3

def bitwise_xor(n1, n2):
    n1 = '{0:08b}'.format(n1)
    n2 = '{0:08b}'.format(n2)
    n3 = ""
    for i in range(8):
        if((int(n1[i])+int(n2[i])) == 1):n3+="1"
        else:n3+="0"
    return n3


print(bitwise_and(7, 12))

print(bitwise_or(7, 12))

print(bitwise_xor(7, 12))