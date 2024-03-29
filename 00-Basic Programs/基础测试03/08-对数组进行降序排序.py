
'''
08-对数组进行降序排序
'''

def descending(arr:list[int])->list[int]:
    # arr.sort(reverse=True)
    # return arr
    # ---------------第二种
    arr.sort(key=lambda x:-x)
    return arr

assert descending([3,2,1,4,5]) == [5,4,3,2,1]
assert descending([]) == []
assert descending([1]) == [1]
assert descending([1,2,3]) == [3,2,1]
print("pass")