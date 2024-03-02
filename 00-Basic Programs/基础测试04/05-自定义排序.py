
'''
05-自定义排序

给你一个数组，数组里面元素是一个[x,y] 表示坐标
我们需要把所有的坐标按照优先按x升序，再按y降序
'''

def sortOfxyArray(pos:list[list[int]])->list[list[int]]:
    pos.sort(key = lambda item:(item[0],-item[1]))
    return pos

assert sortOfxyArray([[2,3],[1,1],[1,0],[4,5],[4,6]]) == [[1,1],[1,0],[2,3],[4,6],[4,5]]
assert sortOfxyArray([[4,5],[4,6],[1,1],[1,0],[2,3]]) == [[1,1],[1,0],[2,3],[4,6],[4,5]]
assert sortOfxyArray([[1,1]]) == [[1,1]]
assert sortOfxyArray([]) == []
print("pass")
