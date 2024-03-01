
'''

将一个list进行翻转后，返回
例如:
[1,2,3,4] 翻转后 [4,3,2,1]
'''
def reverse(arr:list[int])->list[int]:
    L,R = 0,len(arr)-1 # 
    while L < R:
        arr[L],arr[R] = arr[R],arr[L]
        L += 1
        R -= 1
    return arr

print(reverse([1,2,3,4])) # len([1,2,3,4]) = 4 - 1 = 3
print(reverse([1,2,3,4,5]))