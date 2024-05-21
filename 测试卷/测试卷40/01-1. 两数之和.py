'''
https://leetcode.cn/problems/two-sum/description/
'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visted = dict()
        for i in range(len(nums)):
            need = target - nums[i]
            if need in visted:
                return [i,visted[need]]
            visted[nums[i]] = i
        return [-1,-1]


def twosum(nums:list[int],target:int)->list[list[int]]:
    st = set()
    nums = list(set(nums))
    ans = []
    for x in nums:
        y = target - x
        if y in st:
            ans.append([x,y])
        st.add(x)
    return ans

input = [4,5,7,2,2,9,7]
print(twosum(input,9))