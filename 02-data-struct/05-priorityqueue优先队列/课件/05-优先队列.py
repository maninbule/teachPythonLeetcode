

class Node:
    def __init__(self,x:int):
        self.x = x
    def __lt__(self, other): # less than
        return self.x > other.x

from queue import PriorityQueue

q = PriorityQueue()

q.put(Node(2))
q.put(Node(1))

while q.qsize() > 0:
    print(q.get().x)

q.put(Node(3))
print(q.get().x)

