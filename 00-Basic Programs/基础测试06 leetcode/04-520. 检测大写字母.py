
'''
url: https://leetcode.cn/problems/detect-capital/description/
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def judge1():
            for c in word:
                if c.islower():
                    return False
            return True
        def judge2():
            for c in word:
                if c.isupper():
                    return False
            return True
        def judge3():
            if word[0].islower():
                return False
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
            return True
        return judge1() or judge2() or judge3()