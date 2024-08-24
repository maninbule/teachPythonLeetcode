'''
https://leetcode.cn/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
'''
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort() # O(nlogn)
        count = dict()
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        # O(n)
        for x in nums:
            if count[x] > 0:
               need = count[x]
               # x + 1, x + 2...x + k - 1都要有count[x]次
               for y in range(x,x + k):
                 if y not in count:
                    return False
                 if count[y] < need:
                    return False
                 else:
                    count[y] -= need
        return True