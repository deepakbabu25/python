unit=input("temperature is in celesius or fahrenheit?(c/f)").upper()
temp=float(input("enter the temperature"))  
if unit=="C":
    temp=(temp*9/5)+32
    unit='F'
    print(f"temperature is {temp} {unit}")
elif unit=="F":
    temp=(temp-32)*5/9
    unit='C'
    print(f"temperature is {temp} {unit}")
else: 
    print("invalid unit")