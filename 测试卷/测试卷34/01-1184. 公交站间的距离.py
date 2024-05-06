'''
https://leetcode.cn/problems/distance-between-bus-stops/description/
'''
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        cur = 0
        while start != destination:
            cur += distance[start]
            start = (start + 1) % len(distance)
        return min(cur,total-cur)

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        total = sum(distance)
        cur = 0
        while start != destination:
            cur += distance[start]
            start = start + 1
            if start == len(distance):
                start = 0
        return min(cur,total-cur)
