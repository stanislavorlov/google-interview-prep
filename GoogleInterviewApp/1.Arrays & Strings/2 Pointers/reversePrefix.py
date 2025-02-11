# https://leetcode.com/problems/reverse-prefix-of-word/

# Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
# If the character ch does not exist in word, do nothing.

# Input: word = "abcdefd", ch = "d"
# Output: "dcbaefd"

# Input: word = "xyxzxe", ch = "z"
# Output: "zxyxxe"

# Input: word = "abcd", ch = "z"
# Output: "abcd"

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = []
        idx = -1
        
        for i, letter in enumerate(word):
            arr.append(letter)
            if letter == ch and idx == -1:
                idx = i

        if idx:
            left, right = 0, idx
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left, right = left + 1, right - 1
            
            return "".join(arr)
        
        return word
        
solution = Solution()
print(solution.reversePrefix("abcdefd", "d"))       # "dcbaefd"

print(solution.reversePrefix("xyxzxe", "z"))        # "zxyxxe"

print(solution.reversePrefix("abcd", "z"))