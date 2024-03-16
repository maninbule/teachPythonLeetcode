'''
https://leetcode.cn/problems/ugly-number/description/
'''

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <=0:
            return False
        for v in [2,3,5]:
            while n % v == 0:
                n //= v
        if n == 1:
            return True
        else:
            return False