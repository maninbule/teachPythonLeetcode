'''
https://leetcode.cn/problems/min-stack-lcci/description/
'''

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sk = []
        self.sk_min = []
    def push(self, x: int) -> None:
        self.sk.append(x)
        if len(self.sk_min) == 0:
            self.sk_min.append(x)
        else:
            min_value = min(x,self.sk_min[-1])
            self.sk_min.append(min_value)
    def pop(self) -> None:
        self.sk.pop()
        self.sk_min.pop()

    def top(self) -> int:
        return self.sk[-1]

    def getMin(self) -> int:
        return self.sk_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()