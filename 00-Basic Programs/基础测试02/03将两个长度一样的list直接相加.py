
'''
03将两个长度一样的list直接相加成一个新的list
C[i] = A[i] + B[i]

保证A和长度和B的长度一样
例如：
A = [1,2,3,4]
B = [0,1,2,3]

C = [1,3,5,7]
'''
def addArray(arr1:list[int],arr2:list[int])->list[int]:
    C = []
    for i in range(len(arr1)):# 0 1 2 3
        C.append(arr1[i] + arr2[i])
        # C = [1]
        # C = [1,3]
        # C = [1,3,5]
        # C = [1,3,5,7]
    return C

def addArray2(arr1:list[int],arr2:list[int])->list[int]:
    C = [0] * len(arr1)
    for i in range(len(arr1)):
        C[i] = arr1[i] + arr2[i]
    return C

print(addArray2([1,2,3,4],[0,1,2,3]))