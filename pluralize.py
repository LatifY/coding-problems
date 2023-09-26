def pluralize(lst):
    a={}
    for i in lst:
        if(lst.count(i)>1):a.append(i+"s")
        else:a.append(i)
    for j in range(len(a)):
        if(j!=0) and (a[j] in a[:j]):a[j]="za"
    return a

print(pluralize(["cow", "pig", "cow", "cow"])) #{"cows", "pig"}
print(pluralize(["table", "table", "table"])) #{"tables"}
print(pluralize(["chair", "pencil", "arm"])) #{"chair", "pencil", "arm"}