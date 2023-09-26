char_at_pos=lambda x,r: type(x)(type(x[0])(x[i]) for i in range(len(x)) if i%2==1) if r=="even" else type(x)(type(x[0])(x[i]) for i in range(len(x)) if i%2==0)

print(char_at_pos([2, 4, 6, 8, 10], "even"))
print(char_at_pos("EDABIT", "odd"))
print(char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd"))