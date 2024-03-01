
'''
计算数组中的最大元素，并返回
'''
def getMax(arr:list[int])->int:
    ans = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > ans:
            ans = arr[i]
    return ans

print(getMax([4,2,1,6,4]))