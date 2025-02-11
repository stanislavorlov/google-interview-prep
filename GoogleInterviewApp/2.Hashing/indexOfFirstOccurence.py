# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenH = len(haystack)
        lenN = len(needle)
        if lenH < lenN:
            return -1
        
        for i in range(0, lenH - lenN):
            j = 0
            while j < lenN and haystack[i+j] == needle[j]:
                j += 1
            if j == lenN:
                return i

        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        lenH = len(haystack)
        lenN = len(needle)
        if lenN > lenH:
            return -1

        for i in range(0, lenH):
            hIdx = i
            nIdx = 0
            while haystack[hIdx] == needle[nIdx] and hIdx < lenH -1 and nIdx < lenN - 1:
                hIdx += 1
                nIdx += 1

            if not (hIdx < lenH and nIdx < lenN and haystack[hIdx] != needle[nIdx]):
                return i
        
        return -1
            

            
                
            

solution = Solution()
print(solution.strStr("sadbutsad", "sad"))
print(solution.strStr("leetcode", "leeto"))
print(solution.strStr("aaabcde", "bcde"))
print(solution.strStr("aaa", "aaaa"))