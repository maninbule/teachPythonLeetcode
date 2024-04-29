'''
https://leetcode.cn/problems/path-crossing/description/
'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {'N':[0,1],'S':[0,-1],'E':[1,0],'W':[-1,0]}
        pos = [(0,0)]
        x,y = 0,0
        for p in path:
            dx,dy = dir[p]
            x,y = x + dx,y + dy
            pos.append((x,y))
        return len(pos) != len(set(pos))

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dir = {'N':[0,1],'S':[0,-1],'E':[1,0],'W':[-1,0]}
        path_pos = set()
        x,y = 0,0
        path_pos.add((0,0))
        for p in path:
            dx,dy = dir[p]
            x,y = x + dx,y + dy
            if (x,y) in path_pos:
                return True
            else:
                path_pos.add((x,y))
        return False