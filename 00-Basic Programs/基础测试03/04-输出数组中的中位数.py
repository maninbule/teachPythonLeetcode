

'''
04-输出数组中的中位数

如果数组的长度是偶数，中位数位中间的两个数求和除2向下取整
'''

def getMiddle(arr:list[int])->int:
    n = len(arr)
    arr.sort()
    if n % 2 == 1:
        return arr[n//2] # [0,1,2] n = 3  n//2 = 1
    else:
        return int((arr[n//2-1] + arr[n//2])/2) # [0,1,2,3] n = 4 4//2 = 2

assert getMiddle([1,2,3,4,5]) == 3
assert getMiddle([5,4,3,2,1]) == 3
assert getMiddle([4,2,3,1]) == 2
print("pass")