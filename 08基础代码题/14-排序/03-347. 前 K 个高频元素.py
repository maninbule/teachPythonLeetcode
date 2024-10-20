'''
https://leetcode.cn/problems/top-k-frequent-elements/description/?envType=problem-list-v2&envId=hash-table
'''
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for v in nums:
            if v in cnt:
                cnt[v] += 1
            else:
                cnt[v] = 1
        pair = []
        for x,count in cnt.items():
            pair.append([x,count])
        pair.sort(key=lambda x:-x[1])
        return [x[0] for x in pair[:k]]