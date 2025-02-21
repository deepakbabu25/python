from database import questions,options
print("Welcome to my quiz game")
print("*********************************************")

score=0
yesorno=input("Do you want to play the quiz game?").upper()
def checkanswer(guess,answer):
    if guess==answer:
        return True
    else:
        return False
    
if yesorno=="YES":
    print("great lets start the game")
    for i in range(len(questions)):
        print(questions[i]["text"])
        for j in range(len(options[i])):
            print(options[i][j])
        guess=input("Enter your guessA/B/C/D:").upper()
        is_correct=checkanswer(guess,questions[i]["answer"])
        if is_correct:
            print("Your answer is correct")
            score+=1

        else:
            print("Your answer is wrong")
            print(f"the correct answer is{questions[i]['answer']}")
        print(f"your current score is{score}/{i+1}")
        print("*********************************************")
    print(f"Your score is {score}")
    print(f"your score is{(score/len(questions))*100}%")


