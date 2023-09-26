def alphabet_soup(txt):
    new_txt = ""
    txt=sorted(txt)
    for i in txt:
        new_txt+=i
    return new_txt
print(alphabet_soup("hello"))