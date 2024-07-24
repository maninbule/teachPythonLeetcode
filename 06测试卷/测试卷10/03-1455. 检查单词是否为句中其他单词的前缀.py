'''
https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
'''

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split()
        for i in range(len(arr)):
            s = arr[i]
            if len(searchWord) > len(s):
                continue
            ok = True
            for j in range(len(searchWord)): # len(searchWord) = 10, len(s) = 5
                if searchWord[j] != s[j]:
                    ok = False
                    break
            if ok:
                return i + 1
        return -1