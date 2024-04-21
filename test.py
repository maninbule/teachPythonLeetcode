def solve(A: list[int], B: list[int]) -> float:
    m = len(A)
    n = len(B)
    length = m + n  # 总长度
    left = -1  # 保存旧的right值(也就是right的左边一个)
    right = -1  # 指向最新的一个已经合并的数
    a_start = 0  # A数组下标
    b_start = 0  # B数组下标

    for i in range(length // 2 + 1):  # 遍历一半的元素， + 1 是因为还需要中间靠右那个数
        left = right  # left保存之前的right的值
        # 应该合并a元素更小
        if a_start < m and (b_start >= n or A[a_start] < B[b_start]):
            right = A[a_start]
            a_start += 1
        else:  # b的元素更小
            right = B[b_start]
            b_start += 1
    # 长度为偶数，那么left,right刚好是中间那两个数
    if length % 2 == 0:
        return (left + right) / 2.0
    else:  # 长度为奇数，那么right刚好是中间那个数
        return right


# 思路
'''
将两个有序数组进行合并，合并到一半的时候，就知道了中位数是谁了

如果长度是奇数： 中位数只有一个
如果长度是偶数： 中位数 = (中间靠左的数 + 中间靠右的数)/2

时间复杂度O(n) 

'''

# 测试
A1 = [1, 3, 5]
B1 = [2, 4, 6]
print(solve(A1, B1))  # out = 3.5

# 测试用例2：一个长度为偶数、一个长度为奇数的数组
A2 = [1, 2, 3, 4]
B2 = [5, 6, 7]
print(solve(A2, B2))  # out = 4

# 测试用例3：两个长度为偶数的数组
A3 = [1, 3, 5, 7]
B3 = [2, 4, 6, 8]
print(solve(A3, B3))  # out = 4.5

A4 = [1]
B5 = [2, 3, 5, 6, 8]
print(solve(A4, B5))  # out = 4

