
'''
09-删除数组中前三大的元素
剩余元素保持原来的顺序

保证数组长度大于等于3
'''

def deleteTop3(arr:list[int])->list[int]:
    # 前三大的元素
    # set 把前三大的元素放到set里面
    # 进行一次arr数组拷贝，然后拷贝的那一份进行排序
    # 对排序后的前三大元素放进set
    # 遍历原来的arr，把非前三大的元素放进一个新的list里面
    from copy import copy
    top3 = set()
    cpy = copy(arr)
    # cpy = [x for x in arr]
    cpy.sort(key=lambda x:-x)
    for i in range(3):
        top3.add(cpy[i])
    ans = []
    for v in arr:
        if v not in top3:
            ans.append(v)
    return ans



assert deleteTop3([1,2,3,4]) == [1]
assert deleteTop3([4,5,6,2,1,3]) == [2,1,3]
assert deleteTop3([2,7,1,9,10,3]) == [2,1,3]
print("pass")