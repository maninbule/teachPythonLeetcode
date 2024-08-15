'''
O(n^2)
'''

A = [1,2,3,6,7,9,12,4,5,9,1,2,3,2,1]
n = len(A)
for i in range(n):
    min_id = i
    for j in range(i + 1,n):
        if A[j] < A[min_id]:
            min_id = j
    A[i],A[min_id] = A[min_id],A[i]
print(A)