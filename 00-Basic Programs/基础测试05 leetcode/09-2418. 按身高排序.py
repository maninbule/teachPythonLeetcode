
'''
url: https://leetcode.cn/problems/sort-the-people/description/
'''
from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        P = []
        for i in range(len(names)):
            P.append([names[i],heights[i]])
        P.sort(key = lambda item:-item[1])
        ans = []
        for p in P:
            ans.append(p[0])
        return ans