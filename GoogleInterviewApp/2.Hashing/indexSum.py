# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

# Given two arrays of strings list1 and list2, find the common strings with the least index sum.

# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]
# Explanation: There are three common strings:
# "happy" with index sum = (0 + 1) = 1.
# "sad" with index sum = (1 + 0) = 1.
# "good" with index sum = (2 + 2) = 4.
# The strings with the least index sum are "sad" and "happy".
# All the strings of list1 are unique.
# All the strings of list2 are unique.

import sys

# put first list into HashMap
# iterate over the second list
# calculate the sum of indexes, if less, put a new sum and elem into array
# if equal, put element to existing array

def findRestaurant(list1: list[str], list2: list[str]) -> list[str]:
    map = {}
    res = []

    min = sys.maxsize
    for idx, word in enumerate(list1):
        map[word] = idx

    for idx, word in enumerate(list2):
        if word in map:
            sum = map[word] + idx
            if sum < min:
                res = [word]
                min = sum
            else:
                if sum == min:
                    res.append(word)

    return res

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]

findRestaurant(list1, list2)

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]

findRestaurant(list1, list2)