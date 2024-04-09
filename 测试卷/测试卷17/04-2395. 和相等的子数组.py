'''
https://leetcode.cn/problems/find-subarrays-with-equal-sum/description/
'''
from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        arr = [] # 占空间，空间复杂度是O(n)
        for i in range(1,len(nums)):
            arr.append(nums[i-1] + nums[i])
        return len(arr) != len(set(arr))


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        from collections import defaultdict
        cnt = defaultdict(int)
        for i in range(1,len(nums)):
            pair_sum = nums[i-1] + nums[i]
            cnt[pair_sum] += 1
            if cnt[pair_sum] >= 2:
                return True
        return False
