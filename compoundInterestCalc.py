principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("Enter the principle amount: "))
    if principle<=0:
        print("Invalid amount")
while rate<=0:
    rate=float(input("Enter the rate of interest: "))
    if rate<=0:
        print("Invalid rate")
while time<=0: 
    time=float(input("Enter the time period: "))
    if time<=0:
        print("Invalid time period")
total=principle*(1+rate/100)**time
print(f"Total amount is {total}")
print(f"Interest is {total-principle}")