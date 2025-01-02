# List () = changeable, most flexible

# Append - adds the element to the end of the list
# Insert - adds the element to the beginning of the list
# Remove - removes the element from the list
# Pop - remove an element at a given index
# Clear - removes all the elements from the list

# Tuple () = non-changeable, faster

# Set {} = mutchangeable (only add/remove), unordered,
# NO duplicates, best for membership testing



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

check = input("Search for a fruit")

if check in fruits:
    index = fruits.index(check)
    print(f"We found {check} in the list at index {index}")




while status == True:

    add_fruit = input("What fruit you wanna add: ").strip().capitalize()
    add_fruit_list(add_fruit)

    inputStatus = input("Do you wanna end the program: ").strip().capitalize()
    program_status(inputStatus)

    remove_fruit = input("What fruit you wanna remove: ").strip().capitalize()
    remove_fruit_list(remove_fruit)

    inputStatus = input("Do you wanna end the program: ").strip().capitalize()
    program_status(inputStatus)


    

