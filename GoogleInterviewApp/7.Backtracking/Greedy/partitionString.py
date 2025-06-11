import unittest


class Solution:
    def partitionString(self, s: str) -> int:
        answer = 1
        hash_map = {}
        start = 0

        for idx, ch in  enumerate(s):
            if ch in hash_map and start <= hash_map[ch] < idx:
                answer += 1
                start = idx
            hash_map[ch] = idx

        return answer

    def partitionString2(self, s: str) -> str:
        last_seen = [-1] * 26
        count = 1
        substring_start = 0

        for i in range(len(s)):
            if last_seen[ord(s[i]) - ord('a')] >= substring_start:
                count += 1
                substring_start = i

            last_seen[ord(s[i]) - ord('a')] = i

        return count


class TestPartitionString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first(self):
        result = self.solution.partitionString("abacaba")

        self.assertEqual(4, result)

    def test_second(self):
        result = self.solution.partitionString("ssssss")

        self.assertEqual(6, result)