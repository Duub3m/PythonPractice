# List (] = mutable, most flexible
# Tuple () = immutable, faster
# = mutable (add/remove), unordered,
# NO duplicates, best for membership testing

# Append - adds to the end of the list
# Insert - adds to the beginning of the list
# Remove - removes an item from the list
fruits = ["orange", "banana", "coconut"]

def update_fruit_list(add_fruit):
    global fruits 
    fruits.insert(0, add_fruit)

add_fruit = input("What fruit you wanna add: ")
update_fruit_list(add_fruit)

for fruit in fruits:
    print(fruit, end = ", ")
