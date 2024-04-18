

# 所有题目都必须写成函数形式，把函数调用之后的结果使用print进行打印

# (1) 给你一个list[str],问其中出现1次的字符串有哪些，请保持在一个list[str]进行返回
    # defaultdict [int|str|tuple]
    def find_unique_string(arr:list[str])->list[str]:
        from collections import defaultdict
        mp = defaultdict(int)
        for s in arr:
            mp[s] += 1
        ans = []
        for key,value in mp.items():
            if value == 1:
                ans.append(key)
        return ans
    
    # 测试
    input = ["a","b","b","c","d","c"] # output: ["a","d"]
    print(find_unique_string(input))
# (2) 给你一个list[str],问其中出现2次的字符串有哪些，请保持在一个list[str]进行返回
    # defaultdict [int|str|tuple]
    def find_unique_string(arr:list[str])->list[str]:
        from collections import defaultdict
        mp = defaultdict(int)
        for s in arr:
            mp[s] += 1
        ans = []
        for key,value in mp.items():
            if value == 2:
                ans.append(key)
        return ans
    # 测试
    input = ["a","b","b","c","d","c"] # output: ["a","d"]
    print(find_unique_string(input))
# (3) 给你一个小写字母，请输出下一个字母，如果是z，则输出a
    例如：输入a,输出b
         输入y，输出z
         输入z，输出a
    def next_char(c:str)->str:
        next = chr((ord(c) - ord('a') + 1)%26 + ord('a'))
        return next
    
    # 测试
    
    print(next_char("z")) # output = "a"
    print(next_char("a")) # output = "b"
# (4) 给你两个坐标(x1,y1),(x2,y2) 计算这两点之间的直线距离(欧式距离)
    import math
    def get_distance(x1:int,y1:int,x2:int,y2:int)->float:
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
        # return ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5
    
    # 测试
    print(get_distance(1,1,2,2)) # output = 2**0.5
    print(get_distance(1,1,10,1)) # output = 9
    print(get_distance(1,1,1,10)) # output = 9

# (5) 给你两个坐标(x1,y1),(x2,y2) 计算这两点之间的哈密顿距离
    
# (6) 给你n个坐标(xi,yi),以list[list[int]]形式给你，将这些坐标进行排序，先按照x升序，如果x相等，则按照y降序排序
    def list_sort(arr:list[list[int]])->list[list[int]]:
        arr.sort(key=lambda x:(x[0],-x[1]))
        return arr
    
    # 测试
    arr = [[1,2],[1,1],[2,1],[3,-1],[2,5]]
    # output:[[1,2],[1,1],[2,5],[2,1],[3,-1]]
    print(list_sort(arr))
# (7) 给你n个坐标(xi,yi)，计算出哪两个点的直线距离最短，你只需要输出距离即可,不需要输出具体是哪两个点
    def get_distance(x1:int,y1:int,x2:int,y2:int)->float:
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)

    def get_min_distance(pos:list[list[int]])->float:
        ans = -1
        for i in range(len(pos)):
            x1,y1 = pos[i]
            for j in range(i + 1,len(pos)):
                x2,y2 = pos[j]
                if ans == -1:
                    ans = get_distance(x1,y1,x2,y2)
                else:
                    ans = min(ans,get_distance(x1,y1,x2,y2))
        return ans
    # 测试
    input = [[1,2],[1,1],[2,1],[3,-1],[2,5]]
    # output: 1
    print(get_min_distance(input))

# (8) 给你list[str] 将所有长度一样的字符串按顺序进行拼接，然后放到新的list[str]，再按照字符串长度进行排序
    例如：['a','b','abc','xyz','d']->['abd','abcxyz']
    # defaultdict key:int, value:list[str]
    def solve(arr:list[str])->list[str]:
        from collections import defaultdict
        mp = defaultdict(list[str])
        for s in arr:
            mp[len(s)].append(s)
        ans = []
        for key,value in mp.items(): # value = list[str]
            ans.append("".join(value))
        ans.sort(key=lambda x:len(x))
        return ans
    
    # 测试
    input = ['a','b','abc','xyz','d']
    # output = ['abd','abcxyz']
    print(solve(input))
# (9) 在x坐标轴上有n个点xi，你需要放一个新的点，这个点到这n个点的距离之和最小，请输出这个点
    
# (10) 给你三个int类型的变量a,b,c，问是否可以由a，b,c作为边长组成一个直角三角形
    

