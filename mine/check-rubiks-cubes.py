def identify(*cube):
    l=len(cube)
    c=0
    for i in cube:
        a=len(max(cube))
        j=len(i)
        if j != a:c+=a-j
    if(c>0):return "Missing "+str(c)
    if(len(cube[0])==l):return "Full"
    else:return "Non-Full"


print(
identify(
["O","O"],
["O","O"],
["O","O","O"])) #"Missing 2"

print(
identify(
["O","O"],
["O","O","O"])) #"Missing 1"

print(
identify(
["O","O","O"],
["O","O","O"],
["O","O","O"])) #"Full"

print(
identify(
["O","O","O","O"],
["O","O","O","O"],
["O","O","O","O"],
["O","O","O","O"]))#"Full"

print(
identify(
["O","O","O","O"],
["O","O","O","O"],
["O","O","O"],
["O","O","O","O"]))#"Missing 1"

print(
identify(
["O","O","O","O"],
["O","O","O","O"]))#"Non-Full"

print(
identify(
["O","O"],
["O","O"]))#"Full"

print(
identify(
["O","O"],
["O"]))#"Missing 1"








