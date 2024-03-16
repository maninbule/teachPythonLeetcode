
'''
url: https://leetcode.cn/problems/length-of-last-word/
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[-1])