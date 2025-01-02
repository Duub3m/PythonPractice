# Initialize a String
first_name = "Dubem"
last_name = "Eneh"
full_name = first_name + " " + last_name

# Initialize a Number
age = 14

# Convert from Number to String
age_string = str(age)

# Print the converted Number and String

print("Your name is " + full_name + " and your age is " + age_string) 
if (age >= 18):
   print("You are old enough to vote. Congrats!")
elif (age < 18):
    print("You are not old enough to vote")

# Int
age = "12"
print(type(age))
age = 12
print(type(age))
age = 12.5
print(type(age))
human = False
print(type(human))
#  

if (age >=12):
    print("You're to old for the kids menu")
elif (age <12):
    print("You're of age to get the kids menu items")

name1, age1, attractive1 = "Dubem", 21 , True

name2, age2, attractive2 = "John", 25, False

full_name_1 = name1 +str(age1) + str(attractive1)

print(full_name_1)

def process_day(day):
    match day.upper():
        case "MONDAY":
            return "Today is monday"
        case _:
            return "This is not a day"

print(process_day("MOnday"))

name = "dubem eneh"

# Prints the Length of the String
print(len(name))

# Finds the index of the specified letter(if its repeated it returns the first instance)
print(name.find("d"))

# Capitalizes the first letter in the String 
print(name.capitalize())

# Makes the String LowerCase
print(name.lower())

# Makes the String UpperCase
print(name.upper())

# Checks if String is a Digit
print(name.isdigit())

# Checks if String containts alphabetical letters
print(name.isalpha())

# Prints the Count of a specifc letter in a String
print(name.count("e"))

# Replaces the specificed letter in a String
print(name.replace("d","p"))

# Prints a String 3 times
print(name*3)
