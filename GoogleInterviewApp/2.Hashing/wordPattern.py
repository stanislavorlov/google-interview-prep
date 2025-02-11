# Given a pattern and a string s, find if s follows the same pattern.
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False

        s_to_pattern = {}
        pattern_to_s = {}
        for word, p in zip(s.split(), pattern):
            if word not in s_to_pattern and p not in pattern_to_s:
                s_to_pattern[word] = p
                pattern_to_s[p] = word
            else:
                if s_to_pattern.get(word) != p and pattern_to_s.get(p) != word:
                    return False

        return True

solution = Solution()
solution.wordPattern("abba", "dog cat cat dog")

### Optimized solution
# def wordPattern(self, pattern: str, str: str) -> bool:
#     str = str.split(' ')
#     if not len(str) == len(pattern):
#             return False
#     return len(set(zip(pattern, str))) == len(set(str)) == len(set(pattern))