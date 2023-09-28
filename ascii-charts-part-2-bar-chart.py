def bar_chart(results:dict):
	k =  list(results.keys())
	for x in range(len(k)):
		k[x] = str(int(results[k[x]] / 50) * "#") + str(k[x]) + "|*" + str(results[k[x]]) + "\n"
	k.sort()
	for t in range(len(k)):
		f = k[t].count("#")
		k[t] = k[t].replace("#", "")
		k[t] = k[t].replace("*", "#" * f + ("" if f == 0 else " "))
	l = ""
	for i in k:l+=i
	l = l[:-1]
	return l
		
print(bar_chart({'Q4': 0, 'Q3': 100, 'Q2': 0, 'Q1': 600}))
print(bar_chart({'Q4': 300, 'Q3': 150, 'Q2': 350, 'Q1': 250}))
print(bar_chart({'Q4': 350, 'Q3': 400, 'Q2': 400, 'Q1': 50}))
print(bar_chart({'Q4': 200, 'Q1': 500, 'Q2': 300, 'Q3': 300}))
print(bar_chart({'Q4': 300, 'Q3': 250, 'Q2': 600, 'Q1': 350}))
print(bar_chart({'Q4': 150, 'Q1': 550, 'Q2': 50, 'Q3': 600}))
print(bar_chart({'Q4': 450, 'Q3': 0, 'Q2': 50, 'Q1': 200}))
print(bar_chart({'Q4': 150, 'Q3': 0, 'Q2': 0, 'Q1': 450}))
print(bar_chart({'Q4': 0, 'Q1': 600, 'Q2': 250, 'Q3': 400}))
print(bar_chart({'Q4': 100, 'Q1': 150, 'Q2': 450, 'Q3': 0}))
print(bar_chart({'Q4': 150, 'Q1': 400, 'Q2': 100, 'Q3': 0}))
print(bar_chart({'Q4': 550, 'Q1': 600, 'Q2': 200, 'Q3': 50}))
print(bar_chart({'Q4': 250, 'Q3': 200, 'Q2': 500, 'Q1': 550}))
print(bar_chart({'Q4': 450, 'Q3': 50, 'Q2': 500, 'Q1': 0}))
print(bar_chart({'Q4': 250, 'Q3': 400, 'Q2': 150, 'Q1': 500}))
print(bar_chart({'Q4': 400, 'Q3': 600, 'Q2': 350, 'Q1': 600}))
print(bar_chart({'Q4': 50, 'Q1': 100, 'Q2': 150, 'Q3': 50})) 
print(bar_chart({'Q4': 50, 'Q1': 100, 'Q2': 100, 'Q3': 300}))
print(bar_chart({'Q4': 350, 'Q3': 50, 'Q2': 600, 'Q1': 300}))
print(bar_chart({'Q4': 100, 'Q1': 500, 'Q2': 50, 'Q3': 200}))