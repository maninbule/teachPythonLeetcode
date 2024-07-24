'''
https://leetcode.cn/problems/find-the-distinct-difference-array/description/
'''
from typing import List


class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L,R = [0] * n,[0] * n # L[i] = len(set(nums[:i]))
        st = set()
        for i in range(n):
            st.add(nums[i])
            L[i] = len(st)
        st = set()
        for i in range(n-1,-1,-1):
            R[i] = len(st)
            st.add(nums[i])
        # ans[i] = L[i] - R[i]
        ans = [0] * n
        for i in range(n):
            ans[i] = L[i] - R[i]
        return ans