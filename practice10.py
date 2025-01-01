list = []

def menu(option):
    global list
    match option:
        case "O":
            print("you chose the order your list")
        case "B": 
            print("You chose the make your list backwards")
        case "T":
            print("You chose to multiply your list times two")
        case "I":
            print("You chose to get the indicies of the list")

option = input("What would you like to do with the list")

