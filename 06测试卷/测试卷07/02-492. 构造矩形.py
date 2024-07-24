'''
https://leetcode.cn/problems/construct-the-rectangle/description/
'''
from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ansL,ansW = area,1
        min_diff = area - 1
        for L in range(1,area + 1):
            if area % L == 0:
                W = area//L
                # L *  W =  area
                if L - W < min_diff and L >= W:
                    min_diff = L - W
                    ansL,ansW = L,W
        return [ansL,ansW]

s = Solution()
ans = s.constructRectangle(122122)
print(ans)