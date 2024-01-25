# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

class Solution:

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]: # type: ignore
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        intercept = set()
        result = []
        for val in nums1:
            if val in nums2 and val not in intercept:
                intercept.add(val)
                result.append(val)

        return result
    
solution = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]

print(solution.intersection(nums1, nums2))
