
'''
url: https://leetcode.cn/problems/divide-array-into-equal-pairs/description/
'''
from typing import List
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import defaultdict
        count = defaultdict(int)
        # {3:2,2:4}
        for v in nums:
            count[v] += 1
        for value in count.values(): # [2,4]
            if value % 2 == 1:
                return False
        return True
