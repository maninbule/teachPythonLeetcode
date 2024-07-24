'''
https://leetcode.cn/problems/can-place-flowers/description/
'''
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i - 1 >= 0 and flowerbed[i-1] == 1:
                continue
            if i + 1 < len(flowerbed) and flowerbed[i + 1] == 1:
                continue
            flowerbed[i] = 1
            count += 1
        if count >= n:
            return True
        else:
            return False


s = Solution()
ans = s.canPlaceFlowers([1,0,0,0,0,1],2)
print(ans)
