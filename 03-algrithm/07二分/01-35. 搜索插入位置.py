'''
https://leetcode.cn/problems/search-insert-position/description/
'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if ans != -1:
            return ans
        # 上面是找到了
        # 下面没有找到，去找插入的位置
        left,right = 0,len(nums)-1
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] < target: # 满足 [left,right] ,mid满足，于是就去[mid + 1,right]
                ans = mid
                left = mid + 1
            else: # target < nums[mid] [mid,right]x   -> [left,mid-1]
                right = mid - 1
        return ans + 1


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        ans = -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= target: # [left,right] ->[mid + 1,right]
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        # ans目前存储的是<=target的最后一个元素的下标
        if ans == -1:
            return 0
        elif nums[ans] == target: # == target
            return ans
        else:  # < target
            return ans + 1