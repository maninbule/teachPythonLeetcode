
'''
02将list所有的奇数位元素和偶数位元素互换
例子：
[1,2,3,4]

[2,1,4,3]

保证list的长度是偶数

'''

def swap(arr:list[int])->list[int]:
    for i in range(0,len(arr),2): # 0 2 4 
        arr[i],arr[i+1] = arr[i+1],arr[i] 
        # arr[i] arr[i + 1]
        # arr[0] arr[1]
        # arr[2] arr[3]
    return arr

print(swap([1,2,3,4]))
