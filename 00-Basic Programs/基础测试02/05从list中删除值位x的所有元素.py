
'''
05从list中删除值为x的所有元素
保留所有不等于x的元素，存放到一个新的list里面
arr = [1,3,3,5,6] x = 3

arr = [1,5,6]

'''

def deleteFromArray(arr:list[int],x:int)->list[int]:
    ans = [] # [1,5]
    for v in arr: # [1,3,3,5,6]
        if v != x: # v = 5 != 3
            ans.append(v)
    return ans

print(deleteFromArray([1,3,3,5,6],3))