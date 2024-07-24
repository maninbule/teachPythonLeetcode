'''
https://leetcode.cn/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/description/
'''
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis = -1
        ans = None
        for i in range(len(points)):
            x2,y2 = points[i]
            if x == x2 or y2 == y:
                dis = abs(x-x2) + abs(y - y2)
                if min_dis == -1:
                    min_dis = dis
                    ans = i
                else:
                    if dis < min_dis:
                        min_dis = dis
                        ans = i
        return ans

s = Solution()
ans = s.nearestValidPoint(3,4,[[1,2],[3,1],[2,4],[2,3],[4,4]])
print(ans)