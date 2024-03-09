
'''
url: https://leetcode.cn/problems/range-sum-query-immutable/description/
'''
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.pre = [0] * len(nums)
        self.pre[0] = nums[0]
        for i in range(1,len(nums)):
            self.pre[i] = self.pre[i-1] + nums[i]
    def sumRange(self, left: int, right: int) -> int:
        if left == 0: # nums[0:right] pre[right] = nums[0] + ... nums[right]
            return self.pre[right]
        else: # left > 0, nums[0:left-1] nums[left:right]
            return self.pre[right] - self.pre[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)