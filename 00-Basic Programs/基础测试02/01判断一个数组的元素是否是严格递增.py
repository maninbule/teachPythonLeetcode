'''

01判断一个数组的元素是否是严格递增

A = [1,2,3,4]  A[i] < A[i+1]  0<=i < len(A)-1
               A[0] A[1]
               A[1] A[2]
               A[2] A[3]

'''
def judge(arr:list[int])->bool:
    for i in range(0,len(arr)-1):
        if not arr[i] < arr[i+1]:
            return False
    return True

print(judge([4,3,2,1]))