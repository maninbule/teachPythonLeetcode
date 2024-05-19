'''
https://leetcode.cn/problems/count-number-of-pairs-with-absolute-difference-k/description/
'''
from typing import List
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        for x in nums:
            cnt[x] += 1
        nums = list(set(nums))
        ans = 0
        for x in nums:
            ans += cnt[x] * cnt[x + k]
        return ans

nums = [1,2,2,1]
k = 1
s = Solution()
print(s.countKDifference(nums,k))


nums = [1,3]
k = 3
s = Solution()
print(s.countKDifference(nums,k))

nums = [3,2,1,5,4]
k = 2
s = Solution()
print(s.countKDifference(nums,k))