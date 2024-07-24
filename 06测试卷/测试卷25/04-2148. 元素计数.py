'''
https://leetcode.cn/problems/count-elements-with-strictly-smaller-and-greater-elements/description/
'''
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_value = min(nums) # O(n)
        max_value = max(nums)
        cnt = 0
        for v in nums:
            if v != min_value and v != max_value:
                cnt += 1
        return cnt

class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_value = nums[0]
        max_value = nums[0]
        for v in nums:
            min_value = min(min_value,v)
            max_value = max(max_value, v)
        cnt = 0
        for v in nums:
            if v != min_value and v != max_value:
                cnt += 1
        return cnt