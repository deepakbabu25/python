import time

my_time=int(input("Enter the time in seconds: "))

for x in range(0,my_time):
    seconds=x%60
    minutes=(x//60)%60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)#sleep for 3 sec
print("Time's up!")