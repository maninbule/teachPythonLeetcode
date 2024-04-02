'''
https://leetcode.cn/problems/check-if-the-sentence-is-pangram/description/
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # st = set(sentence)
        # return len(st) == 26

        from collections import defaultdict
        cnt = defaultdict(int)
        for c in sentence:
            cnt[c] += 1 # cnt['a'] = 次数 而不是 cnt[97] = 次数
        # a 97 b 98 ..... z 122
        # ord('a') = 97  chr(97) = 'a'
        for ascii in range(ord('a'),ord('z') + 1):
            char = chr(ascii)
            if cnt[char] == 0:
                return False
        return True
