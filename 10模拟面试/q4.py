'''

题意：
The question is to give a string, which consists of brackets, and ask whether the brackets in the string are completely matched.

思路：
Data structure used: stack
steps:
1.We can use a hash table to store the matching relationship of brackets
2.Define a stack to store the left brackets encountered while traversing the string
3. Traverse the string and push the left bracket encountered into the stack. If a right bracket is encountered, take the left bracket from the stack to see if it matches
4. The following three situations all indicate mismatches:
    (1). There is an extra right bracket, and when you want to match a left bracket, there is no left bracket in the stack
    (2) When the right bracket comes, the left bracket in the stack does not match the right bracket
    (3) All right brackets have been matched, but there are still left brackets in the stack that have not been matched.
    In all three cases, false is returned.
5. If the entire string is traversed and none of the above three situations occur, true is returned

举个例子：
Input: s = "([])"
The table stores the left bracket that matches each right bracket.
table = {']':'[',')':'(','}':'{'}
stack = []
i = 0   s[i] = '('  Put it on the stack  ,stack = ['(']
i = 1   s[i] = '['  Put it on the stack  ,stack = ['(','[']
i = 2   s[i] = ']'
            Take the left bracket '[' from the stack
            It was found that the brackets matched
            now stack = ['(']
i = 3 s[i] = ')'
            Take the left bracket '(' from the stack
            It was found that the brackets matched
            now stack = []
Finally, it is found that all the right brackets are matched, and the stack is empty, which means that all the left brackets are also matched.

'''

# 代码
def solution(s:str)->bool:
    table =  {']':'[',')':'(','}':'{'}
    # The values of the table are all the left brackets, and the keys of the table are all the right brackets.
    stack = []
    for c in s:
        if c in table.values(): # c is left bracket
            stack.append(c)
        else: # c is right bracket
            if len(stack) == 0:# When I wanted to match the left bracket, I found that there was no left bracket.
                return False
            leftbracket = stack.pop() # The current left bracket,
            should_leftbracket = table[c] #the left bracket that should be matched
            if leftbracket != should_leftbracket:
                return False
    if len(stack) > 0: # There are remaining left brackets that have not been matched
        return False
    else:
        return True

'''
Time complexity: O(n) Each character only needs to be traversed once
Space complexity: O(n) Because we need to store all the left brackets, the maximum number of left brackets can be n
'''
