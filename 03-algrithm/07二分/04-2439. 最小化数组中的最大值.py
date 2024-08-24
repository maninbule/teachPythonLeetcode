'''
https://leetcode.cn/problems/minimize-maximum-of-array/description/
'''
import copy
from typing import List

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        left,right = min(nums),max(nums)
        ans = -1
        while left <= right:
            mid = (left + right)//2
            arr = copy.copy(nums)
            ok = True
            for i in range(n-1,-1,-1):
                if i > 0 and arr[i] > mid:
                    more = arr[i] - mid
                    arr[i-1] += more
                if i == 0 and arr[i] > mid:
                    ok = False
            if ok:
                ans = mid
                right = mid - 1 # [left,mid-1]
            else:
                left = mid + 1
        return ans
