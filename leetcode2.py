from typing import List

class Solution:
    def twoSum(self, nums, target):
        prevMap = {}  # Map to store numbers and their indices

        for index, number in enumerate(nums):
            difference = target - number
            if difference in prevMap:
                return [prevMap[difference], index]
            prevMap[number] = index
        
        return []  # Return an empty list if no solution is found

# Example usage
nums = [2, 4, 6, 3]
target = 7

solution = Solution()  # Create an instance of Solution
result = solution.twoSum(nums, target)  # Call the method
print(result)  # Print the result
