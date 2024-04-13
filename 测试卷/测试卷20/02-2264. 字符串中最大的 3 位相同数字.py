'''
https://leetcode.cn/problems/largest-3-same-digit-number-in-string/description/
'''

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt = 1
        ans = ""
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                cnt += 1
                if cnt >= 3:
                    cur = num[i] * 3
                    if len(ans) == 0: ans = cur
                    else:ans = max(ans,cur)
            else:
                cnt = 1
        return ans

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                cur = num[i] * 3
                if ans == "":ans = cur
                else: ans = max(ans,cur)
        return ans