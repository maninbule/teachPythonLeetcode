'''
url:https://leetcode.cn/problems/contains-duplicate/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st = set(nums)
        if len(st) != len(nums):
            return True
        else:
            return False
