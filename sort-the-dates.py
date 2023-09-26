from datetime import datetime
def sorting(L):
    splitup = L.split('-')
    return splitup[1], splitup[0]

def asc(lst):
    '''
    y = []
    m = []
    d = []
    h = []
    m = []
    for date in lst:
        print(date)
        date_object = datetime.strptime(date, "%d-%m-%Y_%H:%M")
        y.append(date_object.strftime("%Y"))
    '''


    sorted(d, key=sorting)

def dsc(lst):
    print("dsc")

def sort_dates(lst, mode):
    if(mode == "ASC"):return asc(lst)
    if(mode == "DSC"):return dsc(lst)


print(asc(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"]))