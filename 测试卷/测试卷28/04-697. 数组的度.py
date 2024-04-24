'''
https://leetcode.cn/problems/degree-of-an-array/description/
'''
from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        from collections import defaultdict
        mp = defaultdict(int)
        max_times = 0
        for v in nums:
            mp[v] += 1
            max_times = max(max_times,mp[v])
        # 计算每一个数字的第一次出现位置，和最后一个出现的位置
        L = dict()# L[v]
        R = dict() # R[v]
        for i in range(len(nums)):
            if nums[i] not in L:
                L[nums[i]] = i
            R[nums[i]] = i
        # 遍历每一种数字，计算覆盖这种数字，需要的最小区间的长度
        ans = len(nums)
        for key in L.keys():
            if mp[key] == max_times:
                ans = min(ans,R[key] - L[key] + 1)
        return ans






