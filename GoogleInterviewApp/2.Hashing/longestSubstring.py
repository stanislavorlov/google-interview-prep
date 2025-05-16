# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Given a string s, find the length of the longest substring without repeating characters.

#Input: s = "abcabcbb"
#Output: 3

#Input: s = "bbbbb"
#Output: 1

#Input: s = "pwwkew"
#Output: 3

from collections import defaultdict


def lengthOfLongestSubstring(input: str) -> int:
    map = {}
    max_length = 0
    for idx, ch in enumerate(input):
        if not ch in map:
            map[ch] = idx
            max_length += 1
        else:
            pos = map[ch]
            max_length = max(max_length, idx - pos)
            map[ch] = idx
            
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("dvdf"))