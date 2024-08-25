'''
https://leetcode.cn/problems/binary-search/description/
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1 # [left,mid-1]
            else:
                left = mid + 1
        return -1