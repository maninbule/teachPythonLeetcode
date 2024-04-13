'''
https://leetcode.cn/problems/find-the-difference-of-two-arrays/description/
'''
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = []
        ans2 = []
        st1 = set(nums1)
        st2 = set(nums2)
        for x in st1:
            if x not in st2:
                ans1.append(x)
        for x in st2:
            if x not in st1:
                ans2.append(x)
        return [ans1,ans2]