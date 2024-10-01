# https://leetcode.com/problems/reverse-string/

def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    start, end = 0, len(s)-1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start, end = start + 1, end - 1
        
s = ["h","e","l","l","o"]
reverseString(s)
print(s)

s = ["H","a","n","n","a","h"]
reverseString(s)
print(s)