
list = [1, 2, 5, 2, 3]
new_list = []
choice = ""

print(list)


def order_list():
    global list 
    list.sort()
    print(f"Ordered List: {list}")

def update_list(num):
    global list
    if type(num) == int:
        list.append(num)
        print(f"Succesfully added {num} to the list!")
        print(f"New list: {list}")
    else:
        print("Could not add this item to list as its not a number")

def end_program():
    exit()

def update_list(num):
    global new_list
    

def get_indices(num):
    global list
    global new_list
    for index, number in enumerate(list):
        if target == number:
            new_list.append(index)      

def check_list(target):
    global list
    global new_list
    if target in list:
        get_indices(target)
    else:
        print("We couldn't find this number")

        

target = int(input("What number would you like to check for: "))
check_list(target)
print(f"We found the numbers at these indices: {new_list}")


while True:
    choice = input("Do you want to add a number, Yes or No: ").strip().capitalize()
    if choice == "Yes":
        num_input = int(input("What number do you want to add to the list: "))
        update_list(num_input)
        order_list()
    elif choice == "No":
        print("Thank you for playing! Goodbye")
        end_program()
    else:
        print("That is not one of the choices, pls try again")

