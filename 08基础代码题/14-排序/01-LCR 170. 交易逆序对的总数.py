'''
https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/description/
'''
from typing import List
class Solution:
    def mergeSort(self,A:list[int]):
        if len(A) == 1:
            return A,0
        mid = len(A)//2
        leftA = A[:mid]
        rightA = A[mid:]
        leftA,leftcnt = self.mergeSort(leftA)
        rightA,rightcnt = self.mergeSort(rightA)
        total = leftcnt + rightcnt  # 存储逆序对的个数
        # 就是对A数组进行归并排序，使用leftA,rightA两个进行归并
        # 并且在归并的过程中，进行计算leftA选择i，rightA选择j，能产生多少个逆序对
        i,j = 0,0
        B = []
        while i < len(leftA) and j < len(rightA):
            if leftA[i] > rightA[j]:
                # len(leftA) = 10 i = 2 [2,len(leftA))
                total += len(leftA) - i
                B.append(rightA[j])
                j += 1
            else:
                B.append(leftA[i])
                i += 1
        B += leftA[i:]
        B += rightA[j:]
        return B,total
    def reversePairs(self, record: List[int]) -> int:
        if record == []:
            return 0
        sortedArr,total = self.mergeSort(record)
        return total