'''
python里面的栈叫做： 最后进最先出队列
它的使用方式与 queue.Queue 类似，但是它的出队操作是从队尾（最后一个入队的元素）开始


对于栈来说，其实我们使用LifoQueue情况很少，一般用list就可以代替了
list[-1]就是栈顶
list.pop()就是出栈
'''


from queue import LifoQueue

# 创建一个后进先出队列实例
stack = LifoQueue()

# 入栈操作
stack.put(1)
stack.put(2)
stack.put(3)

# 查询栈元素个数
size = stack.qsize()
print("栈中的元素个数:", size)  # 输出：栈中的元素个数: 3

# 出栈操作
while not stack.empty():
    item = stack.get()
    print("出栈元素:", item)

# 再次查询栈元素个数
size = stack.qsize()
print("栈中的元素个数:", size)  # 输出：栈中的元素个数: 0



