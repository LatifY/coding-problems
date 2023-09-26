customers = {
  'Captain America': [10, 10, 54, 14, 51, 33, 42, 73, 66, 33, 55, 42, 47],
  'Iron Man': [30, 56, 38, 14, 17],
  'Hulk': [53, 25, 13, 7, 61, 16, 17, 29, 64, 8],
  'Superman': [27, 28]
}

def pizza_points(customers, min_orders, min_price):
    res = []
    for name in list(customers):
        can = False
        orders = customers[name]
        orders.sort(reverse=True)
        if(len(orders) >= min_orders):
            for order in range(min_orders):
                if(orders[order] >= min_price):
                    can = True
                else:
                    can = False
                    break
            if(can == True):
                res.append(name)
    return sorted(res)
    
print(pizza_points(customers,1,5))
'''
print(customers["Batman"])
print(list(customers)[0])
'''