# https://leetcode.com/problems/reverse-only-letters/

# reverse only english letters in string

class Solution:
    def isLetter(self, ch):
        code = ord(ch)
        r1 = range(ord('a'), ord('z') + 1)
        r2 = range(ord('A'), ord('Z') + 1)
        
        return code in r1 or code in r2

    def reverseOnlyLetters(self, s: str) -> str:
        arr = []
        for c in s:
            arr.append(c)
            
        start, end = 0, len(arr) - 1
        while start < end:
            if not self.isLetter(arr[start]):
                start += 1
            elif not self.isLetter(arr[end]):
                end -= 1
            else:
                arr[start], arr[end] = arr[end], arr[start]
                start, end = start + 1, end - 1
            
        return "".join(arr)
    
sol = Solution()
s = "ab-cd"
print(sol.reverseOnlyLetters(s))

s = "a-bC-dEf-ghIj"
print(sol.reverseOnlyLetters(s))

s = "Test1ng-Leet=code-Q!"
print(sol.reverseOnlyLetters(s))

s = "z<*zj"
print(sol.reverseOnlyLetters(s))