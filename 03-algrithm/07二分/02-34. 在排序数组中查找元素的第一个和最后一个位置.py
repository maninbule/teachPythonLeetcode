'''
https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 找target左端
        left, right = 0, len(nums) - 1
        ansleft = -1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                ansleft = mid
                right = mid - 1  # [left,mid-1]
            else:  # nums[mid] < target <= xxxxxx
                left = mid + 1  # [mid + 1,right]
        left, right = 0, len(nums) - 1
        ansright = -1  # <= target的最右端
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                ansright = mid
                left = mid + 1  # [mid + 1,right]
            else:
                right = mid - 1
        if ansleft != -1 and nums[ansleft] != target:
            ansleft = -1
        if ansright != -1 and nums[ansright] != target:
            ansright = -1
        return [ansleft, ansright]
