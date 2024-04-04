'''
https://leetcode.cn/problems/count-square-sum-triples/description/
'''

# class Solution:
#     def countTriples(self, n: int) -> int:
#         cnt = 0
#         for a in range(1,n + 1): # 3
#             for b in range(1,n + 1): # 4
#                 c2 = a**2 + b**2
#                 c = int(c2**0.5)
#                 if c*c == c2 and c2 <= n**2:
#                     cnt += 1
#         return cnt

class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1,n + 1):
            for b in range(1,n + 1):
                for c in range(1,n + 1):
                    if a**2 + b**2 == c**2:
                        cnt += 1
        return cnt
s = Solution()
print(s.countTriples(12))