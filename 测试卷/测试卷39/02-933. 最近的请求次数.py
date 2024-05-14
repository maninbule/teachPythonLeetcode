'''
https://leetcode.cn/problems/number-of-recent-calls/description/
'''
from collections import deque
class RecentCounter:
    def __init__(self):
        self.q = deque()
    def ping(self, t: int) -> int:
        self.q.append(t)
        while len(self.q) > 0 and self.q[0] < t-3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)