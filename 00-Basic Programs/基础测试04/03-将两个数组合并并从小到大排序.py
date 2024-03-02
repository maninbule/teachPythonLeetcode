'''
03-将两个数组合并,然后从小到大排序
'''

def mergeTwoArray(A:list[int],B:list[int])->list[int]:
    for b in B:
        A.append(b)
    A.sort()
    return A
    # C = A + B
    # C.sort()
    # return C

assert mergeTwoArray([1,4,3],[2,4,1,7]) == [1,1,2,3,4,4,7]
assert mergeTwoArray([1],[2,4,1,7]) == [1,1,2,4,7]
assert mergeTwoArray([1],[2]) == [1,2]
assert mergeTwoArray([1],[]) == [1]
assert mergeTwoArray([],[]) == []
print("pass")