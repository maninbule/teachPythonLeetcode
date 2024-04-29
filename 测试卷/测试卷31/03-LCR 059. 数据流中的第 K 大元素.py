'''
https://leetcode.cn/problems/jBjn9C/description/
'''
from typing import List
from queue import PriorityQueue

class KthLargest:
    class node:
        def __init__(self,x:int):
            self.x = x
        def __lt__(self, other):
            return self.x < other.x
    def __init__(self, k: int, nums: List[int]):
        self.q = PriorityQueue()
        self.k = k
        for x in nums:
            self.add(x)
    def add(self, val: int) -> int:
        self.q.put(val)
        if self.q.qsize() > self.k:
            self.q.get()
        return self.q.queue[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)