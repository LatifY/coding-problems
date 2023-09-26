def bonus(d):
    if d<=32:
        return 0
    elif d>32 and d<=40:
        return (d-32)*325
    elif d>40 and d<=48:
        return 8*325 + (d-40)*550
    elif d>48:
        return 8*325 + 8*550 + (d-48)*600
    
#alternative
def bonus2(days):
	return 325*max(0,days-32) + 225*max(0,days-40) + 50*max(0,days-48)

#alternative2
def bonus3(days):
	return sum(([0]*33+[325]*8+[550]*8+[600]*2)[:days+1])

print(bonus(15))
print(bonus(37))
print(bonus(50))
