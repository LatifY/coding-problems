def tetra(n):
    c = 0
    for a in range(1,n+1):
        c += (a*(a+1))/2
    return int(c)

#optional alternative
def tetra2(n):
	return (n * (n + 1) * (n + 2)) / 6

for i in range(1, 21):
    print(tetra(i))