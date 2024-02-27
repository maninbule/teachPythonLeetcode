
'''

只能末尾入队，头部出队，就像水管一样
'''
from queue import Queue

# 创建一个队列实例
q = Queue()

# 入队操作
q.put(1)
q.put(2)
q.put(3)

# 查询队列元素个数
size = q.qsize()
print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 3

# 出队操作
while not q.empty():
    item = q.get()
    print("出队元素:", item)

# 再次查询队列元素个数
size = q.qsize()
print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 0
