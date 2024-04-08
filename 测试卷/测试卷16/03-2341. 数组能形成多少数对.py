'''
https://leetcode.cn/problems/maximum-number-of-pairs-in-array/description/
'''
from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        cnt = defaultdict(int)
        pairs = 0
        left = 0
        for x in nums:
            cnt[x] += 1
        for key,value in cnt.items(): # {3:2,2:3,1:2}
            pairs += value//2
            left += value%2
        return [pairs,left]