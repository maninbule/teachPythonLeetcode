'''
https://leetcode.cn/problems/valid-palindrome-ii/description/
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(s:str)->bool:
            return s == s[::-1] # O(n)
        left,right = 0,len(s)-1
        while left < right:
            if s[left] != s[right]:
                t1 = s[:left] + s[left + 1:]
                t2 = s[:right] + s[right + 1:]
                if isValid(t1) or isValid(t2):
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True
s = Solution()
print(s.validPalindrome("abc"))