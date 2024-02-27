def PriorityQueue_tuple():
    from queue import PriorityQueue
    # 创建一个优先级队列实例
    pq = PriorityQueue()

    # 入队操作
    pq.put((3, 'apple'))
    pq.put((1, 'banana'))
    pq.put((2, 'orange'))

    # 查询队列元素个数
    size = pq.qsize()
    print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 3

    # 出队操作
    while not pq.empty():
        priority, item = pq.get()
        print("出队元素:", item)

    # 再次查询队列元素个数
    size = pq.qsize()
    print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 0
