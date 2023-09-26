def tallest_skyscraper(lst):
    ss = []
    for i in range(len(lst[0])):
        subss = []
        for a in lst:
            subss.append(a[i]) 
        ss.append(subss)
    for x in range(len(ss)):
        ss[x] = list(filter((0).__ne__, ss[x]))
    m = max(len(a) for a in ss)
    return m

#alternative
def tallest_skyscraper2(lst):
	return sum(1 for i in lst if sum(i)>0)

#alternative2
def tallest_skyscraper3(A):
	return sum(1 in R for R in A)

print(tallest_skyscraper([
  [0, 0, 0, 0],
  [0, 1, 0, 0],
  [0, 1, 1, 0],
  [1, 1, 1, 1]
]))