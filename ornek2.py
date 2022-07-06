def quarter_of(month):
    if month%3==0:
        print(month//3,"quarter")
    elif month==1 and month==2 and month==3:
        print("1st quarter")
    else:
        print(month//3+1, "quarter")
quarter_of(8)

