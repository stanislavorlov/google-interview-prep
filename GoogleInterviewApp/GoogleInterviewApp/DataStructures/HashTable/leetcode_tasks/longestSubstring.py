# Given a string s, find the length of the longest substring without repeating characters.

#Input: s = "abcabcbb"
#Output: 3

#Input: s = "bbbbb"
#Output: 1

#Input: s = "pwwkew"
#Output: 3

from collections import defaultdict


def lengthOfLongestSubstring(input: str) -> int:
    map = defaultdict(set)
    idx = 0
    for i,s in enumerate(input):
        map[s].add(i)
        #if s in map[idx]:
        #    idx += 1
        #map[idx].add(s)

    return 0

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("dvdf"))