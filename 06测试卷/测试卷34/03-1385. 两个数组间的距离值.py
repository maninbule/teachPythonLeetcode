'''
https://leetcode.cn/problems/find-the-distance-value-between-two-arrays/description/
'''
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for x in arr1:
            flag = True
            for y in arr2:
                if abs(x - y) <= d:
                    flag = False
                    break
            if flag:
                ans += 1
        return ans
