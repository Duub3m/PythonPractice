
import random
	
greeting = input("Hi, what's your name? ")
print(f"Hello, {greeting}")

health = 100

def health_change(hp: int):
    global health
    health = health + hp
    return health


def status():
    if health > 0:
        print("success")
    else:
        print("You fainted")
        exit()

while True:
    path = input("Pick a path (right or left) > ").strip().capitalize()
    if path == "Right":
        print("You have encountered a bear!")
        choice = input("Do you want to fight or flee? ").strip().capitalize()   
        if choice == "Fight":
            current_health = health_change(random.randint(0,50))
            print(f"You took {current_health} damage")
        elif choice == "Flee":
            health_change(10)

    elif path == "Left":
        print("You have encountered a river!")
        choice = input("Do you want to drink? ").strip().capitalize()
        if choice == "Yes":
            health_change(10)   
    status()
