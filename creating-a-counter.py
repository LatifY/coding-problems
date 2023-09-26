def counter():
	if'c'not in counter.__dict__:counter.c=-1
	counter.c+=1
	return counter.c

a="print('asdasd')"
exec(a)

print(counter())
print(counter())
print(counter())