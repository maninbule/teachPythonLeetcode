

'''
url: https://leetcode.cn/problems/intersection-of-multiple-arrays/description/
'''
from typing import List
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        # ans = []
        # for i in range(1,len(nums)):
        #     nums[i] = set(nums[i])
        # for v in nums[0]:
        #     all = True
        #     for i in range(1,len(nums)):
        #         if v not in nums[i]:
        #             all = False
        #             break
        #     if all == True:
        #         ans.append(v)
        # ans.sort()
        # return ans
        # ---------------第二种解法
        ans = []
        from collections import defaultdict
        count = defaultdict(int)
        for i in range(len(nums)):
            for v in nums[i]:
                count[v] += 1
        for key,value in count.items():
            if value == len(nums):
                ans.append(key)
        ans.sort()
        return ans



