# https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/705/hashing/4601/

# Check if the Sentence Is Pangram
# A pangram is a sentence where every letter of the English alphabet appears at least once.

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
    
solution = Solution()
print(solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))

print(solution.checkIfPangram("leetcode"))