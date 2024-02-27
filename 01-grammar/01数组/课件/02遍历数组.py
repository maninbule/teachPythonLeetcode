

'''
遍历一维数组
'''

def trverse1DArray(arr:list[int]):
    # 第一种，不带index的方式
    for v in arr:
        print(v,end=" ")
    print()

    # 第二种，通过index遍历
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()

'''
遍历二维数组
'''
def trverse2DArray(arr:list[list[int]]):
    # 第一种，不通过index
    for line in arr:
        for value in line:
            print(value,end=" ")
        print()

    # 第二种，完全通过index
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j],end=" ")
        print()
