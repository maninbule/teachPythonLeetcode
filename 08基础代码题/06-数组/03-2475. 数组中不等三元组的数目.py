'''
https://leetcode.cn/problems/number-of-unequal-triplets-in-array/description/
'''
from typing import List


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        total = len(nums)
        for x in nums:
            count[x] += 1
        nums = list(set(nums))
        nums.sort()
        leftCount = 0
        ans = 0
        for i in range(len(nums)):
            curCount = count[nums[i]] # (x,y,z) 中的y的数量
            rightCount = total - leftCount - curCount
            ans += leftCount * curCount * rightCount
            leftCount += curCount
        return ans



