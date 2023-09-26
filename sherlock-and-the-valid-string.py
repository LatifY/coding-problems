import collections
def is_valid(txt):
    c = collections.Counter()
    txt = sorted(txt)
    c.update(txt)
    nums=[]
    a = []
    ones=0
    twos=0
    threes=0
    fours=0
    for i in c:
        if c[i] == 1:ones+=1
        if c[i] == 2:twos+=1
        if c[i] == 3:threes+=1
        if c[i] == 4:fours+=1
        num = c[i]
        if num not in nums:nums.append(num)
    a.append(ones)
    a.append(twos)
    a.append(threes)
    a.append(fours)
    nums = sorted(nums,reverse=True)
    if len(nums)>2:return "NO"
    elif len(nums) == 1:return "YES"
    else:
        if(nums[0]-nums[1]>1):return "NO"
        elif(a[nums[0]-1]>1):return "NO"
        else:return "YES"

#alternative
def is_valid2(txt):
	return "YES" if len(txt)%len(set(txt))==0 or (len(txt)-1)%len(set(txt))==0 else "NO"

print(is_valid("aabbccddeefghi"))
print(is_valid("aabbcd"))
print(is_valid("abcdefghhgfedecba"))
print(is_valid("abc"))
print(is_valid("abcc"))
print(is_valid("abccc"))