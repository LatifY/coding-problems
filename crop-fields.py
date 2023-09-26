def crop_hydrated(field):
    f_col = []
    f_l = len(field)
    for i in range(f_l):
        sub_f = field[i]#field icindeki alt listeler
        sub_f_l = len(sub_f)
        for x in range(sub_f_l):
            ar = []
            subsub_f = sub_f[x]#field icindeki listedeki secilen karakter
            if(subsub_f == "c"):
                if(sub_f_l>1):
                    #linelinelinelinelinelineline
                    if(x == 0):#eger field icindeki ilk karakterse
                        ar.append(sub_f[x+1])
                    elif(x == sub_f_l-1):#eger field icindeki son karakterse
                        ar.append(sub_f[x-1])
                    else:
                        ar.append(sub_f[x-1])
                        ar.append(sub_f[x+1])
                    #columncolumncolumncolumncolumn
                    if(f_l>1):
                        if(i == 0):#eger field icindeki ilk listeyse
                            if(x == 0):#eger field icindeki ilk listedeki ilk karakterse
                                ar.append(field[i+1][x])
                                ar.append(field[i+1][x+1])
                            elif(x == sub_f_l-1):#eger field icindeki ilk listedeki son karakterse
                                ar.append(field[i+1][x])
                                ar.append(field[i+1][x-1])
                            else:#eger field icindeki ilk listedeki orta karakterlerse (lenght sadece >2 ise olabilir)
                                ar.append(field[i+1][x])
                                ar.append(field[i+1][x+1])
                                ar.append(field[i+1][x-1])
                        elif(i == f_l-1):#eger field icindeki son listeyse
                            if(x == 0):#eger field icindeki son listedeki ilk karakterse
                                ar.append(field[i-1][x])
                                ar.append(field[i-1][x+1])
                            elif(x == sub_f_l-1):#eger field icindeki son listedeki son karakterse
                                ar.append(field[i-1][x])
                                ar.append(field[i-1][x-1])
                            else:#eger field icindeki son listedeki orta karakterlerse
                                ar.append(field[i-1][x])
                                ar.append(field[i-1][x+1])
                                ar.append(field[i-1][x-1])
                        else:#eger field icindeki orta listeyse
                            if(x == 0):#eger field icindeki orta listedeki ilk karakterse
                                ar.append(field[i-1][x])
                                ar.append(field[i-1][x+1])
                                ar.append(field[i+1][x])
                                ar.append(field[i+1][x+1])                               
                            elif(x == sub_f_l-1):#eger field icindeki orta listedeki son karakterse
                                ar.append(field[i-1][x])
                                ar.append(field[i-1][x-1])
                                ar.append(field[i+1][x])
                                ar.append(field[i+1][x-1]) 
                            else:#eger field icindeki orta listedeki orta karakterlerse
                                ar.append(field[i-1][x])
                                ar.append(field[i-1][x+1])
                                ar.append(field[i-1][x-1])
                                ar.append(field[i+1][x])
                                ar.append(field[i+1][x+1])
                                ar.append(field[i+1][x-1])
                else:
                    if(i == 0):
                        ar.append(field[i+1][0])
                    elif(i == f_l-1):
                        ar.append(field[i-1][0])
                    else:
                        ar.append(field[i-1][0])
                        ar.append(field[i+1][0])
       
                if('w' not in ar):return False
    return True


#alternative
def crop_hydrated2(field):
  n,m = len(field), len(field[0])
  pos = {}
  for t in ['w','c']:
    pos[t] = {(i,j) for i in range(n) for j in range(m) if field[i][j] == t}
  dirs = {(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)}
  
  return all(any((a+i,b+j) in pos['w'] for (i,j) in dirs) for (a,b) in pos['c'])

print(crop_hydrated([
  [ "c", "c", "c", "c" ],
  [ "w", "c", "c", "c" ],
  [ "c", "c", "c", "c" ],
  [ "c", "w", "c", "c" ]
]))

print(crop_hydrated([
  [ "w", "c" ],
  [ "w", "c" ],
  [ "c", "c" ]
]))

print(crop_hydrated([
  [ "c", "c", "c" ]
]))

