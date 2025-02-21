foods=[]
prices=[]
total=0
while True:
    food=input("Enter the food item to buy(q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)
        total+=price
print("-----------------your cart-------------------")
for food in foods:
    print(food, end=",")
print(f"\nTotal amount is {total}")
print("Thank you for shopping with us")