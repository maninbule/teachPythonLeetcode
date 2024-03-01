from typing import List

'''
url:https://leetcode.cn/problems/relative-sort-array/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        A = []
        B = []
        for v in arr1:
            if v in arr2:
                A.append(v)
            else:
                B.append(v)
        P = [0] * 1001
        for i in range(len(arr2)):
            P[arr2[i]] = i
        A.sort(key = lambda x: P[x])
        B.sort()
        C = A + B
        return C

        