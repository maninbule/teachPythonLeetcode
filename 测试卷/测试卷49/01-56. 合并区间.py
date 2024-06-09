'''
https://leetcode.cn/problems/merge-intervals/description/
'''

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if intervals == []:
            return []
        intervals.sort(key=lambda x:x[0])
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if  intervals[i][0] <= ans[-1][1]:
                l = min(ans[-1][0],intervals[i][0])
                r = max(ans[-1][1],intervals[i][1])
                ans[-1] = [l,r]
            else:
                ans.append(intervals[i])
        return ans

