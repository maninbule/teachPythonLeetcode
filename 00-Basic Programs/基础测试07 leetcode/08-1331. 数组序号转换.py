
'''
url: https://leetcode.cn/problems/rank-transform-of-an-array/description/
'''
from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr2 = list(set(arr))
        arr2.sort()
        mp = dict()
        for i in range(0,len(arr2)):
            # arr2[i] -> i + 1
            mp[arr2[i]] = i + 1
        ans = []
        for x in arr:
            ans.append(mp[x])
        return ans
