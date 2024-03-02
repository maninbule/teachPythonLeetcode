
'''
02-将数组的前一半升序后一半降序

保证数组的长度是偶数
将前一半的数组升序
将后一半的数组倒序
'''

def UPleftDownRight(arr:list[int])->list[int]:
    n = len(arr)
    left = arr[:n//2]
    right = arr[n//2:]
    left.sort()
    right.sort(reverse=True)
    return left + right

assert UPleftDownRight([2,1,3,4]) == [1,2,4,3]
assert UPleftDownRight([2,1]) == [2,1]
assert UPleftDownRight([]) == []
assert UPleftDownRight([7,2,5,6,8,1,3,7]) == [2,5,6,7,8,7,3,1]
print("pass")