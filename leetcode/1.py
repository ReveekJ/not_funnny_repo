from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        q = {}
        for index, elem in enumerate(nums):
            if q.get(elem) is not None:
                return [q.get(elem), index]
            q[target - elem] = index
