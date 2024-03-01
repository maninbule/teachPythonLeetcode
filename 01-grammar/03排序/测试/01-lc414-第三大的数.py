from typing import List

'''
url:https://leetcode.cn/problems/third-maximum-number/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        st = set(nums)
        nums = list(st)
        nums.sort(reverse=True)
        if len(nums) >= 3:
            return nums[2]
        else:
            return nums[0]
        
            