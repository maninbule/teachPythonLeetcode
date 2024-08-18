'''
https://leetcode.cn/problems/container-with-most-water/description/
'''
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        ans = 0
        while left < right:
            length = right - left
            if height[left] <= height[right]:
                ans = max(ans,length * height[left])
                left += 1
            else:
                ans = max(ans,length * height[right])
                right -= 1
        return ans