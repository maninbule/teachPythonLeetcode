'''
https://leetcode.cn/problems/delete-characters-to-make-fancy-string/description/
'''

class Solution:
    def makeFancyString(self, s: str) -> str:
        # 记录当前字母连续出现了多少次，只有出现前1，2次的时候，才把这个
        # 字母加到答案中
        ans = ""
        curChar = None
        cnt = 0
        for c in s:
            if c != curChar:
                cnt = 1
                curChar = c
            else:
                cnt += 1
            if cnt <= 2:
                ans += curChar
        return ans
