def face_interval(num):
    try:
        num.sort()
        if(num[-1]-num[0] in num):return ":)"
        else:return ":("
    except:
        return ":/"


print(face_interval([1, 2, 5, 8, 3, 9]))
print(face_interval([5, 2, 8, 3, 11]))
print(face_interval([20, 50, 13, 60, 22, 72, 99]))
print(face_interval([11, 42, 83, 28, 47, 94]))
print(face_interval("bruh"))