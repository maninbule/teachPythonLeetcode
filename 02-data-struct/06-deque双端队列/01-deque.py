'''
方法：
从右端（队尾）添加元素：使用 append() 方法。
从左端（队首）添加元素：使用 appendleft() 方法。
从双端队列中删除元素：

从右端（队尾）删除元素：使用 pop() 方法。
从左端（队首）删除元素：使用 popleft() 方法。
'''

from collections import deque

# 创建双端队列
dq = deque()
# 从右端添加元素
dq.append(1)
dq.append(2)
dq.append(3)
# 从左端添加元素
dq.appendleft(0)
# 打印双端队列的内容和长度
print("Deque:", dq)
print("Length:", len(dq))

# 从右端删除元素
dq.pop()

# 从左端删除元素
dq.popleft()

# 打印删除后的双端队列内容和长度
print("Deque after deletion:", dq)
print("Length after deletion:", len(dq))
