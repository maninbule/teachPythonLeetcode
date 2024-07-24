'''
https://leetcode.cn/problems/animal-shelter-lcci/description/
'''
from typing import List
from collections import deque
class AnimalShelf:

    def __init__(self):
        self.dog = deque()
        self.cat = deque()
        self.order = 1
    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self.cat.append([animal[0],animal[1],self.order])
        else:
            self.dog.append([animal[0], animal[1], self.order])
        self.order += 1
    def dequeueAny(self) -> List[int]:
        # dog cat 都不为空，cat为空，dog为空，两个都为空
        if len(self.dog) > 0 and len(self.cat) > 0:
            if self.dog[0][2] < self.cat[0][2]:
                item = self.dog.popleft()
                return item[:2]
            else:
                item = self.cat.popleft()
                return item[:2]
        elif len(self.dog) > 0:
            item = self.dog.popleft()
            return item[:2]
        elif len(self.cat) > 0:
            item = self.cat.popleft()
            return item[:2]
        else:
            return [-1,-1]

    def dequeueDog(self) -> List[int]:
        if len(self.dog) > 0:
            item = self.dog.popleft()
            return item[:2]
        else:
            return [-1,-1]

    def dequeueCat(self) -> List[int]:
        if len(self.cat) > 0:
            item = self.cat.popleft()
            return item[:2]
        else:
            return [-1,-1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()