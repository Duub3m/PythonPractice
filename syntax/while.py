number = int(input("Type the number 12: "))
answered = False

if number == 12:
    answered = True
    print("Thanks for typing the number " + str(number) + ". Enjoy your day bro")
elif not number == 12:
    while answered == False:
        print("you didnt answer the question correctly, now you're stuck in a loop") 

name = ""

while len(name) == 0:
    name = (input("What is your name: "))
    print("you didnt type anything, please type in your name")
else:
    print("Your name is " + name)


name = None

while not name:
    name = (input("What is your name: "))
    print("Your name is: " + name)