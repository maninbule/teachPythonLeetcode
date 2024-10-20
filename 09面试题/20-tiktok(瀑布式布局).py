'''
输入：
    1. 屏幕的宽度
    2. 屏幕有几列
    3. 每个矩形的高度
每次来一个新的矩阵，摆放位置优先靠上，其次靠左
输出：
    根据摆放的方案，输出每一个矩形摆放后的左上角，以及宽度和高度
        一个矩形的摆放位置就是这样一个数组来表示[0,0,5,10] (x,y,宽度,高度)
'''

def solution(total_width:int,columns:int,rect:list[int])->list[list[int]]:
    rect_width = total_width // columns
    H = [0] * columns
    result = []
    for r_h in rect: # 遍历每一个矩阵的高度
        min_h_index = 0 # 记录高度最低列的Index
        for j in range(columns):
            if H[j] < H[min_h_index]:
                min_h_index = j
        # min_h_index 高度最小列的index
        x = min_h_index * rect_width
        y = H[min_h_index]
        result.append([x,y,rect_width,r_h])
        H[min_h_index] += r_h
    return result

total_width = 8
columns = 4
rect = [1,3,2,5,2,5,1]
print(solution(total_width,columns,rect))

'''
时间复杂度： O(n*m) n是矩阵的个数，m是列数
空间复杂度： O(n + m) 开了两个数组，O(n)是存储每一个矩阵摆放后的位置，一个O(m)是存储每一列当前的高度

时间复杂度可以优化成: O(n * logm)

下面是使用优先队列的形式来做：
'''
from queue import PriorityQueue
class node:
    def __init__(self,index,h) -> None:
        self.index = index
        self.h = h
    def __lt__(self,other):
        return self.h < other.h
def solution2(total_width:int,columns:int,rect:list[int])->list[list[int]]:
    rect_width = total_width // columns
    q = PriorityQueue()
    result = []
    for index in range(columns):
        q.add(node(index,0))
    for r_h in rect:
        minH_column = q.get()
        index = minH_column.index
        curHeight = minH_column.h
        result.append([index * rect_width,curHeight,rect_width,r_h])
        q.add(node(index,curHeight + r_h))
    return result

total_width = 8
columns = 4
rect = [1,3,2,5,2,5,1]
print(solution(total_width,columns,rect))