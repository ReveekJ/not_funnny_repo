from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0

        res = 0
        for i in range(len(timeSeries) - 1):
            res += min(duration, timeSeries[i + 1] - timeSeries[i])

        res += duration
        return res


print(Solution().findPoisonedDuration([1,3,5,7,9,11,13,15], 1))