'''
https://leetcode.cn/problems/two-sum/description/
'''

'''
思路：
arr = [1,2,11,19,5,7,6,15]
target = 9
hashmap存储的是已经遇到过的数字
存储方式是 key = 元素，value = index
hashmap = 
{
    1: 0,
    2: 1,
    11: 2,
    19: 3,
    5: 4,
}

x = 9 - 1 = 8
x = 9 - 2 = 7
x = 9 - 11 = -2
x = 9 - 19 = -10
x = 9 - 5 = 4
x = 9 - 7 = 2
return [1,5]
'''


from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = dict()
        for i in range(len(nums)):
            x = target - nums[i]
            if x in table:
                return [table[x],i]
            table[nums[i]] = i
        return [-1,-1]