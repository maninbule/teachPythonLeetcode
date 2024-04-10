'''
https://leetcode.cn/problems/find-the-pivot-integer/description/
'''
# n -> 列方程 -> 求解

# n -> 如果有答案就，在(1,n)其中一个，那么把每一个可能的答案都拿去验证
class Solution:
    def pivotInteger(self, n: int) -> int:
        for x in range(1,n + 1):
            left_sum,right_sum = 0,0
            for y in range(1,x + 1):
                left_sum += y
            for y in range(x,n + 1):
                right_sum += y
            if left_sum == right_sum:
                return x
        return -1

class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum, right_sum = 0, 0
        # total = (1 + n) * n // 2
        total = 0
        for x in range(1,n + 1):total += x
        for x in range(1,n + 1):
            left_sum += x
            right_sum = total - left_sum + x
            if left_sum == right_sum:
                return x
        return -1
# x = 5
# left_sum
# x = 6
# left_sum + 6

# rignt_sum
# total = 1 + ... + n

# x = 6, left_sum
# right = total - left_sum + x

# [x,n] = [1,n] - [1,x] + x
#