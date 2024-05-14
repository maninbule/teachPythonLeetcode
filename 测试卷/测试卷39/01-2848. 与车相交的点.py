'''
https://leetcode.cn/problems/points-that-intersect-with-cars/description/
'''
from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        point = [0] * 105
        for L in nums:
            l,r = L
            for j in range(l,r + 1):
                point[j] = 1
        cnt = 0
        for x in point:
            cnt += x
        return cnt

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        point = [0] * 105
        for L in nums:
            l,r = L
            for j in range(l,r + 1):
                point[j] = 1
        return sum(point)