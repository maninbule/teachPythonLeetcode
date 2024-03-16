'''
https://leetcode.cn/problems/contains-duplicate-ii/
'''
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastIndex = dict()
        for i in range(len(nums)):
            cur = nums[i]
            if cur in lastIndex and i - lastIndex[cur] <= k:
                return True
            lastIndex[cur] = i
        return False