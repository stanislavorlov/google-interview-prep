# https://leetcode.com/problems/maximum-number-of-balloons/editorial/

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# Input: text = "nlaebolko"
# Output: 1

# Input: text = "loonbalxballpoon"
# Output: 2

# Input: text = "leetcode"
# Output: 0

from typing import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        
        return min(counter['b'], counter['a'], counter['l'] // 2, counter['o'] // 2, counter['n'])
    
solution = Solution()
print(solution.maxNumberOfBalloons('nlaebolko'))

print(solution.maxNumberOfBalloons('loonbalxballpoon'))

print(solution.maxNumberOfBalloons('leetcode'))