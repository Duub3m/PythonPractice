import random



inventory = [1,2,3,4,5,6,7,8,9,10] 

print(inventory[10:0:-1])

age = input("Whats your age").strip()
print(age)

name = input("Hey lil bro, what's your name: ")
print("You're on a road trip in the middle of nowhere, and your car has suddenly broken down. You must decide how to handle the situation.")

energy = 100

money = 50

def current_energy(energy_change: int, amount: int):
    global energy 
    energy += energy_change * amount

def current_money(money_change: float, amount: int):
    global money 
    money -= money_change * amount

# def inventory_change(str: item):
#      global inventory
#      inventory += item

print(f"You have {money} USD")

print(f"You have {energy} energy")

def process_beverage_choice(beverage_choice):

    match beverage_choice:
        case "Water":
            price = 30
            amount=int(input(f"How much Water you want its {price}"))
            current_money(price, amount)
            current_energy(40,amount)
        case "Juice":
            price = 40
            amount=int(input(f"How much Juice you want its {price}"))
            current_money(price, amount)
            current_energy(20,amount)
        case "Mystery":
            price = 10
            amount=int(input(f"How much Mystery you want its {price}"))
            current_money(price, amount)
            current_energy(random.randint(-50,50), amount)
        case _:
            print("This is not a valid choice")

def process_item_choice(choice):
    match choice:
        case "Wrench":
            price = 30
            amount=int(input(f"How much Water you want its {price}"))
            current_money(price, amount)
            current_energy(40,amount)
        case "Juice":
            price = 40
            amount=int(input(f"How much Juice you want its {price}"))
            current_money(price, amount)
            current_energy(20,amount)
        case _:
            print("This is not a valid choice")


beverage_choice = input("What beverage you want, we got Water, Juice, and Mystery: ").strip().capitalize()
process_beverage_choice(beverage_choice)

item_choice = input("What item do you want, we got Wrench, and Crowbar ").strip().capitalize()
process_item_choice(item_choice)

print(f"You have {energy} energy and {money} USD left")


