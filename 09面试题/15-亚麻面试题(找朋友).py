'''
亚麻面试题
'''
'''
getFriends---可以返回一个人的所有朋友集合

Person--class

给你两个人，问这两个人是什么朋友类型

两个人是同一个人：返回0
两个不是同一个人，但是有一个共同的朋友(或者就是直接朋友)，返回1
没有任何关系，返回-1
======================
下面是follow up:
两个人没有共同的朋友，但是有朋友关系可以连接，返回最短的关系路径长度
'''
from collections import deque
class Person:
    def __init__(self,name):
        self.name = name
        self.friends = None
    def add_friends(self,friend:set):
        self.friends = friend
    def getFriends(self):
        return self.friends
def solution(a:Person,b:Person)->int:
    # 同一个人
    if a.name == b.name:
        return 0
    # 不同的人,但是有共同的朋友
    friendsOfb = b.getFriends()
    for p in a.getFriends():
        if p in friendsOfb:
            return 1
    return bfs(a,b)

def bfs(a:Person,b:Person)->int:
    q = deque()
    q.append([a,0]) # (点，层数)
    visited = set()
    visited.add(a)

    while len(q) > 0:
        curNode = q.popleft()
        curPerson = curNode[0]
        level = curNode[1]
        if curPerson.name == b.name:
            return level
        for friend in curPerson.getFriends():
            if friend in visited:
                continue
            q.append([friend,level + 1])
            visited.add(friend)
    return -1


a = Person('a')
b = Person('b')
c = Person('c')
d = Person('d')
e = Person('e')

a.add_friends({b})
b.add_friends({a,c,d})
c.add_friends({b,d})
d.add_friends({b,c,e})
e.add_friends({d})

print(solution(a,e))


