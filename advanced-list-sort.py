def ctrl(lst,e,adv_lst):
    for i in adv_lst:
        if e in i:
            i.append(e)
            return True
    return False

def advanced_sort(lst):
    adv_lst = []
    for e in lst:
        a = ctrl(lst,e,adv_lst)
        if(a == False):adv_lst.append([e])
    return adv_lst

#alternative
def advanced_sort2(lst):
	unique, l =  [], []
	for e in lst:
		if e not in unique:
			l.append([e] * lst.count(e))
			unique.append(e)
	return l

print(advanced_sort([2,1,2,1]))