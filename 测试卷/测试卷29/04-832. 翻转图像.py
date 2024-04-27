'''
https://leetcode.cn/problems/flipping-an-image/description/
'''
from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = [x^1 for x in image[i][::-1]]
        return image
