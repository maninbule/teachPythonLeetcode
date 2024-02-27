
import doctest

def solve(n:int)->list[int]:
    '''
    :param n: 数组的长度
    :return: 一个数组，数组长度为n，并且数组的两端从n开始，依次往中间依次减少1
    >>> solve(10)
    [10, 9, 8, 7, 6, 6, 7, 8, 9, 10]
    >>> solve(5)
    [5, 4, 3, 4, 5]
    '''
    # [n,n-1,n-2...n-2,n-1,n]




def solve2(n:int,m:int)->list[list[int]]:
    '''
    :param n: 矩阵的行数
    :param m: 矩阵的列数
    :return:一个矩阵，矩阵的第i行，第j列的元素值为i + j, i和j都从0开始
    >>> solve2(3,4)
    [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5]]
    >>> solve2(1,4)
    [[0, 1, 2, 3]]
    >>> solve2(4,1)
    [[0], [1], [2], [3]]
    '''
    arr = [[0] * m for i in range(n)]
    for i in range(n): # i 是行号
        for j in range(m): # j 是列号
            arr[i][j] = i + j
    return arr

if __name__ == '__main__':
    print(solve2(4,1))
