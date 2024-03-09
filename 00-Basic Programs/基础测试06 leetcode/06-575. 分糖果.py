
'''
url: https://leetcode.cn/problems/distribute-candies/description/
'''
from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        can = len(candyType)//2
        uniques = len(set(candyType))
        return min(can,uniques)
