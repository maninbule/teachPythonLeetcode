'''

题意：
Given an array, put all the 0s in the array at the end of the array, and keep the remaining elements in the previous order.
思路：
algorithm used: two pointers
steps:
1. We define two pointers, left and right, both initialized to 0
2. Left ponter always points to the next location where a non-zero element is to be stored
3. right ponter moves backward to find a non-zero element.
4. When the right pointer finds a non-zero element, the element pointed to by the right pointer is swapped with the element pointed to by the left pointer.
'''

# 代码
def solution(arr:list[int])->list[int]:
    # Define left pointer and right pointer
    left,right = 0,0
    while right < len(arr):
        if arr[right] != 0:
            # When it is found that the element pointed to by the right pointer is not 0, it is exchanged with the element pointed to by the left pointer.
            arr[left],arr[right] = arr[right],arr[left]
            left += 1
        right += 1
    return arr

# 例子
'''
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
firstly left = 0,right = 0
left = 0, right = 0  arr[right] = 0, so right = right + 1 = 1
left = 0, right = 1  arr[right] !=0, so swap arr[left] and arr[right]
    nums should change to  nums = [1,0,0,3,12]
    and left = left + 1 = 1, right = right + 1 = 2
left = 1, right = 2,arr[right] = 0,so right = right + 1 = 3
left = 1, right = 3,arr[right] =3 != 0,so swap arr[left] and arr[right]
    nums should change to  nums = [1,3,0,0,12]
    and left = left + 1 = 2, right = right + 1 = 4
left = 2, right = 4,arr[right] = 12 != 0,so swap arr[left] and arr[right]
    nums should change to  nums = [1,3,12,0,0]
    and left = left + 1 = 3, right = right + 1 = 5
right pointer has traversed all array indexes, and the for loop ends
return nums = [1,3,12,0,0]


Time complexity: O(n) Because the left pointer and the right pointer can only move to the right, the left pointer and the right pointer can move at most n times
Space complexity: O(1) because no new array needs to be created
'''