

'''
url: https://leetcode.cn/problems/majority-element/description/
'''
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
