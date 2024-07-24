'''
https://leetcode.cn/problems/keyboard-row/description/
'''

class Solution:
    def wordsAllinSet(self,word:str,row:set):
        for c in word:
            if c not in row:
                return False
        return True
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        ans = []
        for w in words:
            w_cpy = w
            w = w.lower()
            if self.wordsAllinSet(w,row1) or self.wordsAllinSet(w,row2) or self.wordsAllinSet(w,row3):
                ans.append(w_cpy)
        return ans
