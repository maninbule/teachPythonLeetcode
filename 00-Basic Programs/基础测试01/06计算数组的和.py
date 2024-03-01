

'''
给你一个list，请求出这个list里面所有元素的和
'''
def getsum(arr:list[int])->int:
    sum = 0
    for v in arr:
        sum += v
    return sum

print(getsum([1,2,3,4,5]))