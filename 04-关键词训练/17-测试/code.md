

# (1) 给你一个大小为nxn(n>=3)的list[list[int]]，请把里面的每一个3x3的子矩阵求最大值，放在一个(n-2)x(n-2)的答案矩阵中
    例子：输入
        [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
        输出：
        [[11,12],
        [15,16]]



    def solve(arr:list[list[int]])->list[list[int]]:
        n = len(arr)
        ans = [[0] * (n-2) for i in range(n-2)]
        for i in range(len(arr)):
            for j in range(len(arr)):
                # i i + 2,j,j + 2
                if i + 2 >= len(arr) or j + 2 >= len(arr[i]):
                    break
                mx = arr[i][j]
                for x in range(i,i + 3):
                    for y in range(j,j + 3):
                        mx = max(mx,arr[x][y])
                ans[i][j] = mx
        return ans
    
    input = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]
    print(solve(input))
# (2) 请使用栈来完成list[int]的翻转功能，(栈可以用list来实现)

# (3) 请使用栈来完成字符串s的翻转功能，(栈可以用list来实现)

# (4)  给你一个list[int]，请求出所有相邻k个元素的和，保存在一个list[int]进行返回
        要求使用队列来完成，队列里面实时记录已经放入队列的元素和
        例子：arr = [1,2,3,4,5,6] k = 3
        输出：[6,9,12,15]

# (5) 给你一个list[int]，计算一个ans数组，ans[i]表示arr[i]在arr中有多少个数是自己的约数(忽略arr[i]是arr[i]的约数)

# (6) 给你一个list[list[int]]，对这个数组进行排序，先按list[int]数组的长度从小到大排序，再按list[int]元素和从大到小排序

# (7) 给你两个dict,判断这两个dict内容是否完全一样(key,value都一样)，不能使用python内置dict == dict判断

# (8) 写一个class,构造函数会传入两个int a, b, 里面再加一个add函数，可以返回a和b的求和

# (9) 给你一个只有括号)和(组成的字符串s，判断里面的括号是否匹配
    例子：()()(()) -> true
        )() ->false
        (())) ->false
        ((()) ->false
# (10) 给你一个由字母和空格组成的字符串，请把其中的字母变成大小写交替(先大写)的形式，空格不变,
    例子："ab cA d  " ->"Ab Ca D  "
    def solve(s:str)->str:
        cnt = 0
        ans = ""
        for c in s:
            if c == ' ':
                ans += c
            else:
                cnt += 1
                if cnt%2 == 1:
                    ans += c.upper()
                else:
                    ans += c.lower()
        return ans
    
    input = "ab cA d  "
    print(solve(input))

    