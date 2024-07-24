'''
https://leetcode.cn/problems/count-vowel-substrings-of-a-string/description/
'''

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0
        for L in range(len(word)):
            cur = set()
            for R in range(L,len(word)):
                c = word[R]
                if c in "aeiou":
                    cur.add(c)
                else:
                    break
                if len(cur) == 5:
                    ans += 1
        return ans
