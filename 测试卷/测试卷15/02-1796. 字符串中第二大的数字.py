'''
https://leetcode.cn/problems/second-largest-digit-in-a-string/
'''

class Solution:
    def secondHighest(self, s: str) -> int:
        st = set()
        for c in s:
            if c.isdigit():
                st.add(int(c))
        arr = list(st)
        arr.sort()
        if len(arr) < 2:
            return -1
        else:
            return arr[-2]


class Solution:
    def secondHighest(self, s: str) -> int:
        # "abc9cxx765" cnt = 0

        cnt = 2
        for x in range(9, -1, -1):
            c = str(x)
            if c in s:
                cnt -= 1
                if cnt == 0:
                    return int(c)
        return -1
