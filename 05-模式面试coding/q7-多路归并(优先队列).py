

'''
n个生产线,m总共的物品数量
物品都有一个id

line1 : 2 7 18
line2 : 7 9 15 16
line3 : 1 2 3
...

line: 1 2 2 3 7 7 9 15 16 18
'''

from queue import PriorityQueue

class node:
    def __init__(self,value,id,index):
        self.value = value
        self.id = id
        self.index = index
    def __lt__(self, other): # less than
        return self.value < other.value
def merge(lines:list[list[int]])->list[int]:
    ans = []
    q = PriorityQueue()
    for i in range(len(lines)):
        if len(lines) > 0:
            q.put(node(lines[i][0],i,0))
    while q.qsize() > 0:
        cur = q.get()
        value,id,index = cur.value,cur.id,cur.index
        ans.append(value)
        if index + 1 < len(lines[id]):
            q.put(node(lines[id][index + 1],id,index + 1))
    return ans
# m * logn
lines = [[2,7,18],[7,9,15,16],[1,2,3]]
print(merge(lines))



