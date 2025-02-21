operator=input("enter the operator")
num1=float(input("enter the first number"))
num2=float(input("enter the second number"))
while True:
    if operator=="+":
        print(f"{num1}+{num2}={num1+num2}")
        break
    elif operator=="-":
        print(f"{num1}-{num2}={num1-num2}")
        break
    elif operator=="*":
        print(f"{num1}*{num2}={num1*num2}")
        break
    elif operator=="/":
        print(f"{num1}/{num2}={num1/num2}")
        break
    else:
        print("invalid operator")
        break
    