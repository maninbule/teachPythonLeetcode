'''
url:https://leetcode.cn/problems/valid-palindrome/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
from typing import List


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for c in s:
            if c.isupper():
                c = c.lower()
                s2 += c
            elif c.islower():
                s2 += c
            elif c.isdigit():
                s2 += c
            else:
                continue
        left,right = 0,len(s2)-1
        while left < right:
            if s2[left] != s2[right]:
                return False
            left,right = left+1,right-1
        return True
