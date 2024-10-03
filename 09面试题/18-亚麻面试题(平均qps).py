''''''

'''
下面有一个class，是在具有基础dict的功能上，
加上了可以分析Put函数和get函数调用频率的功能

measure_put_load：可以得出put函数在前5分钟的平均每秒调用次数,根据前5分钟的调用情况，得出qps
measure_get_load：可以得出get函数在前5分钟的平均每秒调用次数，根据前5分钟的调用情况，得出qps
'''

from collections import deque
import time
class Solution:
  def __init__(self):
    self.table = dict()
    self.put_queue = deque()
    self.get_queue = deque()
  def put(self, key, val):
    self.clear(self.put_queue)
    self.table[key] = val
    self.put_queue.append(time.time())
  def get(self, key):
    self.clear(self.get_queue)
    self.get_queue.append(time.time())
    return self.table[key]
  def measure_put_load(self):
    return len(self.put_queue)/300
  def measure_get_load(self):
    return len(self.get_queue) / 300
  def clear(self,q:deque):
    current_time = time.time()
    while len(q) > 0 and current_time - q[0] >= 300:
      q.popleft()


# follow up: todo
class Solution:
  def __init__(self):
    self.table = dict()
    self.put_queue = deque()
    self.get_queue = deque()
  def put(self, key, val):
    self.clear(self.put_queue)
    self.table[key] = val
    self.put_queue.append(time.time())
  def get(self, key):
    self.clear(self.get_queue)
    self.get_queue.append(time.time())
    return self.table[key]
  def measure_put_load(self):
    return len(self.put_queue)/300
  def measure_get_load(self):
    return len(self.get_queue) / 300
  def clear(self,q:deque):
    current_time = time.time()
    while len(q) > 0 and current_time - q[0] >= 300:
      q.popleft()
