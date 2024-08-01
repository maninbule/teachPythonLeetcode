'''
https://leetcode.cn/problems/reverse-words-in-a-string-iii/description/
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        curWord = ""
        for i in range(len(s)):
            if s[i] == ' ':
                if i - 1 >=0 and s[i-1] != ' ':
                    ans += curWord[::-1]
                    curWord = ""
                ans += s[i]
            else:
                curWord += s[i]
        return ans + curWord[::-1]

s = Solution()
ans = s.reverseWords("Let's    take LeetCode  contest")
print(ans)