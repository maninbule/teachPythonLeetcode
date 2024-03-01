

'''
09求二维数组的元素和
'''

def sumOf2Darray(arr:list[list[int]])->int:
    sum = 0
    for i in range(len(arr)): # 0 1 2
        for j in range(len(arr[i])): # 0 1 2 3
            sum += arr[i][j]
    return sum

A = [[1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]]

print(sumOf2Darray(A))