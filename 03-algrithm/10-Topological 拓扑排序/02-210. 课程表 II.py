'''
https://leetcode.cn/problems/course-schedule-ii/description/
'''
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # b -> a
        # (1) 建图
        from collections import defaultdict,deque
        graph = defaultdict(list)
        count = defaultdict(int)
        for x,y in prerequisites:
            # y -> x
            graph[y].append(x)
            count[x] += 1
        q = deque()
        for index in range(numCourses):
            if count[index] == 0:
                q.append(index)
        ans = []
        while len(q) > 0:
            x = q.popleft()
            ans.append(x)
            for y in graph[x]:
                count[y] -= 1
                if count[y] == 0:
                    q.append(y)
        if len(ans) != numCourses:
            ans = []
        return ans