
'''
url: https://leetcode.cn/problems/min-max-game/description/
'''
from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) > 1:
            A = []
            tag = 0
            for i in range(0,len(nums),2):# 0 2 4
                if tag == 0: # i = 0, min(nums[0],nums[1])
                    A.append(min(nums[i],nums[i+1]))
                    tag = 1
                else:
                    A.append(max(nums[i],nums[i+1]))
                    tag = 0
            nums = A
        return nums[0]

s = Solution()
s.minMaxGame([1,3,5,2,4,8,2,2])
