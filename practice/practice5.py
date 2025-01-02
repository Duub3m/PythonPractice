num3 = 0

def addition(num1: int, num2: int):
    global num3
    num3 = num1 + num2
    print(f"Answer: {num3}")

def subtraction(num1: int, num2: int):
    global num3
    num3 = num1 - num2
    print(f"Answer: {num3}")

def multiplication(num1: int, num2: int):
    global num3
    num3 = num1 * num2
    print(f"Answer: {num3}")

def division(num1: int, num2: int):
    global num3
    num3 = num1 / num2
    print(f"Answer: {num3}")






print("Wsg man what two numbers you wanna divide: ")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
division(num1, num2)

print("I gave you the answer now lets do it again: ")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
addition(num1, num2)
