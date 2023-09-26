def first_before_second(txt, f, s):
    txt = txt.replace(" ","")
    fb = False
    sb = False
    for x in txt:
        if(x == f and sb == False):fb = True
        elif(x == f and sb == True):return False

        if(x == s and fb == True):sb = True
        elif(x == s and fb == False):return False
    if(fb and sb):return True
    else:return False

#alternative
def first_before_second2(s, first, second):
	return s.rindex(first) < s.index(second) #rindex finds the last occurrence of the str parameter in s.(txt)

print(first_before_second("knaves knew about waterfalls", "k", "w"))
	