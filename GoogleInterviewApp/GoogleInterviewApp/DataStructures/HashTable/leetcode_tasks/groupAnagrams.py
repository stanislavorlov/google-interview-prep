# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

import collections

# def hash_code(str):
#     code = 1
#     counter = collections.Counter(str)
#     for letter in counter:
#         code += ord(letter) * counter[letter]

#     return code

# def groupAnagrams(strs: list[str]) -> list[list[str]]:
#     hash_table = collections.defaultdict(list)
#     for str in strs:
#         hash_table[hash_code(str)].append(str)

#     counter = collections.Counter(hash_table)
#     return counter.values()

def groupAnagramsLeetCode(strs: list[str]) -> list[list[str]]:
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()

strs = ["ddddddddddg","dgggggggggg"]
#print(groupAnagramsLeetCode(strs))
strs = ["eat","tea","tan","ate","nat","bat"]
#print(groupAnagramsLeetCode(strs))
strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    dict = collections.defaultdict(list)
    for str in strs:
        dict[tuple(sorted(str))].append(str)

    return list(dict.values())

print(groupAnagrams(strs))