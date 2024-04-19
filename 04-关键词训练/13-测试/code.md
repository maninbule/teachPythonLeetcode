
# 所有都用函数来写

# (1) 给你一个字符串，判断字符串中出现的数字和字母的个数是否一样

# (2) 给你一个字符串，问字符串中的数字和字母是否交替出现
    例如：1a2b3c -> yes
# (3) 给你一个list[int],问一共有多少种这样的(a,b,c)元素，满足a + b == c
    def solve(arr:list[int])->int:
        st = set()
        for i in range(len(arr)):
            for j in range(len(arr)):
                for k in range(len(arr)):
                    if i != j and j != k and i != k:
                        if arr[i] + arr[j] == arr[k]:
                            st.add((arr[i],arr[j],arr[k]))
        return len(st)
    
    # 测试
    arr = [2,2,2,1,3,4]
    print(solve(arr)) # 5  (2,2,4),(1,3,4),(3,1,4),(1,2,3),(2,1,3)
# (4) 给你一个int变量，问这个变量是否是质数

# (5) 给你一个区间[L,R]，返回出现在这个区间的最小质数

# (6) 给你三个坐标(xi,yi)，问这三个坐标组成的三角形，是否是等边三角形
    import math

    def get_dis(p1:list[int],p2:list[int])->float:
        x1,y1 = p1
        x2,y2 = p2
        return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    def solve(points:list[list[int]])->bool:
        d1 = get_dis(points[0],points[1])
        d2 = get_dis(points[1], points[2])
        d3 = get_dis(points[0], points[2])
        return d1 == d2 == d3
# (7) 给你两个list[int], 问这两个数组是否排序之后，一模一样

# (8) 给你三个字符变量a,b,c，再给你一个字符串s，问这三个字符变量哪一个在字符串s中出现的次数最多，如果有一样多的，输出任意一个
    def solve(a:str,b:str,c:str,s:str)->str:
        a_cnt,b_cnt,c_cnt = 0,0,0
        for x in s:
            if x == a:
                a_cnt += 1
            if x == b:
                b_cnt += 1
            if x == c:
                c_cnt += 1
        if a_cnt >= max(b_cnt,c_cnt):
            return a
        if b_cnt >= max(a_cnt,c_cnt):
            return b
        return c

    # 测试
    print(solve("a","b","c","aabbbcccc")) # output: c
    print(solve("a","b","c","aabbcccc12424hf")) # output: c
    print(solve("a","b","c","aabbbccc")) # output: b or c
        
# (9) 给你一个list[int]，按照int的十进制长度进行从小到大排序，排序之后，还是一个List[int]

# (10) 给你两个int，问这两个数有多少个公共约数
    def solve(a:int,b:int)->int:
        ans = 0
        for i in range(1,min(a,b) + 1):
            if a % i == 0 and b % i == 0:
                ans += 1
        return ans
    
    # 测试
    print(solve(12,18)) # 1,2,3,6 -> 4
