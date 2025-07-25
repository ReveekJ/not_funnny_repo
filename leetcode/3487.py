from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_int = max(nums)
        nums = list(filter(lambda x: x > 0, set(nums)))

        if not nums:
            return max_int
        return sum(nums)


print(Solution().maxSum(nums=[-100]))
