

# (1) 反复的询问某个数在不在一个list中，你能想到怎么去进行优化？
    arr = []
    st = set(arr)
    for t in range(1000):
        if t in st:
            print("in")
        else:
            print("no")
# (2) 列出你知道的对数组能执行的操作，写出对应的操作代码
    arr = []
    arr.append()
    arr.pop() 
    arr.pop(index)
    arr[::-1]
    arr.sort()
    arr.sort(reversed = True)
    arr.remove(value)
# (3) 列出你知道对字符串能执行的操作，写出对应的操作代码
    s = "abc"
    s[::-1]
    s[left:right+1]
    s = "abc" t = "cdr"
    s + t
    s.split()
    "+".join(list[str])
    s.find(str)
# (4) 一个函数可以用多少个return语句返回答案
    任意个

# (5) 什么是时间复杂度?
    程序的运行时间与数据量n的关系
# (6) 什么是空间复杂度?
    程序的占用内存大小与数据量n的关系
# (7) 给你99个数，这些数字都不一样，范围都是1-100其中的一个，问缺失了哪个数字？
    写出代码：
    arr = []
    st = set(arr)
    for x in range(1,101):
        if x not in st:
            return x
    return None
# (8) 给你n个数字，问哪两个数字加起来最大？
    写出代码：
    arr = []
    arr.sort()
    return arr[-1] + arr[-2]
# (9) 给你n个数字，问哪两个数字乘起来最大？
    写出代码：
    arr = []
    arr.sort()
    return max(arr[0]*arr[1],arr[-1]*arr[-2])
# (10) 给你n个数字,假如没有重复的数字，让你求出所有的ans[i],ans[i]表示这n个数中比第i个数大的有多少个？
    写出思路：
    写出代码：
    arr = [1,3,2,4,5]
    arr_with_index = []
    for i in range(len(arr)):
        arr_with_index.append([arr[i],i])
    arr_with_index.sort(key=lambda x:x[0])
    ans = [0] * len(arr)
    for i in range(len(arr)):
        ans[arr_with_index[i][1]] = len(arr) - i - 1
    print(ans)