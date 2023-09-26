import string
alp = list(string.ascii_lowercase)
def atbash(txt):
    new_txt = ""
    for let in txt:
        if(let.lower() in alp):
            if(let == let.lower()):
                new_txt+=alp[25-(alp.index(let))]
            else:
                new_txt+=(alp[25-(alp.index(let.lower()))]).upper()
        else:
            new_txt+=let
    return new_txt
print(atbash("Hello world!"))