'''
https://leetcode.cn/problems/shuffle-the-array/description/
'''
from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        A = nums[:n] # [0,n-1]
        B = nums[n:] # [n,2*n-1]
        C = []
        i,j = 0,0
        while i < len(A) and j < len(B):
            C.append(A[i])
            C.append(B[j])
            i,j = i + 1,j + 1
        return C