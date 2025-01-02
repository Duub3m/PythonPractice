nums = [1,2,5,2,3]

target = int(input("what number are you looking for: "))

# Sort the list first
nums.sort()

# Find all indices of the target
indices = [] #create an empty list to store our indices

#for loop called index that checks if the number is in the nums list
for index, number in enumerate(nums): 
    if number == target:
        indices.append(index)

# Output the results
if indices:
    print(f"The target {target} is found at indices: {indices}")
else:
    print(f"The target {target} is not in the list.")
