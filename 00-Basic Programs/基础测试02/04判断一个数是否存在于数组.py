
'''
04判断一个数是否存在于数组
'''

def exsited(arr:list[int],x:int)->bool:
    for v in arr:
        if v == x:
            return True
    return False

print(exsited([1,2,3,4],5))

