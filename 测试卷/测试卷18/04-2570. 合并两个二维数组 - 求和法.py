'''
https://leetcode.cn/problems/merge-two-2d-arrays-by-summing-values/
'''
from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        cnt = defaultdict(int)
        for pair in nums1:
            cnt[pair[0]] += pair[1]
        for pair in nums2:
            cnt[pair[0]] += pair[1]
        ans = []
        for key,value in cnt.items():
            ans.append([key,value])
        ans.sort(key=lambda pair:pair[0])
        return ans

