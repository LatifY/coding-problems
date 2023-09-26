def operation(a, b, o):
    a=int(a)
    b=int(b)
    if(o=="add"):return str(a+b)
    if(o=="subtract"):return str(a-b)
    if(o=="multiply"):return str(a*b)
    if(o == "divide" and b != 0):return str(round(a/b))
    else:return "undefined"

print(operation("6", "3", "divide"))
