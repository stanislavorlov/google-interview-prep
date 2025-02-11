# https://neetcode.io/problems/is-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while end > start and not s[end].isalnum():
                end -= 1
            if not s[start].lower() == s[end].lower():
                return False
            start += 1
            end -= 1

        return True

solution = Solution()
print(solution.isPalindrome("Was it a car or a cat I saw?"))    # true

print(solution.isPalindrome("tab a cat"))    # false

print(solution.isPalindrome("0P"))    # false