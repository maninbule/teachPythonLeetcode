'''
https://leetcode.cn/problems/two-out-of-three/
'''
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        st1,st2,st3 = set(nums1),set(nums2),set(nums3)
        from collections import defaultdict
        cnt = defaultdict(int)
        for st in [st1,st2,st3]:
            for x in st:
                cnt[x] += 1
        ans = []
        for key,value in cnt.items():
            if value >= 2:
                ans.append(key)
        return ans
