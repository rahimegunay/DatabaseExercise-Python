def findcentury(year):

    if year<=0:
        print("0 and negative value are not valid for a year")

    elif year<=100:
        print("1.century")

    elif (year %100==0):
        print(year//100, "century")
    else:
        print(year//100+1, "century")

year=2001
findcentury(1801)