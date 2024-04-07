'''
https://leetcode.cn/problems/reverse-prefix-of-word/description/
'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos = -1
        for i in range(len(word)):
            if word[i] == ch:
                pos = i
                break
        if pos == -1:
            return word
        left,right = word[:pos+1],word[pos+1:]
        return left[::-1] + right
