def show_balance(balance):
    print("Your balance is: ",balance)
def deposit(amount):

    print("Amount deposited: ",amount)
    return amount
    
def withdraw(amount,balance):
    if balance<amount:
        print("Insufficient balance")
    else:
        print("Amount withdrawn: ",amount)
    return amount
    
def main():
    balance=0
    is_running=True
    while is_running:
        print("---------------------------------")
        print("Welcome to the bank")
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")
        print("---------------------------------")
        choice=int(input("Enter your choice: "))
        if choice==1:
            show_balance(balance)
        elif choice==2:
            amount=int(input("Enter the amount you want to deposit: "))
            balance+=deposit(amount)
            #print(balance)
        elif choice==3:
            amount=int(input("Enter the amount you want to withdraw: "))
            balance-=withdraw(amount,balance)
            
        elif choice==4:
            is_running=False
        else:
            print("Invalid choice")
    print("Thank you for using our service")

if __name__ == "__main__":
    main()


