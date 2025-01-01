nums = [1,2,5,2,3]
new_nums = []
target = 2

for index, number in enumerate(nums):
    if number == target:
        new_nums.append(index)

print(new_nums)