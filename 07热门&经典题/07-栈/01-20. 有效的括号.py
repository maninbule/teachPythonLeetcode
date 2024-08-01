'''
https://leetcode.cn/problems/valid-parentheses/description/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        for c in s:
            if c in ['{','[','(']: # 左括号
                sk.append(c)
            else: # 右括号
                if len(sk) == 0:
                    return False
                elif c == ']' and sk[-1] != '[':
                    return False
                elif c == '}' and sk[-1] != '{':
                    return False
                elif c == ')' and sk[-1] != '(':
                    return False
                else: # 匹配上了
                    sk.pop()
        # 如果还有剩余的左括号没有被匹配，也要返回False
        if len(sk) > 0:
            return False
        return True

class Solution:
    def isValid(self, s: str) -> bool:
        sk = []
        table = {']':'[','}':'{',')':'('}
        for c in s:
            if c in table.values(): # 左括号
                sk.append(c)
            else: # 右括号
                if len(sk) == 0:
                    return False
                elif table[c] != sk[-1]:
                    return False
                else: # 匹配上了
                    sk.pop()
        # 如果还有剩余的左括号没有被匹配，也要返回False
        if len(sk) > 0:
            return False
        return True
