def convert_to_decimal(perc):
    percs = []
    for a in perc:
        percs.append(float(a[:-1])/100)
    return(percs)


#alternative
def convert_to_decimal2(perc):
	return [float(item.strip("%")) * .01 for item in perc]