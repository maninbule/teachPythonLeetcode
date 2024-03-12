'''
url:https://leetcode.cn/problems/positions-of-large-groups/description/
'''
from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        cnt = 0 # 当前出现了多少次
        left,right  = -1,-1 # 当前连续出现的字符，开始下标，和结束下标
        ans = []
        for i in range(len(s)):
            if i == 0 or s[i] != s[i-1]: # 不等于前一个字符
                if cnt >= 3:
                    ans.append([left,right])
                cnt = 1
                left = i
                right = i
            else: # 等于前一个字符
                cnt += 1
                right = i
        if cnt >= 3:
            ans.append([left,right])
        return ans

