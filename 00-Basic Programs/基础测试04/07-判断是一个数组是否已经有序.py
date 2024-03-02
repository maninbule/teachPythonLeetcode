
'''
07-判断是一个数组是否已经有序

给你一个数组，判断这个数组是否已经从小到大排好序了

A[0] <= A[1] <= A[2] .... <= A[n-1]
'''

def isSorted(arr:list[int])->bool:
    for i in range(1,len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

assert isSorted([1,2,3,4,5]) == True
assert isSorted([1,2,3,5,4]) == False
assert isSorted([1]) == True
assert isSorted([]) == True
assert isSorted([2,1]) == False
assert isSorted([5,4,3,2,1]) == False
print("pass")