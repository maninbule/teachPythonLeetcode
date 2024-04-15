
def solve(h):
    length = len(h)
    L = [0] * length # L[i] 表示h[i] 左边最大的高度
    R = [0] * length # R[i] 表示h[i] 右边最大的高度
    lmx = 0 #
    rmx = 0
    res = 0
    for i in range(length): # 不断计算每一个h[i]左边的最大值
        L[i] = lmx
        lmx = max(lmx, h[i])
    for i in range(length - 1, -1, -1): # 不断更新每一个h[i] 右边的最大值
        R[i] = rmx
        rmx = max(rmx, h[i])
    for i in range(length): # 计算第i个位置能装多少水
        area = min(L[i], R[i]) - h[i]
        # h[i] 左右两边最大值的高度的较小高度，就是上限
        # h[i] 自身的高度就是下限，所以能装的水，就是当前位置i
        # 能装的水上限减去下限
        if area > 0:
            res += area # 加到总和
    return res

# 测试
print(solve([0,1,0,2,1,0,1,3,2,1,2,1]))


'''
思路：
计算所有能装水的量= 求和(所有位置i能装多少水)

位置i能装多少水，取决于他两边最高的高度的较小值

就类似于山谷能装多少水，取决于两边山峰的较小值

然后能装的水量，等于水能达到的高度减去第i个位置的高度(山谷的高度)


'''

