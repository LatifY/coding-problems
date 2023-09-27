def split(number,sum = 0, product = 1):
	if(number == 1):return 1
	if(sum == number):return product
	add = 0
	diff = number - sum
	if(diff == 2 or diff == 4):add = diff
	else: add = 3
	return split(number, sum+add, product *add)

print(split(5))
print(split(5))
print(split(48))
