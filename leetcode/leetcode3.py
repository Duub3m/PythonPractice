class Solution(object):
    def maxScore(self, s):
        max_score = 0
        
        # Iterate through all possible split points
        for i in range(1, len(s)):
            left = s[:i]
            right = s[i:]
            
            # Calculate the score: number of zeros in left + number of ones in right
            score = left.count('0') + right.count('1')
            max_score = max(max_score, score)
        
        return max_score
        


s = "00111"



solution = Solution()
result = solution.maxScore(s)
print(result)

        