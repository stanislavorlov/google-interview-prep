# https://leetcode.com/problems/summary-ranges/
from typing import List


class Solution:
    @staticmethod
    def summary_ranges(nums: List[int]) -> List[str]:
        output = []
        n = len(nums)
        index = 0
        while index < len(nums):
            start, end = nums[index], nums[index]
            while index + 1 < n and nums[index]+1 == nums[index+1]:
                index = index + 1
                end = nums[index]
            if start != end:
                output.append(f"{start}->{end}")
            else:
                output.append(f"{start}")
            index = index + 1

        return output

solution = Solution()
input_list = [0, 1, 2, 4, 5, 7]
print(solution.summary_ranges(input_list))         # ["0->2","4->5","7"]

input_list = [0, 2, 3, 4, 6, 8, 9]
print(solution.summary_ranges(input_list))         # ["0","2->4","6","8->9"]