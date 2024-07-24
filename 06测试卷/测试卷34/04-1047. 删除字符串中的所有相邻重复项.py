'''
https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/description/
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        sk = []
        for c in s:
            if len(sk) > 0 and sk[-1] == c:
                sk.pop()
            else:
                sk.append(c)
        return "".join(sk)