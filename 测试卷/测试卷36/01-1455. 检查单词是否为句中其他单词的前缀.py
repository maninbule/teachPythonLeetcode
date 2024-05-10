'''
https://leetcode.cn/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
'''

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        arr = sentence.split()
        n = len(searchWord)
        for i in range(len(arr)):
            s = arr[i]
            if len(s) >= n and searchWord == s[:n]:
                return i + 1
        return -1