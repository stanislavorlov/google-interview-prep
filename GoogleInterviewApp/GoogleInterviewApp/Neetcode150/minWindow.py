# https://neetcode.io/problems/minimum-window-with-characters

# Given two strings s and t, return the shortest substring of s such that every character in t,
# including duplicates, is present in the substring. If such a substring does not exist, 
# return an empty string "".

# Input: s = "OUZODYXAZV", t = "XYZ"
# Output: "YXAZ"

# Input: s = "xyz", t = "xyz"
# Output: "xyz"

# Input: s = "x", t = "xy"
# Output: ""

from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        set_t = set(t)
        
        left = right = 0
        for right in range(len(s)):
            