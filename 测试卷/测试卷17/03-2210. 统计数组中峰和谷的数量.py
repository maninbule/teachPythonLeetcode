'''
https://leetcode.cn/problems/count-hills-and-valleys-in-an-array/description/
'''
from typing import List


class Solution:
    def countHillValley(self, nums: List[int])  -> int:
        arr = []
        for i in range(0,len(nums)):
            if i == 0:
                arr.append(nums[i])
            else:
                if nums[i] != nums[i-1]:
                    arr.append(nums[i])
        ans = 0
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                ans += 1
            elif arr[i-1] > arr[i] < arr[i + 1]:
                ans += 1
        return ans

'''
https://leetcode.cn/problems/count-hills-and-valleys-in-an-array/description/
'''
from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = []
        for i in range(0,len(nums)):
            if i - 1>=0 and nums[i] == nums[i-1]:
                continue
            arr.append(nums[i])
        ans = 0
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                ans += 1
            elif arr[i-1] > arr[i] < arr[i + 1]:
                ans += 1
        return ans