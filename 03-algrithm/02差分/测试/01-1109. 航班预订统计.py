
'''
url: https://leetcode.cn/problems/corporate-flight-bookings/
'''
from typing import List
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ca = [0] * (n + 1)
        for b in bookings:
            l,r,cnt = b[0],b[1],b[2]
            l -= 1
            r -= 1
            ca[l] += cnt
            ca[r + 1] -= cnt # [l,r] += cnt
        pre = [0] * n
        pre[0]= ca[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + ca[i]
        return pre