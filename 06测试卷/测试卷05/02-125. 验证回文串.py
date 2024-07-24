'''
https://leetcode.cn/problems/valid-palindrome/description/
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                result += c.lower()
        left,right = 0,len(result)-1
        while left < right:
            if result[left] != result[right]:
                return False
            left,right = left + 1,right - 1
        return True
