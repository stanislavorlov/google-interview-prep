# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        for c in s:
            arr.append(c)

        lastSpaceIndex, strLen = -1, len(s)
        for strIndex in range(strLen):
            if arr[strIndex] == ' ' or strIndex == strLen - 1:
                start = lastSpaceIndex + 1
                end = strIndex - 1 if arr[strIndex] == ' ' else strIndex
                while start < end:
                    arr[start], arr[end] = arr[end], arr[start]
                    start += 1
                    end -= 1
                lastSpaceIndex = strIndex
        return "".join(arr)

solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))

print(solution.reverseWords("Mr Ding"))