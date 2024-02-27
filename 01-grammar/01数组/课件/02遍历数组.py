

'''
遍历一维数组

'''

def trverse1DArray(arr:list[int]):
    # 第一种，不带index的方式
    for v in arr:
        print(v,end=" ")
    print()
    print("---------------------------")
    # 第二种，通过index遍历
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

'''
遍历二维数组
'''
def trverse2DArray(arr:list[list[int]]):
    # 第一种，不通过index
    for row in arr:
        for value in row:
            print(value,end=" ")
        print()
    print("---------------------------")
    # 第二种，完全通过index
    # arr = [[1,2,3],[4,5,6]]
    # len([[1,2,3],[4,5,6]]) = 2
    for i in range(len(arr)): # i: 0,1
        for j in range(len(arr[i])): # arr[i] = [1,2,3] len([1,2,3]) = 3
            # range(3) range(0,3,1) j: 0 1 2
            print(arr[i][j],end=" ")
        print()
if __name__ == '__main__':
    arr = [[1,2,3],[4,5,6]]
    trverse2DArray(arr)
