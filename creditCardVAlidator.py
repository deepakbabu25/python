sumOddDigit=0
sumEvenDigit=0
total=0

cardNo=input("Enter your card number: ")
cardNo=cardNo.replace("-","")  
cardNo=cardNo.replace(" ","")
cardNo=cardNo[::-1]
for i in range(0,len(cardNo),2):
    sumOddDigit+=int(cardNo[i])
for i in range(1,len(cardNo),2):
    temp=int(cardNo[i])*2
    if temp>9:
        sumEvenDigit+=(1+(temp%10))
    else:
        sumEvenDigit+=temp
total=sumOddDigit+sumEvenDigit
if total%10==0:
    print("Valid card number")
else:
    print("Invalid card number")


