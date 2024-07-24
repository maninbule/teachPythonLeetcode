'''
https://leetcode.cn/problems/count-number-of-pairs-with-absolute-difference-k/description/

'''
class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        for v in nums:
            cnt[v] += 1
        ans = 0
        nums = list(set(nums))
        for x in nums:
            ans += cnt[x] * cnt[x + k]
        return ans