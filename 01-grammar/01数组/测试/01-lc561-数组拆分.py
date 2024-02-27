'''
url:https://leetcode.cn/problems/array-partition/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        sum = 0
        # [0,1,2,3]
        for i in range(0,n,2): # range(0,n,2) = [0,2]
            # i = 0,2
            sum += min(nums[i],nums[i+1])
        return sum

