'''
题意：
let's implement a stack. Based on the ordinary stack data structure, we need to add a function to get the minimum value in the stack in real time.

思路:
Approach: Algorithm: Use two stacks
1. Use a primary stack to store the elements.
2. Use a secondary stack to keep track of the minimum elements. When pushing a new element, compare it with the current minimum and push the smaller one onto the minimum stack.
3. When popping an element, also pop from the minimum stack if the popped element is the current minimum.
4. The top element can be get from the primary stack, and the minimum element can be get from the secondary stack.
'''


# 代码

class MinStack:
    def init(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Stack to store minimum elements

    def push(self, val: int) -> None:
        self.stack.append(val)  # Push the value onto the main stack
        # Push the minimum value onto the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()  # Pop the top element from the main stack
            # If the popped element is the current minimum, pop it from min_stack as well
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None  # Return the top element

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None  # Return the minimum element


'''
Time Complexity: O(1) for all operations (push, pop, top, getMin). 

Space Complexity: O(n) in the worst case, where n is the number of elements in the stack, due to storing elements in two stacks. 
'''