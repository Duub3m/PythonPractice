# List (] = mutable, most flexible
# Tuple () = immutable, faster
# = mutable (add/remove), unordered,
# NO duplicates, best for membership testing

# Append - adds to the end of the list
# Insert - adds to the beginning of the list
# Remove - removes an item from the list

fruits = ["Orange", "Banana", "Coconut"]

status = True

def add_fruit_list(add_fruit):
    global fruits 
    fruits.insert(0, add_fruit)
    for fruit in fruits:
        print(fruit, end = ", ")

def remove_fruit_list(remove_fruit):
    global fruits 
    if remove_fruit in fruits:
        fruits.remove(remove_fruit)
    for fruit in fruits:
        print(fruit, end = ", ")

def program_status(input_program_status):
    global status 
    if input_program_status == "Yes":
        status == False
        exit()
    elif input_program_status == "No":
        status == True

print(fruits)




while status == True:

    add_fruit = input("What fruit you wanna add: ").strip().capitalize()
    add_fruit_list(add_fruit)

    inputStatus = input("Do you wanna end the program: ").strip().capitalize()
    program_status(inputStatus)

    remove_fruit = input("What fruit you wanna remove: ").strip().capitalize()
    remove_fruit_list(remove_fruit)

    inputStatus = input("Do you wanna end the program: ").strip().capitalize()
    program_status(inputStatus)


    

