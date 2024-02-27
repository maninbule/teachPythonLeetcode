
'''

url: https://leetcode.cn/problems/length-of-last-word/
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result =  s.split()
        return len(result[-1])