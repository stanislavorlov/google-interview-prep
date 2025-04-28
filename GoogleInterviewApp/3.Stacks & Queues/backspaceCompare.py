# https://leetcode.com/problems/backspace-string-compare/

# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.

class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(input_str: str):
            stack = []
            for ch in input_str:
                if ch != '#':
                    stack.append(ch)
                elif stack:
                    stack.pop()

            return ''.join(stack)

        return backspace(s) == backspace(t)

solution = Solution()
print(solution.backspaceCompare("ab#c", "ad#c"))

print(solution.backspaceCompare("ab##", "c#d#"))

print(solution.backspaceCompare("a#c", "b"))

print(solution.backspaceCompare("y#fo##f", "y#f#o##f"))