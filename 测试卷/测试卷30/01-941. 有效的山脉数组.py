'''
https://leetcode.cn/problems/valid-mountain-array/description/
'''
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        cnt = 0 # 山峰
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                cnt += 1
            if arr[i-1] > arr[i] < arr[i+1]:
                return False
            if arr[i-1] == arr[i] or arr[i] == arr[i + 1]:
                return False
        return cnt == 1
