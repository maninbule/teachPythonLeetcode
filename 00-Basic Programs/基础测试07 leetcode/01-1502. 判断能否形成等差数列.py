
'''
url: https://leetcode.cn/problems/can-make-arithmetic-progression-from-sequence/description/?envType=study-plan-v2&envId=programming-skills
'''
from typing import List
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        first = arr[1] - arr[0]
        for i in range(2,len(arr)):
            dif = arr[i] - arr[i-1]
            if dif != first:
                return False
        return True
