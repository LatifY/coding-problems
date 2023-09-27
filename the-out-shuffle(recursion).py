def shuffle(lst,deck, count = 0):
    mid = int(len(lst) / 2)
    left = lst[0: mid]
    right = lst[mid: ]

    new = []
    for i in range(mid):
        new.append(left[i])
        new.append(right[i])

    if(new == deck):
        return count + 1

    return shuffle(new,deck,  count +1)

def shuffle_count(num):
    deck = []
    for i in range(num):deck.append(i + 1)
    count = shuffle(deck, deck)
    return count

print(shuffle_count(2))
print(shuffle_count(14))
print(shuffle_count(52))