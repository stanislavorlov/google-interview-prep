# https://leetcode.com/problems/first-unique-character-in-a-string/description/

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Input: s = "leetcode"
# Output: 0

# Input: s = "loveleetcode"
# Output: 2

from collections import defaultdict

def firstUniqChar(s: str) -> int:
    map = defaultdict(list)
    for idx, c in enumerate(s):
        map[c].append(idx)

    for _,v in enumerate(map):
        if len(map[v]) == 1:
            return map[v][0]
        
    return -1

print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("dddccdbba"))
