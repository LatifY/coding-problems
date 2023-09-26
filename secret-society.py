def society_name(friends):
    friends.sort()
    fl = ""
    for ppl in friends:
        fl+= ppl[0]
    return fl.upper()

print(society_name(["Adam", "Sarah", "Malcolm"]))