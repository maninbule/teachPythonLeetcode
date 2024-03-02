'''
url:https://leetcode.cn/problems/merge-similar-items/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
from typing import List

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        mp = defaultdict(int)
        for key,value in items1:
            mp[key] += value
        for key,value in items2:
            mp[key] += value        # values = [9,6,5]
        ans = []                    # keys = [3,1,4]
        for key,value in mp.items(): # items = [[3,9],[1,6],[4,5]]
            ans.append([key,value])
        ans.sort(key = lambda item:item[0])
        return ans