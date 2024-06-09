'''
https://leetcode.cn/problems/WhsWhI/description/
'''

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        st = set(nums)
        ans = 0
        for x in st:
            # 作为起点
            if x - 1 not in st:
                length = 1
                while x + 1 in st:
                    length += 1
                    x += 1
                ans = max(ans,length)
        return ans
# O(n) O(nlogn) O(n^2) n = 1000000, logn = 20    2^20 = 10**6
# 2^10 = 1024 = 1k
# 2^20 = 1024 * 1024 = 1M = 1e6 = 10^6
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums):
            return 0
        nums = list(set(nums))
        nums.sort()
        ans = 1
        length = 1
        for i in range(1,len(nums)):
            if nums[i-1] + 1 == nums[i]:
                length += 1
                ans = max(ans,length)
            else:
                length = 1
        return ans


