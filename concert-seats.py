def can_see_stage(seats):
  lst = []
  for i in range(len(seats[0])):
    sublst = []
    for a in seats:
      sublst.append(a[i]) 
    lst.append(sublst)
  for x in lst:
    for y in range(1,len(x)):
      if(x[y] <= x[y-1]):
        return False 
  return True

print(can_see_stage(
[[1, 2, 2], 
[2, 3, 3], 
[4, 4, 4]]))
