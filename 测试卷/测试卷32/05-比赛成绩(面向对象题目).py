# 面向对象题目

'''
题目：
    现在需要你设计一个比赛成绩看板，可以实时显示前k个最好成绩的(名字，成绩)，如果目前不足k个成绩，就返回所有的
    要以成绩从高到低排序，成绩的范围在0-100
    初始化的时候，就给你一个k
    看板有以下功能：
    1. 添加一个比赛成绩(名字，成绩)
    2. 给出名字，查询这个人的成绩是多少
    3. 返回成绩最好的前k个人的成绩(名字，成绩)

请设计合理的数据结构，并写出一个class来完成这个设计
并进行写一个例子，进行测试
'''
import queue
from queue import PriorityQueue


class node:
    def __init__(self, name: str, sc: int):
        self.name = name
        self.sc = sc
    def __lt__(self, other):
        return self.sc < other.sc
class ScoreBoard:
    def __init__(self,k:int):
        self.k = k
        self.q = PriorityQueue()
        self.getScoreByName = dict()
    def addScore(self,name:str,sc:int):
        self.getScoreByName[name] = sc
        self.q.put(node(name,sc))
        if self.q.qsize() > self.k:
            self.q.get()
    def getScoreBynameFun(self,name:str)->int:
        return self.getScoreByName[name]
    def topkScore(self)->list[list]:
        ans = []
        while self.q.qsize() > 0:
            cur_node = self.q.get()
            name,sc = cur_node.name,cur_node.sc
            ans.append([name,sc])
        for name,sc in ans:
            self.q.put(node(name,sc))
        ans.sort(key=lambda x:-x[1])
        return ans

s = ScoreBoard(3)
s.addScore('A',88)
s.addScore('B',88)
s.addScore('C',90)
s.addScore('D',60)
print(s.getScoreBynameFun('C'))
print(s.topkScore())
s.addScore('E',100)
print(s.topkScore())

