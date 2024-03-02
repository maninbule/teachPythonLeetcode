
'''
01-计算数组中k个连续数字的和

[1,2,3,4,5,6]
k = 3
第1个连续3个数为[1,2,3] = 6
第2个连续3个数为[2,3,4] = 9
第3个连续3个数为[3,4,5] = 12
第4个连续3个数为[4,5,6] = 15
返回 [6,9,12,15]
'''

def getSumOfK(arr:list[int],k:int)->list[int]:
    from queue import Queue
    sum = 0
    q = Queue()
    ans = []
    for v in arr:
        q.put(v) # 入队
        sum += v
        if q.qsize() > k: # 控制出队
            d = q.get()
            sum -= d
        if q.qsize() == k:
            ans.append(sum)
    return ans

assert getSumOfK([1,2,3,4,5,6],3) == [6,9,12,15]
print("pass")