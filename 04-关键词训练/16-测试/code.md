



# (1) 给你一个list[list[int]]数组，里面的list[int]只有2个元素，请按照2个元素的和按从大到小排序
    例如:[[1,2],[3,8],[1,1],[2,5]] ->[[3,8],[2,5],[1,2],[1,1]] 

# (2) 给你一个list[list[int]]数组，里面的list[int]有任意个元素，请按照list[int]的和按从大到小排序
    例如:[[1,2],[8],[1,1,100],[2,5]] ->[[1,1,100],[8],[2,5],[1,2]]
    def sum_sort(arr:list[list[int]])->list[list[int]]:
        arr.sort(key=lambda x:-sum(x))
        return arr
    
    arr = [[1,2],[8],[1,1,100],[2,5]]
    print(sum_sort(arr))
# (3) 给你一个list[int]，请从左往右将两两相邻元素进行交换,不足2个的时候，保持不动
    例如:[1,2,3,4,5,6,7] -> [2,1,4,3,6,5,7]

# (4) 将下面函数包装成一个class，并创建一个对象进行测试
    def add(a:int,b:int)->c:int
        return a + b
# (5) 给你一个list[str],再给你一个由单词组成的字符串s，问哪些单词没有出现在list[str],保存在list[str]进行返回
    
# (7) 给你一个list[int],返回一个list[int],叫ans数组，ans[i]表示第i个元素左边最大的元素是谁，如果没有ans[i]=-1
    def left_max(arr:list[int])->list[int]:
        left_max_value = arr[0]
        ans = [-1] * len(arr)
        for i in range(1,len(arr)): # O(n)
            ans[i] = left_max_value
            left_max_value = max(left_max_value,arr[i]) # O(1)
        return ans
    
    arr = [2,4,7,5,6]
    print(left_max(arr)) # [-1,2,4,7,7]
# (8) 给你一个非负整数，输出菲薄拉切数列的第n项，f[0] = 1,f[1] = 1,后面的f[i] = f[i-1] + f[i-2]
    memo = dict()
    def fib(n:int)->int:
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 1
        res = fib(n-1) + fib(n-2) # fib(n) -> res
        memo[n] = res
        return res
    
    
    print(fib(100))

    def fib(n:int)->int:
        if n == 0 or n == 1:
            return 1
        f = [1] * (n + 1) # f[0] = 1,f[1] = 1
        for i in range(2,n + 1):
            f[i] = f[i-1] + f[i-2]
        return f[n]
    
    print(fib(1000))

    from functools import cache
    import sys
    sys.setrecursionlimit(10000)  # 设置最大递归次数为10000
    @cache
    def fib(n:int )->int:
        if n == 0 or n == 1:
            return 1
        return fib(n-1) + fib(n-2) # fib(n) -> res
    
    print(fib(1000))
# (9) 给你两个直角坐标(x1,y1),(x2,y2)输出这两个点的直线距离

# (10) 给你一个list[int]，将这个数组中的每一个int，只保留最后2位数，也就是保留十位和个位


