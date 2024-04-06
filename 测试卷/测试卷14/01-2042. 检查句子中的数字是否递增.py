'''
https://leetcode.cn/problems/check-if-numbers-are-ascending-in-a-sentence/description/
'''



class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        t = ""
        for c in s:
            if not c.isdigit():
                t += ' '
            else:
                t += c
        arr = t.split() # list[str] -> list[int]
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        for i in range(1,len(arr)):
            if arr[i-1] >= arr[i]:
                return False
        return True

s = Solution()
ans = s.areNumbersAscending("1 box has 3 blue 4 red 6 green and 12 yellow marbles")
print(ans)