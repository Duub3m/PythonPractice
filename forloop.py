import time

def countdown():
    for seconds in range(10,0,-2):
        print(seconds)
        time.sleep(1)


print("You have 10 seconds to answer the question: ")
answer = int(input("What is 2 + 2: "))
countdown()
if answer == 2:
    print("Congrats, you diffused the bomb")
    exit()
else:
    print("You failed to diffuse the bomb")



# for i in range(10):
#     print(i+1)


# for i in range(50,100+1,2):
#     print(i)

# for i in "Dubem Eneh":
#     print(i)

# name = input("whats ur name: ").lower().capitalize()

# print("Your name is: " + name)



# answer = True

# while answer == True:

#     for i in range(100,0-1,-1):
#         print("You have " + str(i) + " seconds left.")

#     if i == 0:
#         print("You've run out of time")
#         inputanswer = input("Would you like to restart? Yes or No: ").lower().capitalize()
            
#     if inputanswer == "No":
#         answer = False
#         print("Thank you for playing the game!")
#     elif inputanswer == "Yes":
#         answer == True
       



