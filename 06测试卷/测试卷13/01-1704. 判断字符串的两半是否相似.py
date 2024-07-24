'''
https://leetcode.cn/problems/determine-if-string-halves-are-alike/description/
'''

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        y = "aeiouAEIOU"
        cnt_left, cnt_right = 0,0
        n = len(s)
        # leftstr = s[:n//2]
        # rightstr = s[n//2:]
        # print(leftstr)
        # for c in leftstr:
        #     if c in y:
        #         cnt_left += 1
        # for c in rightstr:
        #     if c in y:
        #         cnt_right += 1
        # return cnt_left == cnt_right

        for i in range(n):
            if s[i] not in y:continue
            if i < n//2:
                cnt_left += 1
            else:
                cnt_right += 1
        return cnt_left == cnt_right

s = Solution()
print(s.halvesAreAlike("Ieai"))
