def uncensor(txt, vowels):
    chars=[]
    for i in vowels:
        chars.append(i)
    ind = 0
    new_txt = ""
    for m in txt:
        if(m=="*"):
            new_txt+=chars[ind]
            ind+=1
        else:new_txt+=m
    return new_txt

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))