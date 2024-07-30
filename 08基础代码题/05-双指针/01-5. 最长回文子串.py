'''
https://leetcode.cn/problems/longest-palindromic-substring/description/
'''

class Solution:
    def getMaxlength(self,s:str,left:int,right:int)->str:
        while left >=0 and right < len(s):
            if s[left] != s[right]:
                return s[left + 1:right] # [left+1,right-1]
            left,right = left-1,right+1
        return s[left+1:right] # [left+1,right-1]
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            # i为中心轴.left = i-1,right = i+ 1
            ans1 = self.getMaxlength(s,i-1,i+1)
            if len(ans1) > len(ans):
                ans = ans1
            # i-1与i的中间空隙为中心轴，left=i-1,right = i
            ans2 = self.getMaxlength(s,i-1,i)
            if len(ans2) > len(ans):
                ans = ans2
        return ans
