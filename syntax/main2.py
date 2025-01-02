# Int
siblings = 4
# Float
age = 21.8
balance = 2350.56
# Boolean
rich = False
# String
name = "Dubem Eneh"

if (balance >= 1500):
    rich = True
elif (balance <1500):
    rich = False

# Converted the Float Balance into a String then printed it
balance_string = str(balance)
print("Balance is: " + balance_string)

# Converted the float age into an Int then printed it
age_int = int(round(age))
print(age_int)

# Converted the Int into a string then printed it
age_string = str(age_int)
print("Your age is " + age_string)

# Converted the boolean into a string
rich_string = str(rich)
print("Am I rich? " + "Answer: " + rich_string)

