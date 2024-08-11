'''
https://leetcode.cn/problems/course-schedule/
'''

from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque,defaultdict
        indegree = [0] * numCourses
        q = deque()
        graph = defaultdict(list)
        for p in prerequisites:
            a,b = p
            graph[b].append(a) # b -> a
            indegree[a] += 1
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        count = 0
        while len(q) > 0:
            x = q.popleft()
            count += 1
            for y in graph[x]:
                indegree[y] -= 1
                if indegree[y] == 0:
                    q.append(y)
        return count == numCourses
