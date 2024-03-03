
'''
https://leetcode.cn/problems/sort-even-and-odd-indices-independently/description/
'''
from typing import List

class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        ans = []
        i = 0
        j = 0
        while i < len(even) and j < len(odd):
            ans.append(even[i])
            i += 1
            ans.append(odd[j])
            j += 1
        if i < len(even):
            ans.append(even[i])
        return ans
