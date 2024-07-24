'''
https://leetcode.cn/problems/check-if-array-is-good/description/
'''
from typing import List


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort() # nlogn
        n = len(nums)-1
        for i in range(0,n-1): #
            if nums[i] != i + 1:
                return False
        if nums[n-1] != n or nums[n] != n:
            return False
        return True

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)-1
        from collections import defaultdict
        mp = defaultdict(int)
        for x in nums:
            mp[x] += 1
        for x in range(1,n):
            if mp[x] != 1:
                return False
        if mp[n] != 2:
            return False
        return True

