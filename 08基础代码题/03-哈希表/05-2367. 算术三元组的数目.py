'''
https://leetcode.cn/problems/number-of-arithmetic-triplets/
'''
from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        from collections import defaultdict
        n = len(nums)
        leftCnt = [0] * n # leftCnt[i] : 表示i左边有多少个nums[i] - diff这样的值
        rightCnt = [0] * n # 同理 nums[i] + diff
        count = defaultdict(int)
        for i in range(n):
            leftCnt[i] = count[nums[i] - diff]
            count[nums[i]] += 1
        count = defaultdict(int)
        for i in range(n-1,-1,-1):
            rightCnt[i] = count[nums[i] + diff]
            count[nums[i]] += 1
        ans = 0
        for i in range(n): # 以i为三元组的中间下标，来计算能构造的三元组的个数
            ans += leftCnt[i] * rightCnt[i]
        return ans

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        st = set()
        ans = 0
        for x in nums:
            if x - diff in st and x - 2*diff in st:
                ans += 1
            st.add(x)
        return ans