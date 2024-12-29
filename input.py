name = input("What is your name?: ")
age = int(input("What is your age?: "))
height = float(input("What is your height?: "))

if (age >= 21):
    canvote = True
elif (age < 21):
    canvote = False


print("Your name is " + name + " and you are " + str(age) + " years old.")
print("Your height is " + str(height))
print("Can you vote: " + str(canvote))

