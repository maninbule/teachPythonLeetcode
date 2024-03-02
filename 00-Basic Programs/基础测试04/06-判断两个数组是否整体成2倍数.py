
'''
06-判断两个数组是否整体成2倍数

给你两个数组A和B
问是否A中的每个元素x，B中都有2倍x
'''

def IsHasAll(A:list[int],B:list[int])->bool:
    # for v in A: # 遍历每个A中的每个数
    #     # 对枚举出来的一个数，看B中是否存在它的2倍
    #     find = False
    #     for y in B:
    #         if y == 2*v:
    #             find = True
    #     if find == False:
    #         return False
    # return True
    # --------------第二种
    B = set(B)
    for v in A:
        if 2*v not in B:
            return False
    return True

assert IsHasAll([1,2],[4,2]) == True
assert IsHasAll([1,2],[4,2,6]) == True
assert IsHasAll([1,2],[2,6]) == False
assert IsHasAll([6,4],[2,6,12]) == False
print("pass")