'''
https://leetcode.cn/problems/3sum/description/
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        # 选 a + b + c = 0其中的a，
        for i in range(len(nums)):
            # 跳过重复的a
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            # 已经选择了a = nums[i]
            # 剩下的b + c = -a, 这样就变成了两数问题
            # 因为我们假定a是最小的，所以b和c一定是在下标i之后
            # 对[i + 1,n-1]这段区间进行两数之和
            # target = -a
            table = set()
            for j in range(i + 1, len(nums)):
                if j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    pass
                else:
                    need = -nums[i] - nums[j]
                    if need in table:
                        cur_ans = [nums[i], need, nums[j]]
                        ans.append(cur_ans)
                table.add(nums[j])
        return ans


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        # 选 a + b + c = 0其中的a，
        for i in range(len(nums)):
            # 跳过重复的a
            if i - 1 >= 0 and nums[i] == nums[i - 1]:
                continue
            # 已经选择了a = nums[i]
            # 剩下的b + c = -a, 这样就变成了两数问题
            # 因为我们假定a是最小的，所以b和c一定是在下标i之后
            # 对[i + 1,n-1]这段区间进行两数之和
            # target = -a
            target = - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # 跳过重复的b
                if left - 1 >= i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return ans


