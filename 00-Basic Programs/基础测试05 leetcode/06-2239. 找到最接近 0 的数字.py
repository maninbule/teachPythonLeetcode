
'''
url: https://leetcode.cn/problems/find-closest-number-to-zero/description/
'''
from typing import List
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # if 0 in nums:
        #     return 0
        # positive = []
        # negitive = []
        # for v in nums:
        #     if v > 0:
        #         positive.append(v)
        #     else:
        #         negitive.append(v)
        # if len(positive) == 0:
        #     return max(negitive)
        # if len(negitive) == 0:
        #     return min(positive)
        # if abs(max(negitive)) < min(positive):
        #     return max(negitive)
        # else:
        #     return min(positive)
        ans = nums[0]
        for i in range(1,len(nums)):
            if abs(nums[i]) < abs(ans):
                ans = nums[i]
            if abs(nums[i]) == abs(ans):
                ans = max(nums[i],ans)
        return ans