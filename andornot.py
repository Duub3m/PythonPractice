
checking = float(input("How much is in your checking account: "))
savings = float(input("How much is in your savings account"))
balance = checking + savings
print("Your balance is: " + str(balance))
difference = abs(checking - savings)
if checking > savings:
    print("Your checking is " + str(difference) + " more than your savings account")
elif savings > checking:
    print("Your savings is " + str(difference) + " more than your checking account")

answer = input(("Do you think your rich? Yes or No: ")).lower()

if answer == "yes" and balance >=10000:
    print("Correct! you are rich")
elif answer == "yes" and balance <10000:
    print("Wrong! You are not rich")
elif answer == "no" and balance >=10000:
    print("Wrong! You are actually rich")
elif answer == "no" and balance <10000:
    print("Correct! You are not rich")
else:
    print("I asked you to type 'Yes' or 'No', please restart the program")

