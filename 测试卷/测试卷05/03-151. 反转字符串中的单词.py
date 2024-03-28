'''
https://leetcode.cn/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        left,right = 0,len(words)-1
        while left < right:
            words[left],words[right] = words[right],words[left]
            left,right = left + 1,right - 1
        return " ".join(words)