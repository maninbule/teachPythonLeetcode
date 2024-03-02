'''
url:https://leetcode.cn/problems/intersection-of-two-arrays/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1 = set(nums1)
        st2 = set(nums2)
        ans = []
        for item in st1: # 一个一个取
            if item in st2: # 在一堆数里面查询item里面在不在
                ans.append(item)
        return ans