'''
给你很多二维平面的坐标(可能存在重复)
例如：
输入:
[[1,1],[2,2],[0,4],[1,1]]
问有多少对坐标，他们的横坐标的差小于等于2 纵坐标的差小于等于2 (碰撞)
输出:4
解释：[1,1] 和 [1,1]
     [1,1] 和 [2,2]
     [1,1] 和 [2,2]
     [2,2] 和 [0,4]
'''

def solve(pos:list[list[int]])->int:
    n = len(pos)
    res = 0
    for i in range(n):
        a = pos[i]
        for j in range(i + 1,n):
            b = pos[j]
            if abs(a[0] - b[0]) <= 2 and abs(a[1] - b[1]) <= 2:
                res += 1
    return res
#print(solve([[1,1],[2,2],[0,4],[1,1]]))

# 优化1： 面对这样的输入： pos = [[1,1],[1,1],[1,1],[1,1],[2,2],[2,2],[2,2]]

def solve(pos:list[list[int]])->int:
    from collections import defaultdict
    cnt = defaultdict(int)
    res = 0
    for p in pos:
        cnt[(p[0],p[1])] += 1
    for p,count in cnt.items():
        res += count * (count - 1)//2
    pos = list(cnt.keys())
    for i in range(len(pos)):
        a = pos[i]
        for j in range(i + 1,len(pos)):
            b = pos[j]
            if abs(a[0] - b[0]) <= 2 and abs(a[1] - b[1]) <= 2:
                res += cnt[a] * cnt[b]
    return res
print(solve([[1,1],[2,2],[0,4],[1,1]]))


# 优化2： 一个点看可以和哪些发生碰撞，就先枚举自己周围能发生碰撞的点，再去哈希表里面查询次数
def solve(pos:list[list[int]])->int:
    from collections import defaultdict
    cnt = defaultdict(int)
    res = 0
    for p in pos:
        cnt[(p[0],p[1])] += 1
    pos = list(cnt.keys())
    for i in range(len(pos)):
        a = pos[i]
        for dx in range(-2,3):
            for dy in range(-2,3):
                b = (a[0] + dx,a[1] + dy)
                if a == b:
                    continue
                res += cnt[a] * cnt[b]
    res //= 2
    for p,count in cnt.items():
        res += count * (count - 1)//2
    return res
print(solve([[1,1],[2,2],[0,4],[1,1]]))