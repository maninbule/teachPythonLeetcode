'''
https://leetcode.cn/problems/keep-multiplying-found-values-by-two/description/
'''
from typing import List
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = set(nums)
        while original in nums: # nums是list n次 | nums是set, 1次
            original *= 2
        return original