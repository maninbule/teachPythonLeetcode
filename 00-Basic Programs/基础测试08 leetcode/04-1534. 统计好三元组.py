'''
url:https://leetcode.cn/problems/count-good-triplets/description/
'''
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if  abs(arr[i]-arr[j]) <= a \
                        and abs(arr[j] - arr[k]) <= b \
                        and abs(arr[i] - arr[k]) <= c:
                            ans += 1
        return ans