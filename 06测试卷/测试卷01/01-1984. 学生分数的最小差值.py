from typing import List

'''
https://leetcode.cn/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
'''
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1] - nums[0]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if j - i + 1 == k: # [i,j]
                    ans = min(ans,nums[j] - nums[i])
        return ans
