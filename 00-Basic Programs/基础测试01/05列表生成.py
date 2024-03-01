
'''
给一个n，要求产生[0,n]之间，所有的奇数
并保存在一个list进行返回
例如：
输入：n = 6
输出：[1,3,5]
'''
def genList(n:int)->list[int]:
    ans = []
    for i in range(0,n + 1):
        if i % 2 == 1:
            ans.append(i)
    return ans

print(genList(6))