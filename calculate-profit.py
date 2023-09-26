profit = lambda a: int(round(a['inventory']*a['sell_price']-a['inventory']*a['cost_price']))
	
print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))