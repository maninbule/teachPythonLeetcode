'''
https://leetcode.cn/problems/how-many-numbers-are-smaller-than-the-current-number/description/
'''
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [[nums[i],i] for i in range(n)]
        nums.sort(key = lambda x:x[0])
        ans = []
        j = -1
        for i in range(n):
            while j + 1 < n and nums[j + 1][0] < nums[i][0]:
                j += 1
            ans.append([j+1,nums[i][1]])
        ans.sort(key = lambda x:x[1])
        ans = [x[0] for x in ans]
        return ans

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = [[nums[i],i] for i in range(n)]
        nums.sort(key = lambda x:x[0])
        ans = [0] * n
        j = -1
        for i in range(n):
            while j + 1 < n and nums[j + 1][0] < nums[i][0]:
                j += 1
            index = nums[i][1]
            ans[index] = j + 1
        return ans