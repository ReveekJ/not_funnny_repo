from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for index, elem in enumerate(min(strs)):
            for j in strs:
                if j[index] != elem:
                    break
            else:
                res += elem
                continue
            break

        return res
