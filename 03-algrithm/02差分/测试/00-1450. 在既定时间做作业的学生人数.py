
'''
url:https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/description/
'''
from typing import List
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ca = [0] * 1010 # 存储差分数组
        n = len(startTime)
        for i in range(n): # 遍历每一个学生的时间区间
            l,r = startTime[i],endTime[i]
            ca[l] += 1 # 表示ca[l:] += 1
            ca[r + 1] -= 1 # 表示ca[r+1:] -= 1
                            # 实际表示就是ca[l:r] += 1
        pre = [0] * 1010 # 就是去存实际ca的样子
        pre[0] = ca[0] # 求前缀和
        for i in range(1,len(pre)):
            pre[i] = pre[i-1] + ca[i]
        return pre[queryTime]