# https://leetcode.com/problems/longest-palindrome/description/

import unittest
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        odd = False
        for key, value in sorted_counter:
            if value % 2 == 0:
                ans += value
            else:
                ans += value if not odd else value - 1
                odd = True

        return ans

    def longestPalindrome_set(self, s: str) -> int:
        character_set = set()
        res = 0

        for c in s:
            if c in character_set:
                res += 2
                character_set.remove(c)
            else:
                character_set.add(c)

        if character_set:
            res += 1

        return res

class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        s = "abccccdd"
        self.assertEqual(self.solution.longestPalindrome_set(s), 7)

    def test_second(self):
        s = "a"
        self.assertEqual(self.solution.longestPalindrome_set(s), 1)

    def test_third(self):
        s = "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
        self.assertEqual(self.solution.longestPalindrome_set(s), 983)