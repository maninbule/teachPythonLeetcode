# https://leetcode.cn/problems/find-common-elements-between-two-arrays/description/
from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1 = set(nums1)
        st2 = set(nums2)
        cnt1,cnt2 = 0,0
        for x in nums1:
            if x in st2:
                cnt1 += 1
        for x in nums2:
            if x in st1:
                cnt2 += 1
        return [cnt1,cnt2]
