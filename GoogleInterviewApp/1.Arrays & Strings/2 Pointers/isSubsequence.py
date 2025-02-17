# https://leetcode.com/problems/is-subsequence/

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a sequence of characters that can be obtained by deleting some (or none) of the characters from the original string, 
# while maintaining the relative order of the remaining characters.

def isSubsequence(s: str, t: str) -> bool:
    i = j = 0
    leftL, rightL = len(s), len(t)
    while i < leftL and j < rightL:
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == leftL

print(isSubsequence("ace", "abcde"))
print(isSubsequence("aec", "abcde"))