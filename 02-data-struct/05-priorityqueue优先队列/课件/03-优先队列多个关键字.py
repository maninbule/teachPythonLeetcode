def PriorityQueue_tuple2():
    from queue import PriorityQueue
    # 创建一个优先级队列实例
    pq = PriorityQueue()

    # 入队操作
    pq.put((3,-4, 'apple'))
    pq.put((3,-2, 'banana'))
    pq.put((2,3, 'orange'))

    # 查询队列元素个数
    size = pq.qsize()
    print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 3

    # 出队操作
    while not pq.empty():
        priority1,priority2, item = pq.get()
        print("出队元素:", item)

    # 再次查询队列元素个数
    size = pq.qsize()
    print("队列中的元素个数:", size)  # 输出：队列中的元素个数: 0
