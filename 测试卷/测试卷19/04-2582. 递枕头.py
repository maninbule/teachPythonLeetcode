'''
https://leetcode.cn/problems/pass-the-pillow/
'''

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cur =  1
        dir = 1
        for t in range(time):
            if cur == n:
                dir = -1
            if cur == 1:
                dir = 1
            cur += dir
        return cur

