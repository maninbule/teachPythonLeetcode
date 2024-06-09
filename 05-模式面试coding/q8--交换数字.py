'''
给你两个长度一样的数组A,B，里面全部都是int类型的元素
一次操作的步骤是：
交换A[i], B[i]
问最少多少次操作，可以使得数组A中所有元素都相等
如果做不到，得输出-1

输入:
1 2 2 5
3 1 1 1
输出:
1
'''
def solve(A:list[int],B:list[int])->int:
    from collections import defaultdict
    cnt = defaultdict(int)
    cntA = defaultdict(int)
    n = len(A)
    for i in range(n):
        cnt[A[i]] += 1
        cntA[A[i]] += 1
        if A[i] != B[i]:
            cnt[B[i]] += 1
    ans = -1
    for item,times in cnt.items():
        if times == n:
            if ans == -1:
                ans = n - cntA[item]
            else:
                ans = min(ans,n - cntA[item])
    return ans

print(solve([1,2,2,1],
            [2,1,1,2]))

print(solve([1,2,2,2],
            [2,1,1,2]))

print(solve([1,2,3,4],
            [4,5,6,7]))

print(solve([1,1,1,1],
            [1,1,1,1]))


print(solve([1,1,1,1],
            [2,2,2,2]))

print(solve([1,1,1,3],
            [2,2,2,2]))