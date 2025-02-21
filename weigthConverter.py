weight=float(input("enter the weight"))
unit=input("enter the unit?(k or l)").upper()
if unit=="K":
    weight=weight*2.205
    unit='lbs'
    print(f"weight is {weight} {unit}")
elif unit=="L":
    weight=weight/2.205
    unit='kg'
    print(f"weight is {weight} {unit}")
else:
    print("invalid unit")
