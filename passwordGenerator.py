import random
letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n',
        'o','p','q','r','s','t','u','v','w','x','y','z']
numbers=[0,1,2,3,4,5,6,7,8,9]
symbols=['!','@','#','$','%','^','&','*']
print("welcome to the password generator")
n_letters=int(input("enetr the no of letter u wannt in ur password"))
n_numbers=int(input("no of number u want in ur password"))
n_symbols=int(input("no of symbols u want in ur password"))
passwordl=[]
password=''
for i in range(1,n_letters+1):
    passwordl.append(random.choice(letter))
for i in range(1,n_numbers+1):
    passwordl.append(random.choice(numbers))
for i in range(1,n_symbols+1):
    passwordl.append(random.choice(symbols))
random.shuffle(passwordl)
for i in passwordl:
    password+=str(i)

print(password)
