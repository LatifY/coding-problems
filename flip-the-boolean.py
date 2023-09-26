def reverse(arg):
    if(type(arg) == bool):
        if(arg == True):return False
        else:return True
    else:return "boolean expected"

print(reverse(False))