'''
https://leetcode.cn/problems/word-pattern/description/
'''

'''
{"a":{"dog","dog"},"b",{"cat","cat"}}

'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        from collections import defaultdict
        toWord = defaultdict(set)
        toChar = defaultdict(set)
        arr = s.split()
        if len(pattern) != len(arr):
            return False
        for i in range(len(pattern)):
            toWord[pattern[i]].add(arr[i])
            toChar[arr[i]].add(pattern[i])
            if len(toWord[pattern[i]]) > 1:
                return False
            if len(toChar[arr[i]]) > 1:
                return False
        return True

