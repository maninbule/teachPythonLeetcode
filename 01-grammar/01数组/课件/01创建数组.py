
'''
创建一维数组
'''
def solve1DArray(n:int)->list[int]:
    arr = [0] * n # 创建一个全是0的数组，数组长度为n (用的多)

    arr = [1] * n  # 创建一个全是1的数组，数组长度为n

    arr = list(range(1,n+1)) # 创建一个内容为1到n的数组

    arr = [i + 1 for i in range(n)] # 创建一个内容为1到n的数组 (用的多)

    return arr

'''
创建二维数组

创建nxm的矩阵，存在数组中
'''
def create2DArray(n:int,m:int)->list[list[int]]:
    arr = [[0] * m for i in range(n)] # (常用)

    arr = []
    for j in range(n): # 循环n次，每次往arr append一行，不常用
        arr[j] = [0 for i in range(m)]

    arr = [] # 每次只append一个元素，更不常用
    for i in range(n):
        row = []
        for j in range(m):
            row.append(0)
        arr.append(row)
    return arr

if __name__ == '__main__':
    print(solve1DArray(10))