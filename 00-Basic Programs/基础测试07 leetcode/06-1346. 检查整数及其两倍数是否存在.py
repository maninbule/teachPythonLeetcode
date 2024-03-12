'''
url: https://leetcode.cn/problems/check-if-n-and-its-double-exist/description/
'''
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        cnt = 0
        for x in arr:
            if x == 0:
                cnt += 1
        if cnt >= 2:
            return True

        st = set(arr)
        for x in arr:
            if 2 * x in st and x != 0:
                return True
        return False