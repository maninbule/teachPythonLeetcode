'''
https://leetcode.cn/problems/find-the-sum-of-encrypted-integers/description/
'''
from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            x = list(str(x))
            length = len(x)
            mx = max(x)
            x = mx * length
            ans += int(x)
        return ans

