
'''
给一个n，要求产生[0,n]之间，所有的奇数
并保存在一个list进行返回
例如：
输入：n = 6
输出：[1,3,5]
'''
def genList(n:int)->list[int]:
    #首先设一个ans 然后通过for循环对整个list进行iterale 可以知道了 i是整个list里存在的数量
    #然后通过if语句进行一个对于奇数的判断  奇数的判断是通过整个list的数量进行 %2（%取余 ） 有余数就是奇数
    #然后是奇数进行append进去ans
    ans = []
    for i in range(0,n + 1): # [0,n]
        if i % 2 == 1:
            ans.append(i)
    return ans

print(genList(6))