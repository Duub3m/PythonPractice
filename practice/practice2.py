
import random

running = False

input1 = input("Wsg man, lets get this quiz done, you ready? Yes or No?: ").strip().capitalize()

if input1 == "Yes":
    running = True
    while running == True:
        number1 = (random.randint(1,10))
        number2 = (random.randint(1,10))
        print("What do you get when you do the equation" + str(number1) + " + " + str(number2))
        input2 = input("Answer: ")
        number3 = number1 + number2
        if input2 == str(number3):
            print("You got it right")
            input1 = input("would you like to try again Yes or No?: ").lower().capitalize()
        else:
            print(f"wrong buddy, the answer was {number3}")
            input1 = input("would you like to try again Yes or No?: ").lower().capitalize()

elif input1 == "No":
    print("Okay whatever man, suite yourself")


            

    
