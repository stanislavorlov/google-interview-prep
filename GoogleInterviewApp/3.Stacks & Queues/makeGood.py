# https://leetcode.com/problems/make-the-string-great/description/

# To make the string good, you can choose two adjacent characters that make the string bad and remove them.
# You can keep doing this until the string becomes good.

class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and ch.lower() == stack[-1].lower() and ch != stack[-1]:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)

solution = Solution()
print(solution.makeGood("leEeetcode"))

print(solution.makeGood("abBAcC"))

print(solution.makeGood("s"))