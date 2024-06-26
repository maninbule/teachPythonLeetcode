'''
https://leetcode.cn/problems/kth-distinct-string-in-an-array/description/
'''
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for x in arr:
            if arr.count(x) == 1:
                k -= 1
                if k == 0:
                    return x
        return ""