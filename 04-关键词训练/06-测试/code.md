


# (1) 给你一个int类型的数组，输出有多少对相等的相邻元素


# (2) 给你一个defaultdict，同时遍历这个defaultdict的key和value,并输出
    from collections import defaultdict
    cnt = defaultdict(int)
    # 完成后续代码

# (3) 创建一个二维数组arr，第一维度为n，第二维度为m(可以理解为nxm的矩阵)
    # arr = [[0] * m,[0]*m,[0] *m....n]
    arr = [[0] * m for i in range(n)]
# (4) 创建一个二维数组arr，第一维度为n，第二维度为m(可以理解为nxm的矩阵) 并把这个二维数组的所有元素赋值成1
    arr = [[1] * m for i in range(n)]
# (5) 给你一个偶数长度的int数组，输出中位数. (偶数长度的数组中位数 = 中间2个和除以2)

# (6) 给你一个奇数长度的int数组，输出中位数. 

# (7) 给你一个int类型的数组，问有多少种二元组(arr[i],arr[j])相加等于k
    注意是多少种：例如 k = 7 如果有2个(3,4)，(3,4)只算一个
    arr = [1,2,3,2,3,5,7]
    k = 5
    ans = set()
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:continue
            if arr[i] + arr[j] == k:
                ans.add((arr[i],arr[j]))
    print(len(ans))
    

# (8) 将一个字符串s转换成列表，举例： s = "abc" -> arr = ['a','b','c']

# (9) 给你2个int类型的数组，将两个数组合并，然后再排序

# (10) 给你一个int整数x，输出这个x可以被2整除多少次，例如：12->2次，16->4次