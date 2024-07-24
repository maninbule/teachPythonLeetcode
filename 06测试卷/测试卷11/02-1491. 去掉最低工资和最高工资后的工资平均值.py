'''
https://leetcode.cn/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
'''
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        # 原始办法
        # salary.sort()
        # total = 0
        # for i in range(1,len(salary)-1):
        #     total += salary[i]
        # return total / (len(salary) - 2)
        # 方法二  切片
        # salary.sort()
        # salary = salary[1:-1]
        # tatal = 0
        # for x in salary:
        #     tatal += x
        # return tatal / len(salary)
        # 方法二 实际删除方法
        salary.sort()
        # salary.pop(0)
        # salary.pop(len(salary)-1)
        del salary[0]
        del salary[len(salary)-1]
        tatal = 0
        for x in salary:
            tatal += x
        return tatal / len(salary)

