'''
https://leetcode.cn/problems/sum-of-all-odd-length-subarrays/description/
'''
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for length in range(1,len(arr)+1,2): # 长度
            for left in range(len(arr)): # 枚举对于长度子数组的左端点
                right = left + length - 1
                if right >= len(arr): # 越界了
                    break
                # 现在arr[left,right]这一段就是长度为奇数的子数组
                for i in range(left,right + 1):
                    total += arr[i]
        return total
