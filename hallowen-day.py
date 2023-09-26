from datetime import datetime
def halloween(dt):
    y = []
    new_dt = datetime.strptime(dt, "%Y/%m/%d")
    if new_dt.strftime("%m") =="10"  and new_dt.strftime("%d") == "31":return "Bonfire toffee" 
    else:return "toffee"

print(halloween("2013/10/31"))