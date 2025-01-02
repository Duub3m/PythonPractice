list = [1,2,5,2,3]
list.sort()

new_list = []

target = int(input("What number would you like to find: "))

for index, number in enumerate(list):
    if target == number:
        new_list.append(index)

print(new_list)

for index, numer in enumerate(list):
    if target == number:
        new_list.append(index)
        
backwards_list = list[::-1]
print(backwards_list)


    