level = 0
def contains_list(lst):
    contains = False
    for i in lst:
        if(type(i) == list):
            contains = True
            break
    return contains

def get_lists(lst):
    lists = []
    for i in lst:
        if type(i) == list:
            lists.append(i)
    return lists

def get_numbers(lst):
    numbers = []
    for i in lst:
        if(type(i) == int):
            numbers.append(i)
    return numbers

def search_level(lst, curr_level = 0):
    global level
    if(level > 1):
        limit = level - 1
    elif(level == 1):
        return get_lists(lst)
    else: limit = level
    if(curr_level == limit):
        return lst
    else:
        next_level_list = []
        for i in lst:
            if(type(i) == list):
                for item in get_lists(i): next_level_list.append(item)
        return search_level(next_level_list, curr_level+1)
    
def count_number(lst, el):
    count = 0
    count_lst = []
    if(level > 0):
        for item in lst:
            for a in item:
                count_lst.append(a)
    else:
        count_lst = lst

    for i in count_lst:
        if(i == el):
            count += 1
    return count

def freq_count(lst, el):
    global level
    level = 0
    can_search = True
    values = []
    while can_search == True:
        value = search_level(lst)
        if(len(value) == 0):
            can_search = False
            break
        values.append([level, count_number(value, el)])
        level += 1
    return values