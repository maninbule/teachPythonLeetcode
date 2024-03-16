'''
url: https://leetcode.cn/problems/check-if-n-and-its-double-exist/description/
'''
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        zeros = 0
        for v in arr:
            if v == 0:
                zeros += 1
        if zeros >= 2:
            return True
        st = set(arr)
        for v in arr:
            if v == 0:
                continue
            if 2*v in st:
                return True
        return False


