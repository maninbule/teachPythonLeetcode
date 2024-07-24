'''
https://leetcode.cn/problems/reverse-words-in-a-string-iii/description/
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            w = words[i]
            words[i] = w[::-1]
        return " ".join(words)

s = Solution()
ans = s.reverseWords("Let's take LeetCode contest")
print(ans)
