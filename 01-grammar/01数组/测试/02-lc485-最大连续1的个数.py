'''
url:https://leetcode.cn/problems/max-consecutive-ones/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur = 0
        for v in nums:
            if v == 1:
                cur += 1
            else:
                cur = 0
            ans = max(ans,cur)
        return ans