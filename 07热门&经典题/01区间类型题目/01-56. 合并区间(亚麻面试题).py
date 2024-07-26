'''
https://leetcode.cn/problems/merge-intervals/description/
'''

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if intervals == []:
            return []
        intervals.sort(key=lambda x:x[0])
        ans = []
        cur = intervals[0]
        for i in range(1,len(intervals)):
             next = intervals[i]
             if next[0] <= cur[1]:
                 cur[1] = max(cur[1],next[1])
             else:
                 ans.append(cur)
                 cur = next
        ans.append(cur)
        return ans