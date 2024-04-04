'''
https://leetcode.cn/problems/number-of-different-integers-in-a-string/description/
'''

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = ""
        for c in word:
            if c.isalpha():
                s += ' '
            else:
                s += c
        arr = s.split()
        st = set()
        for x in arr:
            x = int(x)
            st.add(x)
        return len(st)
