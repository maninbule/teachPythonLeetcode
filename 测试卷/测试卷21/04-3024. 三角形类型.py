'''
https://leetcode.cn/problems/type-of-triangle/description/
'''
from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        a, b, c = nums
        if not (a + b > c):return "none"
        st = set(nums)
        if len(st) == 1: return "equilateral"
        elif len(st) == 2: return "isosceles"
        else: return "scalene"

