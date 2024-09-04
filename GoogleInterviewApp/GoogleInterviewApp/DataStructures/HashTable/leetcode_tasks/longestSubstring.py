# Given a string s, find the length of the longest substring without repeating characters.

#Input: s = "abcabcbb"
#Output: 3

#Input: s = "bbbbb"
#Output: 1

#Input: s = "pwwkew"
#Output: 3

from collections import defaultdict


def lengthOfLongestSubstring(input: str) -> int:
    chars = set()
    low, high, max_l = 0, 0, 0
    
    while high < len(input):
        if low == high:
            chars.add(input[low])
            high += 1
        else:
            if input[high] not in chars:
                chars.add(input[high])
                high += 1
            else:
                chars_len = len(chars)
                chars.remove(input[high])
                low += 1
                if chars_len > max_l:
                    max_l = chars_len

    return max_l

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("dvdf"))