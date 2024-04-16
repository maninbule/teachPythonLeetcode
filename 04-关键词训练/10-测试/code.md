

# (1) 给你两个字符串s，t，问两个字符串有多少个字符是相同的？
    ans = 0
    st = set(t)
    for c in s:
        if c in st:
            ans += 1
    print(ans)
# (2) 给你4个正整数a,b,c,d，是否可以用a,b,c,d作为边长，构成一个矩形

# (3) 给你一个整数x，一个整数y，其中x < y,求满足x*k>=y的最小正整数k
    4/2 = 2
    5/2 = 2--1 ->3
    if y % x == 0:
        return y // x
    else:
        return y//x + 1
    print((y + x-1)//x)
# (4) 给你一个int数组，将奇数下标的元素+1,偶数下标的元素-1，输出操作之后的数组元素

# (5) 给你一个int数组，你每次操作可以选择一个元素+1，问至少经过多少次操作，才可以让这个int数组严格递增

# (6) 给你一个int数组，将这个数组整体循环往右移动2次
    例如：[1,2,3,4]->[4,1,2,3]->[3,4,1,2]
    arr = [1,2,3,4,5,6]
    k = 2
    print(arr[-k:] + arr[:-k])
# (8) 给你一个list[list[int]]类型的数组，其中list[int]类型中只会出现2个元素，请按照下标为1的元素进行从大到小排序
    arr = [[1,2],[2,3],[5,1]]
    arr.sort(key = lambda x:-x[1])
    print(arr)
# (9) 给你一个list[str]的数组，按照str的字符串长度从小到大排序，长度一样的按照字符串的字典序排序
    arr = ["app","apple","hello","abc","d"]
    arr.sort(key=lambda x:(len(x),x))
    print(arr)
# (10) 给你一个只包含小写字母的字符串，保留大于等于'h'的字母，其余字母删除，输出剩余的字符串
    ans = ""
    for c in s:
        if ord(c) >= ord('h'):  
            ans += c
    print(ans)
            