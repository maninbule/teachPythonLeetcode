'''
url: https://leetcode.cn/problems/check-if-all-as-appears-before-all-bs/description/
'''

class Solution:
    def checkString(self, s: str) -> bool:
        # for i in range(len(s)): # 枚举a的下标
        #     if s[i] == 'a':
        #         for j in range(i):#[0,i-1] 找a的左边是否有一个b
        #             if s[j] == 'b':
        #                 return False
        # return True
        index_a = []
        index_b = []
        for i in range(len(s)):
            if s[i] == 'a':
                index_a.append(i)
            else:
                index_b.append(i)
        if len(index_a) == 0 or len(index_b) == 0:
            return True
        return max(index_a) < min(index_b)

