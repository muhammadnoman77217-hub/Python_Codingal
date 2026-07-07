bill= float(input("enter the units you consumed"))
if bill<=50:
    print("your per-unit cost is 2.60 and bill is 25")
else:
    if bill>=50<=100:
        print("your per-unit cost is 3.25 and bill is 35")
    else:
        if bill>=100<=200:
            print("your per-unit cost is 5.26 and bill is 45")
        else:
            if bill>=200:
                print("your per-unit cost is 8.45 and bill id 85")