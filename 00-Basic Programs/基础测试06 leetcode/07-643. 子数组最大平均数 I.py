
'''
url: https://leetcode.cn/problems/maximum-average-subarray-i/description/
'''
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        from collections import deque
        dq = deque()
        sum = 0
        ans = 0
        first = True
        for v in nums:
            dq.append(v)
            sum += v
            if len(dq) > k:
                x = dq.popleft()
                sum -= x
            if len(dq) == k:
                if first == True: # 如果是第一次计算出答案，就直接赋值
                    ans = sum / k
                    first = False
                else: # 后面再算出答案，就跟之前记录的答案取最大值
                    ans = max(ans,sum/k)
        return ans